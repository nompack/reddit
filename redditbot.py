import praw
import time
import datetime
import requests
import requests.auth



reddit = praw.Reddit(client_id='1rRYW4ILxwgADQ',
                     client_secret='heJu5lZGOClfEWnNR8CC3NFPZw4',
                     username='hacksorskillbot',
                     password='fastlol1234',
                     user_agent='reputation bot by hacksorskill')

client_auth = requests.auth.HTTPBasicAuth('1rRYW4ILxwgADQ', 'heJu5lZGOClfEWnNR8CC3NFPZw4')
post_data = {"grant_type": "password", "username": "hacksorskillbot", "password": "fastlol1234"}
headers = {"User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                         headers=headers)
resp = response.json()
headers = {"Authorization": "bearer " + resp['access_token'], "User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
resp = response.json()


# look for phrase and reply appropriately
print('hi')
reddit.redditor('hacksorskill').message('I am a rep bot created by /u/hacksorskill')


