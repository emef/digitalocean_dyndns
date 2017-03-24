import os
import requests

API_KEY = os.environ['DIGITALOCEAN_API_KEY']
DOMAIN = os.environ['DIGITALOCEAN_DOMAIN']
DNS_RECORD_NAME = os.environ['DIGITALOCEAN_DNS_NAME']
AUTH_HEADERS = {'Authorization': 'Bearer %s' % API_KEY}
GET_RECORDS_API_URL = (
    'https://api.digitalocean.com/v2/domains/%s/records' % DOMAIN)
UPDATE_RECORD_API_URL_FMT = (
    'https://api.digitalocean.com/v2/domains/%s/records/%s')

def getCurrentDnsRecord():
    resp = requests.get(
        GET_RECORDS_API_URL, headers=AUTH_HEADERS)
    resp.raise_for_status()
    return [
        record for record in resp.json()['domain_records']
        if record['name'] == DNS_RECORD_NAME][0]

def updateDnsRecord(record_id, ip):
    url = UPDATE_RECORD_API_URL_FMT % (DOMAIN, record_id)
    resp = requests.put(url, headers=AUTH_HEADERS, data={'data': ip})
    resp.raise_for_status()

def getCurrentIp():
    return requests.get('http://httpbin.org/ip').json()['origin']

if __name__ == '__main__':
    current_record = getCurrentDnsRecord()
    current_ip = getCurrentIp()
    if current_ip != current_record['data']:
        updateDnsRecord(current_record['id'], current_ip)
        print 'Updated DNS record from %s to %s' % (
            current_record['data'], current_ip)
