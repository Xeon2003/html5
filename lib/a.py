from base import Base
from attr.href import Href
from attr.media import Media
from attr.rel import Rel
from attr.form import Name

class A( Base, Href, Media, Rel, Name ):
	_baseClass = "a"

	def __init__(self, *args, **kwargs):
		super(A,self).__init__( *args, **kwargs )

	def _getDownload(self):
		"""
		The download attribute specifies the path to a download
		@return: filename
		"""
		return self.element.download

	def _setDownload(self,val):
		"""
		The download attribute specifies the path to a download
		@param val: filename
		"""
		self.element.download = val






