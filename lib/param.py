from widget import Widget
from attr.form import Name,Value

class Param( Widget,Name,Value ):
    _baseClass = "param"

    def __init__(self, *args, **kwargs):
        super(Param,self).__init__( *args, **kwargs )





