import praw
import time
import datetime
import requests
import requests.auth
import uslapi

usl = uslapi.UniversalScammerList('bot testing stuff by /u/hacksorskill')
user = usl.login('hacksorskill', 'fastlol1234')

reddit = praw.Reddit(client_id='1rRYW4ILxwgADQ',
                     client_secret='heJu5lZGOClfEWnNR8CC3NFPZw4',
                     username='hacksorskillbot',
                     password='fastlol1234',
                     user_agent='bot by hacksorskill')

client_auth = requests.auth.HTTPBasicAuth('1rRYW4ILxwgADQ', 'heJu5lZGOClfEWnNR8CC3NFPZw4')
post_data = {"grant_type": "password", "username": "hacksorskillbot", "password": "fastlol1234"}
headers = {"User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                         headers=headers)
resp = response.json()
headers = {"Authorization": "bearer " + resp['access_token'], "User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
resp = response.json()

keyphrase = '$bid'

# look for phrase and reply appropriately

listofcomments = []
for submission in reddit.redditor('hacksorskill').stream.comments():

    try:
        if keyphrase in submission.body.lower() and int(time.time()) - int(submission.created_utc) < 300:
            parent = submission.parent()

            print(parent.author)
            userz = reddit.redditor(str(parent.author))
            karma = userz.link_karma + userz.comment_karma
            datecreated = (datetime.datetime.fromtimestamp(userz.created_utc))
            print(datecreated)
            print(karma)
            namez = userz.name
            data = usl.query(user, userz.name)
            if data['banned']:
                print(userz.name + " is on the universal Scammer List. Be careful!")
                banned = (userz.name + " is on the universal Scammer List. Be careful!")
            else:
                print(userz.name + " is not on the Universal Scammer List.")
                banned = (userz.name + " is not on the Universal Scammer List.")

            print("OP's name is " + userz.name + "\nOP has a total of " + str(
                karma) + " karma" + "\nOP's account was created on " + str(datecreated) + "\n" + str(
                banned) + "\n" + "I am a bot created by /u/hacksorskill, pm me for more info")
            submission.reply("OP's name is " + userz.name + "\n\nOP has a total of " + str(
                karma) + " karma" + "\n\nOP's account was created on " + str(datecreated) + "\n\n" + str(
                banned) + "\n\n" + "I am a bot created by /u/hacksorskill, pm me for more info")

    except:
        reddit.redditor('hacksorskill').message("User Info",
                                                "OP's name is " + userz.name + "\n\nOP has a total of " + str(
                                                    karma) + " karma" + "\n\nOP's account was created on " + str(
                                                    datecreated) + "\n\n" + str(
                                                    banned) + "\n\n" + "I am a bot created by /u/hacksorskill, pm me for more info")












