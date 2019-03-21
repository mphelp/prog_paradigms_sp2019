#!/escnfs/home/cmc/public/python/bin/python3
# Name: Matthew Phelps
# Date: Mar 20 2019

import requests
import json

class _webservice_primer:
	def __init__(self):
		self.SITE_URL = 'http://student04.cse.nd.edu:51001'
		self.MOVIES_URL = self.SITE_URL + '/movies/'
		self.RESET_URL = self.SITE_URL + '/reset/'
	def get_movie(self, mid):
		if not mid:
			raise ValueError('movie id must be specified')
			return
		r = requests.get(self.MOVIES_URL + str(mid))
		resp = json.loads(r.content.decode('utf-8'))		
		return resp

if __name__ == '__main__':
	MID = 43 # my mid
	ws = _webservice_primer()

	movie = ws.get_movie(MID)
	if movie['result'] == 'success':
		print('Title:\t{title}'.format(**movie))
	else:
		print('Error:\t{message}'.format(**movie))
