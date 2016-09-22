from widget import Widget
from attr.src import Src
from attr.media import Type,Dimensions
class Embed( Widget,Src,Type,Dimensions):
	_baseClass = "embed"

	def __init__(self, *args, **kwargs):
		super(Embed,self).__init__( *args, **kwargs )