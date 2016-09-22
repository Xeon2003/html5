from widget import Widget
from attr.cite import Datetime
class Time( Widget ,Datetime):
    _baseClass = "time"

    def __init__(self, *args, **kwargs):
        super(Time,self).__init__( *args, **kwargs )
