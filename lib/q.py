from widget import Widget
from attr.cite import Cite
class Q( Widget,Cite ):
    _baseClass = "q"

    def __init__(self, *args, **kwargs):
        super(Q,self).__init__( *args, **kwargs )


