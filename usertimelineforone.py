# -*- coding: utf-8 -*-
from weibo import APIClient
import linecache
import simplejson as json
import re, time, MySQLdb, os
import idlist

APP_KEY = '3419072486' # app key
APP_SECRET = '5f3a96a94ff0b9b3e5e54f310d606343' # app secret
CALLBACK_URL = 'http://apps.weibo.com/zhangmukelusidina' # callback url


access_token = linecache.getline('oauthcode', 1).strip()
expires_in= linecache.getline('oauthcode', 2).strip()

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)





r=client.get.statuses__user_timeline(screen_name=u'李开复')
rs=json.dumps(r)
rsl=json.loads(rs)

#print rsl
print rsl['statuses'][1]['id']
print rsl['statuses'][2]['id']
print rsl['statuses'][3]['id']
print rsl['statuses'][4]['id']
print rsl['statuses'][5]['id']
print rsl['statuses'][6]['id']
#In [17]: type(rsl)
#Out[17]: dict

#In [18]: rsl.keys()
#Out[18]: 
#['hasvisible',
# 'total_number',
# 'previous_cursor',
# 'next_cursor',
# 'marks',
# 'statuses']
