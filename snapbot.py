
 
import praw
import time

import requests
import requests.auth
document = open('donecomments.txt', 'w+')


reddit = praw.Reddit(client_id='1rRYW4ILxwgADQ',
                     client_secret='heJu5lZGOClfEWnNR8CC3NFPZw4',
                     username='hacksorskillbot',
                     password='fastlol1234',
                     user_agent='bot by hacksorskill')
                    

client_auth = requests.auth.HTTPBasicAuth('1rRYW4ILxwgADQ', 'heJu5lZGOClfEWnNR8CC3NFPZw4')
post_data = {"grant_type": "password", "username": "hacksorskillbot", "password": "fastlol1234"}
headers = {"User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
resp = response.json()
headers = {"Authorization": "bearer " + resp['access_token'], "User-Agent": "personalbot/0.1 by hacksorskill"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
resp=response.json()


        
keyphrase = 'snap'


# look for phrase and reply appropriately
subreddit = reddit.subreddit('thanosdidnothingwrong')


for submission in subreddit.stream.comments():
    if keyphrase in submission.body.lower() and submission.id not in document.read():
        print (submission.body)
        try:
            submission.reply('You said SNAP! The hardest choices require the strongest wills')
            document.write(submission.id)
            print(submission.id)
            document.close()
            print("saved")
            bashCommand = "dir"
            import subprocesss
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            document = open('donecomments.txt', 'w+')
            print(document.read())
            print(submission.id + "is the id")
            continue
        except:
            print("You have been rate limited trying again in 1 minutes")
            time.sleep(60)
            document = open('donecomments.txt', 'w+')
            continue
        

            
        
