# -*- coding: utf-8 -*-
from weibo import APIClient
import simplejson as json
import re
import linecache
import time

APP_KEY = '' # your app key
APP_SECRET = '' # your app secret
CALLBACK_URL = '' # your callback url

access_token = linecache.getline('oauthcode', 1).strip() #some user's access token
expires_in= linecache.getline('oauthcode', 2).strip() # some user's access timelimit


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)


def searchtwsgraph(cid):
	def _countpages(cid):
		r = client.get.statuses__repost_timeline(id=cid)
		rs = json.dumps(r)
        	rsl = json.loads(rs)
		total_number = rsl['total_number']
		return total_number/50+1
	total_number = _countpages(cid)
	print 'loop1, total_page:',total_number,cid
	time.sleep(30)
	for n in range(total_number):
		try:
			r=client.get.statuses__repost_timeline(id=cid,page=1+n,count=50)
			rs=json.dumps(r)
			rsl=json.loads(rs)
			print 'loop1, total_repor:50'
			for i in range(len(rsl['reposts'])):
				print rsl['reposts'][i]['text'],rsl['reposts'][i]['reposts_count']
				if rsl['reposts'][i]['reposts_count'] !=0:
					print rsl['reposts'][i]['reposts_count'],rsl['reposts'][i]['mid']
					time.sleep(30)
					searchtwsgraph(rsl['reposts'][i]['mid'])
		except:
			pass
		time.sleep(30)

if __name__ == '__main__':
	
	cid=3480029851960633 #any tweet'S mid
	searchtwsgraph(cid)
