# LICENSE: MIT (see LICENSE)
import requests

SITE = 'https://www.publictransport.com.mt'
API_VERSION = '1.3.1'
TIMEOUT = 60

def req(endpoint, data):
    return requests.post(SITE+endpoint, data=data, timeout=TIMEOUT,
        headers={'x-api-version': API_VERSION})

def check(resp):
    if resp.status_code != requests.codes.ok:
        return 'Request failed: '+resp.status_code+' '+resp.reason
    try:
        resp = resp.json()
    except ValueError as e:
        return 'Malformed response: '+str(e)
    if not resp['CommonRet']['Result']:
        return 'Balance query failed: '+resp['CommonRet']['ResultDesc']
    return resp
