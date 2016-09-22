from widget import Widget
from attr.media import Media
from attr.src import Src

class Source( Widget,Media,Src ):
    _baseClass = "source"

    def __init__(self, *args, **kwargs):
        super(Source,self).__init__( *args, **kwargs )





