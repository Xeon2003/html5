from html5.widget import Widget
class _Form(object):
	def _getForm(self):
		return self.element.form
	def _setForm(self,val):
		self.element.form=val

class Alt(object):
	def _getAlt(self):
		return self.element.alt
	def _setAlt(self,val):
		self.element.alt=val

class Autofocus(object):
	def _getAutofocus(self):
		return( True if self.element.hasAttribute("autofocus") else False )
	def _setAutofocus(self,val):
		if val==True:
			self.element.setAttribute("autofocus","")
		else:
			self.element.removeAttribute("autofocus")

class Disabled(object):
	def _setDisabled(self,val):
		Widget._setDisabled( self, val )
		if self._getDisabled():
			self.element.disabled = True
		else:
			self.element.disabled = False

class Checked(object):
	def _getChecked(self):
		return self.element.checked

	def _setChecked(self,val):
		self.element.checked = val

class Indeterminate(object):
	def _getIndeterminate(self):
		return (self.element.indeterminate)
	def _setIndeterminate(self,val):
		self.element.indeterminate=val

class Name(object):
	def _getName(self):
		return self.element.getAttribute( "name" )
	def _setName(self,val):
		self.element.setAttribute( "name", val )

class Value(object):
	def _getValue(self):
		return self.element.value
	def _setValue(self,val):
		self.element.value=val

class Autocomplete(object):
	def _getAutocomplete(self):
		return True if self.element.autocomplete=="on" else False
	def _setAutocomplete(self,val):
		self.element.autocomplete="on" if val==True else "off"

class Required(object):
	def _getRequired(self):
		return( True if self.element.hasAttribute("required") else False )
	def _setRequired(self,val):
		if val==True:
			self.element.setAttribute("required","")
		else:
			self.element.removeAttribute("required")

class Multiple(object):
	def _getMultiple(self):
		return( True if self.element.hasAttribute("multiple") else False )
	def _setMultiple(self,val):
		if val==True:
			self.element.setAttribute("multiple","")
		else:
			self.element.removeAttribute("multiple")

class Size(object):
	def _getSize(self):
		return self.element.size
	def _setSize(self,val):
		self.element.size=val

class __For(object):
	def _getFor(self):
		return self.element.getAttribute("for")
	def _setFor(self,val):
		self.element.setAttribute("for",val)

class Inputs(Required):
	def _getMaxlength(self):
		return self.element.maxlength
	def _setMaxlength(self,val):
		self.element.maxlength=val

	def _getPlaceholder(self):
		return self.element.placeholder
	def _setPlaceholder(self,val):
		self.element.placeholder=val

	def _getReadonly(self):
		return( True if self.element.hasAttribute("readonly") else False )
	def _setReadonly(self,val):
		if val==True:
			self.element.setAttribute("readonly","")
		else:
			self.element.removeAttribute("readonly")

class Formhead(object):
	def _getFormaction(self):
		return self.element.formaction
	def _setFormaction(self,val):
		self.element.formaction=val

	def _getFormenctype(self):
		return self.element.formenctype
	def _setFormenctype(self,val):
		self.element.formenctype=val

	def _getFormmethod(self):
		return self.element.formmethod
	def _setFormmethod(self,val):
		self.element.formmethod=val

	def _getFormtarget(self):
		return self.element.formtarget
	def _setFormtarget(self,val):
		self.element.formtarget=val

	def _getFormnovalidate(self):
		return( True if self.element.hasAttribute("formnovalidate") else False )
	def _setFormnovalidate(self,val):
		if val==True:
			self.element.setAttribute("formnovalidate","")
		else:
			self.element.removeAttribute("formnovalidate")
