from ..lib import *
from ..utils import *
from button import Button

class Popup(Div):
	def __init__(self, title=None, id=None, *args, **kwargs ):
		super(Popup, self).__init__(*args, **kwargs)

		self["class"] = "alertbox"
		if title:
			lbl = Span()
			lbl["class"].append("title")
			lbl.appendChild( TextNode( title ) )
			self.appendChild( lbl )

		# id can be used to pass information to callbacks
		self.id = id

		self.frameDiv = Div()
		self.frameDiv["class"] = "popup"

		self.frameDiv.appendChild( self )
		Body().appendChild( self.frameDiv )

	def close(self, *args, **kwargs):
		Body().removeChild( self.frameDiv )
		self.frameDiv = None

class Alert(Popup):
	"""
	Just displaying an alerting message box with OK-button.
	"""
	def __init__(self, msg, title=None, okCallback=None, okLabel="OK", *args, **kwargs):
		super(Alert, self).__init__(title, *args, **kwargs)
		self.addClass("alert")

		self.okCallback = okCallback

		message = Span()
		message.addClass("alert-msg")
		self.appendChild(message)

		if isinstance(msg, Widget):
			message.appendChild(msg)
		else:
			textToHtml(message, msg)

		okBtn = Button(okLabel, callback=self.onOkBtnClick)
		okBtn.addClass("alert-btn-ok")
		self.appendChild(okBtn)

		self.sinkEvent("onKeyDown")
		okBtn.focus()

	def drop(self):
		self.okCallback = None
		self.close()

	def onOkBtnClick(self, sender=None):
		if self.okCallback:
			self.okCallback(self)

		self.drop()

	def onKeyDown(self, event):
		if hasattr(event, "key"):
			key = event.key
		elif hasattr(event, "keyIdentifier"):
			key = event.keyIdentifier
		else:
			key = None

		if key == "Enter":
			event.stopPropagation()
			event.preventDefault()
			self.onOkBtnClick()

class YesNoDialog( Popup ):
	def __init__(self, question, title=None, yesCallback=None, noCallback=None, yesLabel="Yes", noLabel="No", *args, **kwargs):
		super( YesNoDialog, self ).__init__( title, *args, **kwargs )
		self["class"].append("yesnodialog")

		self.yesCallback = yesCallback
		self.noCallback = noCallback

		lbl = Span()
		lbl["class"].append("question")
		self.appendChild(lbl)

		if isinstance(question, Widget):
			lbl.appendChild(question)
		else:
			textToHtml(lbl, question)

		btnYes = Button(yesLabel, callback=self.onYesClicked )
		btnYes["class"].append("btn_yes")
		self.appendChild(btnYes)

		if len(noLabel):
			btnNo = Button(noLabel, callback=self.onNoClicked )
			btnNo["class"].append("btn_no")
			self.appendChild(btnNo)

		self.sinkEvent("onkeydown")
		btnYes.focus()

	def onkeydown(self, event):
		if hasattr(event, "key"):
			key = event.key
		elif hasattr(event, "keyIdentifier"):
			# Babelfish: Translate 'keyIdentifier' into 'key'
			if event.keyIdentifier in ['Esc', 'U+001B']:
				key = "Escape"
			else:
				key = event.keyIdentifier
		else:
			key = None

		if "Enter" == key:
			event.stopPropagation()
			event.preventDefault()
			self.onYesClicked()
		elif "Escape" == key:
			event.stopPropagation()
			event.preventDefault()
			self.onNoClicked()

	def drop(self):
		self.yesCallback = None
		self.noCallback = None
		self.close()

	def onYesClicked(self, *args, **kwargs ):
		if self.yesCallback:
			self.yesCallback( self )

		self.drop()

	def onNoClicked(self, *args, **kwargs ):
		if self.noCallback:
			self.noCallback( self )

		self.drop()

class SelectDialog( Popup ):

	def __init__( self, prompt, items=None, title=None, okBtn="OK", cancelBtn="Cancel", forceSelect=False, *args, **kwargs ):
		super( SelectDialog, self ).__init__( title, *args, **kwargs )
		self["class"].append("selectdialog")

		# Prompt
		if prompt:
			lbl = Span()
			lbl[ "class" ].append( "prompt" )
			lbl.appendChild( TextNode( prompt ) )
			self.appendChild( lbl )

		# Items
		self.items = []

		if not forceSelect and len( items ) <= 3:
			for item in items:
				btn = Button( item.get( "title" ), callback=self.onAnyBtnClick )
				btn._callback = item.get( "callback" )

				if item.get( "class" ):
					btn[ "class" ].extend( item[ "class" ] )

				self.appendChild( btn )
				self.items.append( btn )
		else:
			self.select = Select()
			self.appendChild( self.select )

			for i, item in enumerate( items ):
				opt = Option()

				opt[ "value" ] = str( i )
				opt._callback = item.get( "callback" )
				opt.appendChild( TextNode( item.get( "title" ) ) )

				self.select.appendChild( opt )
				self.items.append( opt )

			if okBtn:
				self.appendChild( Button( okBtn, callback=self.onOkClick ) )

			if cancelBtn:
				self.appendChild( Button( cancelBtn, callback=self.onCancelClick ) )

	def onAnyBtnClick( self, sender = None ):
		for btn in self.items:
			if btn == sender:
				if btn._callback:
					btn._callback( self )
				break

		self.items = None
		self.close()

	def onCancelClick(self, sender = None ):
		self.close()

	def onOkClick(self, sender = None ):
		if self.select[ "selectedIndex" ] < 0:
			return

		item = self.items[ int( self.select[ "options" ].item( self.select[ "selectedIndex" ] ).value ) ]
		if item._callback:
			item._callback( self )

		self.items = None
		self.select = None
		self.close()
