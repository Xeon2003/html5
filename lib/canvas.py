from widget import Widget
from attr.media import Dimensions
class Canvas( Widget,Dimensions):
	_baseClass = "canvas"

	def __init__(self, *args, **kwargs):
		super(Canvas,self).__init__( *args, **kwargs )