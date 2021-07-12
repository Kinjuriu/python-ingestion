# Write a function, given the github login, will return how much time they are members of github

"""Query GitHub API"""
from datetime import datetime
from urllib.request import urlopen
import json


def user_time(login):
    url = 'https://docs.github.com/en/rest/reference/users' + login
    resp = urlopen(url)
    reply = json.load(resp)
    # "2008-01-14T04:33:35Z", we trim the 'Z' with [:-1]
    ts = reply['created_at']
    created = datetime.fromisoformat(ts[:-1])
    return datetime.utcnow() - created


login = 'Kinjuriu'
print(user_time(login))

