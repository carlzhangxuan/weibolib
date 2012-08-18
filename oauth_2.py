from weibo import APIClient
import simplejson as json
import re,webbrowser

APP_KEY = '3419072486' # app key
APP_SECRET = '5f3a96a94ff0b9b3e5e54f310d606343' # app secret
CALLBACK_URL = 'http://apps.weibo.com/zhangmukelusidina' # callback url
code= raw_input('code from web : ')

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in

f = open('oauthcode','w')
f.write(access_token+'\n')
f.write(str(expires_in))
print str(access_token)+r','+str(expires_in)
f.close()
