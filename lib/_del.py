from widget import Widget
from attr.cite import Cite,Datetime
class _Del( Widget,Cite,Datetime):
	_baseClass = "_del"

	def __init__(self, *args, **kwargs):
		super(_Del,self).__init__( *args, **kwargs )