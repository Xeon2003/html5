from widget import Widget
from attr.cite import Cite,Datetime

class Ins( Widget ,Cite,Datetime):
    _baseClass = "ins"

    def __init__(self, *args, **kwargs):
        super(Ins,self).__init__( *args, **kwargs )
