from weibo import APIClient
import simplejson as json
import re,webbrowser

APP_KEY = '3419072486' # app key
APP_SECRET = '5f3a96a94ff0b9b3e5e54f310d606343' # app secret
CALLBACK_URL = 'http://apps.weibo.com/zhangmukelusidina' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
