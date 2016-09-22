from widget import Widget
from attr.href import Href
from attr.media import Media
from attr.rel import Rel

class Link( Widget,Href,Media,Rel ):
	_baseClass = "link"

	def __init__(self, *args, **kwargs):
		super(Link,self).__init__( *args, **kwargs )

	def _getSizes(self):
		return self.element.sizes
	def _setSizes(self,val):
		self.element.sizes=val



