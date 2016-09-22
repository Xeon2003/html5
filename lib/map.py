from widget import Widget
from attr._label import _Label as Label
from attr.media import Type
class Map( Widget ,Label,Type):
    _baseClass = "map"

    def __init__(self, *args, **kwargs):
        super(Map,self).__init__( *args, **kwargs )
