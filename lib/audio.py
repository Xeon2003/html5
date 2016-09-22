from widget import Widget
from attr.src import Src
from attr.media import Multimedia
class Audio( Widget,Src,Multimedia ):
	_baseClass = "audio"

	def __init__(self, *args, **kwargs):
		super(Audio,self).__init__( *args, **kwargs )
