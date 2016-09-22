from widget import Widget
from attr.href import Href,Target

class Base( Widget,Href ,Target):
	_baseClass = "base"

	def __init__(self, *args, **kwargs):
		super(Base,self).__init__( *args, **kwargs )
