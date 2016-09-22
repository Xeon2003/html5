from ..lib import *
from .popup import Popup
from .button import Button

class InputDialog(Popup):
	def __init__(self, text, value="", successHandler=None, abortHandler=None, successLbl="OK", abortLbl="Cancel", *args, **kwargs ):
		super( InputDialog, self ).__init__(*args, **kwargs)
		self["class"].append("inputdialog")
		self.successHandler = successHandler
		self.abortHandler = abortHandler

		span = Span()
		span.element.innerHTML = text
		self.appendChild(span)
		self.inputElem = Input()
		self.inputElem["type"] = "text"
		self.inputElem["value"] = value
		self.appendChild( self.inputElem )
		okayBtn = Button(successLbl, self.onOkay)
		self.appendChild(okayBtn)
		cancelBtn = Button(abortLbl, self.onCancel)
		self.appendChild(cancelBtn)
		self.sinkEvent("onkeydown")
		self.inputElem.focus()

	def onkeydown(self, event):
		if hasattr(event, 'key'):
			key = event.key
		elif hasattr(event, 'keyIdentifier'):
			# Babelfish: Translate 'keyIdentifier' into 'key'
			if event.keyIdentifier in ['Esc', 'U+001B']:
				key = 'Escape'
			else:
				key = event.keyIdentifier
		if 'Enter' == key:
			event.stopPropagation()
			event.preventDefault()
			self.onOkay()
		elif 'Escape' == key:
			event.stopPropagation()
			event.preventDefault()
			self.onCancel()

	def onOkay(self, *args, **kwargs):
		if self.successHandler:
			self.successHandler( self, self.inputElem["value"] )
		self.close()

	def onCancel(self, *args, **kwargs):
		if self.abortHandler:
			self.abortHandler( self, self.inputElem["value"] )
		self.close()
