from widget import Widget
from attr.media import Type,Dimensions,Usemap
from attr.form import _Form as Form,Name
class Object( Widget,Type,Form,Name,Dimensions,Usemap ):
    _baseClass = "object"

    def __init__(self, *args, **kwargs):
        super(Object,self).__init__( *args, **kwargs )





