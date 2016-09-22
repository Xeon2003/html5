from widget import Widget
from attr._label import _Label as Label
from attr.media import Type
from attr.form import Disabled,Checked
class Command( Widget, Label,Type,Disabled,Checked):
	_baseClass = "command"

	def __init__(self, *args, **kwargs):
		super(Command,self).__init__( *args, **kwargs )

	def _getIcon(self):
		return self.element.icon
	def _setIcon(self,val):
		self.element.icon=val

	def _getRadiogroup(self):
		return self.element.radiogroup
	def _setRadiogroup(self,val):
		self.element.radiogroup=val