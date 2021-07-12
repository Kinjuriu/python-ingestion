#APIs are a way of calling remote servers for data alias RPC
#RPC- Remote Procedure Call
#One of the most common way to call an API is by using the http protocol with objects and call it as JSON
#In the terminal, run the web server python httpd.py, remember to run httpd.py and the trips.json file altogether

"""Calling HTTP + JSON API using requests"""
import requests


url = 'http://localhost:8989/trips'
query = {
    'start': '2018-11-01T00:02:04',
    'end': '2018-11-01T00:44:51',
}
headers = {
    'x-trips-token': 'l3tm3in',
}


resp = requests.get(url, params=query, headers=headers)
if not resp.ok:
    raise SystemExit(f'FAIL: {resp.status_code} - {resp.reson}')

reply = resp.json()
if not reply['ok'] or 'trips' not in reply:
    raise SystemExit(f'bad reply - {reply}')

count = len(reply['trips'])
print(f'Total of {count} trips found')
