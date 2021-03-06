import html5


class Popup(html5.Div):
	def __init__(self, title=None, id=None, className=None, *args, **kwargs):
		super(Popup, self).__init__(*args, **kwargs)

		self["class"] = "alertbox"
		if className is not None and len(className):
			self["class"].append(className)

		if title:
			lbl = html5.Span()
			lbl["class"].append("title")
			lbl.appendChild(html5.TextNode(title))
			self.appendChild(lbl)

		# id can be used to pass information to callbacks
		self.id = id

		self.frameDiv = html5.Div()
		self.frameDiv["class"] = "popup"

		self.frameDiv.appendChild(self)
		html5.Body().appendChild(self.frameDiv)

	def close(self, *args, **kwargs):
		html5.Body().removeChild(self.frameDiv)
		self.frameDiv = None


class Alert(Popup):
	"""
	Just displaying an alerting message box with OK-button.
	"""

	def __init__(self, msg, title=None, okCallback=None, okLabel="OK", *args, **kwargs):
		super(Alert, self).__init__(title, *args, **kwargs)
		self.addClass("alert")

		self.okCallback = okCallback

		message = html5.Span()
		message.addClass("alert-msg")
		self.appendChild(message)

		if isinstance(msg, html5.Widget):
			message.appendChild(msg)
		else:
			html5.utils.textToHtml(message, msg)

		okBtn = html5.ext.Button(okLabel, callback=self.onOkBtnClick)
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


class YesNoDialog(Popup):
	def __init__(self, question, title=None, yesCallback=None, noCallback=None, yesLabel="Yes", noLabel="No", *args,
	             **kwargs):
		super(YesNoDialog, self).__init__(title, *args, **kwargs)
		self["class"].append("yesnodialog")

		self.yesCallback = yesCallback
		self.noCallback = noCallback

		lbl = html5.Span()
		lbl["class"].append("question")
		self.appendChild(lbl)

		if isinstance(question, html5.Widget):
			lbl.appendChild(question)
		else:
			html5.utils.textToHtml(lbl, question)

		btnYes = html5.ext.Button(yesLabel, callback=self.onYesClicked)
		btnYes["class"].append("btn_yes")
		self.appendChild(btnYes)

		if len(noLabel):
			btnNo = html5.ext.Button(noLabel, callback=self.onNoClicked)
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

	def onYesClicked(self, *args, **kwargs):
		if self.yesCallback:
			self.yesCallback(self)

		self.drop()

	def onNoClicked(self, *args, **kwargs):
		if self.noCallback:
			self.noCallback(self)

		self.drop()


class SelectDialog(Popup):

	def __init__(self, prompt, items=None, title=None, okBtn="OK", cancelBtn="Cancel", forceSelect=False,
	                callback=None, *args, **kwargs):
		super(SelectDialog, self).__init__(title, *args, **kwargs)
		self["class"].append("selectdialog")

		self.callback = callback
		self.items = items
		assert isinstance(self.items, list)

		# Prompt
		if prompt:
			lbl = html5.Span()
			lbl["class"].append("prompt")

			if isinstance(prompt, html5.Widget):
				lbl.appendChild(prompt)
			else:
				html5.utils.textToHtml(lbl, prompt)

			self.appendChild(lbl)

		# Items
		if not forceSelect and len(items) <= 3:
			for idx, item in enumerate(items):
				if isinstance(item, dict):
					title = item.get("title")
					cssc = item.get("class")
				elif isinstance(item, tuple):
					title = item[1]
					cssc = None
				else:
					title = item

				btn = html5.ext.Button(title, callback=self.onAnyBtnClick)
				btn.idx = idx

				if cssc:
					btn.addClass(cssc)

				self.appendChild(btn)
		else:
			self.select = html5.Select()
			self.appendChild(self.select)

			for idx, item in enumerate(items):
				if isinstance(item, dict):
					title = item.get("title")
				elif isinstance(item, tuple):
					title = item[1]
				else:
					title = item

				opt = html5.Option(title)
				opt["value"] = str(idx)

				self.select.appendChild(opt)

			if okBtn:
				self.appendChild(html5.ext.Button(okBtn, callback=self.onOkClick))

			if cancelBtn:
				self.appendChild(html5.ext.Button(cancelBtn, callback=self.onCancelClick))

	def onAnyBtnClick(self, sender):
		item = self.items[sender.idx]

		if isinstance(item, dict) and item.get("callback") and callable(item["callback"]):
			item["callback"](item)

		if self.callback:
			self.callback(item)

		self.items = None
		self.close()

	def onCancelClick(self, sender=None):
		self.close()

	def onOkClick(self, sender=None):
		assert self.select["selectedIndex"] >= 0
		item = self.items[int(self.select.children(self.select["selectedIndex"])["value"])]

		if isinstance(item, dict) and item.get("callback") and callable(item["callback"]):
			item["callback"](item)

		if self.callback:
			self.callback(item)

		self.items = None
		self.select = None
		self.close()
