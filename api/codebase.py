import urllib2, base64 
import elementtree.ElementTree as ET
from django.conf import settings

class CodeBase(object):
	"""CodeBase XML API Wrapper"""

	def __init__(self,*args,**kwargs):
		self.top_url = getattr(settings,'CODEBASE_TOP_URL',"https://api3.codebasehq.com")
		self.account = getattr(settings,'CODEBASE_ACCOUNT')
		self.user = getattr(settings,'CODEBASE_USER')
		self.passwd = getattr(settings,'CODEBASE_PASSWD')
		self.project = getattr(settings,'CODEBASE_PROJECT')

	def get(self,query,*args,**kwargs):
		data = None
		headers = { 
			'Accept': 'application/xml', 
			'Content-type': 'application/xml',
			'Authorization': "Basic " + base64.encodestring(
				'%s/%s:%s'%(self.account,self.user,self.passwd)
			).replace('\n', '')
		} 
		url = self.top_url + '/%s/%s'%(self.project,query)
		req = urllib2.Request(url, data, headers) 
		res = urllib2.urlopen(req)
		#print res.read()
		return ET.parse(res).getroot()

	def search(self,query,*args,**kwargs):
		return self.get("tickets?query=%s"%query)

