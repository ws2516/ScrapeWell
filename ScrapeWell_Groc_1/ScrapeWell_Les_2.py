import requests


''' works
url = 'https://www.basketball-reference.com'

myobj = {'search': 'lebron james'}

x = requests.post(url, data = myobj)

class="search-item-name"

print(x.text)'''


''' works - this is the bitescrape
url = 'https://www.yelp.com/login'

myobj = {'email': 'brilliantscarcity354@gmail.com', 'password':'Hello1234'}

x = requests.post(url, data = myobj)

print(x.text)'''

''' Doesnt wokr
url = 'https://www.yelp.com/'

myobj = {'find_desc': 'coffee nyc'}

x = requests.post(url, data = myobj, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})

print(x.text)'''


#this is for the lesson

#url = 'https://www.ebay.com/sch/i.html?'

params = {'_from': 'R40',
'_trksid':'p2380057.m570.l1311',
'_nkw': '3080+rtx',
'_sacat': '0'}

headers = {'Accept': '*/*',
'Content-Type': 'text/plain',
'Accept-Encoding': 'gzip, deflate, br',
'Host': 'www.ebay.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
'Referer': 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw=3080+rtx&_sacat=0',
'Accept-Language': 'en-us',
'Connection': 'keep-alive'}

response = requests.get(url, params = params)
response.text

'''import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.publix.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'services.publix.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Referer': 'https://www.publix.com/savings/all-deals',
    'Connection': 'keep-alive',
    'PublixStore': '1720',
}

params = (
    ('smImg', '150'),
    ('enImg', '262'),
    ('fallbackImg', 'false'),
    ('isMobile', 'false'),
    ('page', '1'),
    ('pageSize', '0'),
    ('includePersonalizedDeals', 'true'),
)

response = requests.get('https://services.publix.com/api/v4/savings', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://services.publix.com/api/v4/savings?smImg=150&enImg=262&fallbackImg=false&isMobile=false&page=1&pageSize=0&includePersonalizedDeals=true', headers=headers)
'''

import requests

cookies = {
    'CIUser': 'b3df89ca0aa281efb753dbc3414043a0a1e75f1c0473f441c7f53e71eb9cbdc6de88219f55a618cc01708043df0b1e3500feb555ddde8dfe36bbfce01ad994b097a0673cd2d96bc371eb37871e9073fe8c4711a2e9211795a3a667fa0c8e3f8b',
    '_vwo_uuid_v2': 'D31B13805A6140D7020BCAB22837392A4|8c83019e7760f7f7d7eac24430ad9346',
    '_fbp': 'fb.1.1622976934498.1141808830',
    '_ga': 'GA1.2.1397215564.1622976934',
    '_gat_catalogspreeTracker2': '1',
    '_gid': 'GA1.2.1688166673.1623309979',
    '_vis_opt_test_cookie': '1',
    '_vwo': 'ts~nDwZHKg(MX1)l~1%7C(2sg)k~*(MX1',
    'ls_c': '0',
    'ls_e': '0',
    's_cc': 'true',
    's_fid': '6CA41F06B92A092D-3EB3173EE9A83268',
    's_la': 'Thu%20Jun%2010%202021%2003%3A26%3A43%20GMT-0400%20%28EDT%29',
    's_nr': '1623310003700-Repeat',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|305E54D4EC13F3F7-6000174D8DE84B18[CE]',
    '_gat_UA-172784514-2': '1',
    '_pin_unauth': 'dWlkPU1Ua3daR1kyTVdRdFlqUmlZaTAwTkRWakxUZzBNR1F0TlRRM01HWXdNRFl6WWpkag',
    '_vis_opt_s': '1%7C',
    'ADRUM': 's=1623309976111&r=https%3A%2F%2Fwww.safeway.com%2F%3Fhash%3D35',
    '_ga_LZL2CD3SX2': 'GS1.1.1623309976.3.0.1623309976.0',
    '_br_uid_2': 'uid%3D5647911862151%3Av%3D12.0%3Ats%3D1622976933966%3Ahc%3D6',
    '_gcl_au': '1.1.1278303928.1622976934',
    '_uetsid': '21448dc0c9bd11eb9aef2767bbf0985c',
    '_uetvid': 'b8294fc0c6b511ebaf714328c4c6e811',
    'aam_uuid': '52427603405180283192129302807457674843',
    'AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '-1124106680%7CMCIDTS%7C18789%7CMCMID%7C47847013639026807631668697828973346047%7CMCAAMLH-1623914769%7C7%7CMCAAMB-1623914769%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1623317169s%7CNONE%7CMCSYNCSOP%7C411-18792%7CvVersion%7C5.2.0',
    'SAFEWAY_MODAL_LINK': '',
    '_gat_gtag_UA_172784514_2': '1',
    'gpv_Page': 'safeway%3Aloyalty%3Ahome',
    'mbox': 'PC#8bb1853684fb45a5982024f199d2cbe8.34_0#1686554770|session#539a066079104eff94aa6e90fa14e04d#1623311829',
    's_ivc': 'true',
    's_nr30': '1623309969811-Repeat',
    's_vncm': '1625111999759%26vn%3D4',
    'safeway_ga': 'GA1.2.1397215564.1622976934',
    'safeway_ga_gid': 'GA1.2.465403696.1623309970',
    'SWY_SYND_USER_INFO': '%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D',
    'at_check': 'true',
    'incap_ses_8074_1738022': 'yn+6NCLDA213m1YkXpwMcGLovmAAAAAA7VvYZYNRZEeLyZ5BtSTdUw==',
    'nlbi_1738022': 'dN+nXjwluQ2l5NcxEEDIZQAAAABrb/j0F0DUVaGp6H+yCgTE',
    'incap_ses_1415_1738022': 'ewcQO8j3+i/dShyBhRejE67KvWAAAAAAQ/YpAW3CDwl3hlMojmb+ZA==',
    '_elevaate_session_id': 'ccba63e0-9d74-47fd-bf7c-fa959c2b78c5',
    'B': 'i=1622716804EyggJ6BO3a&r=858&t=1622716804&v=2&s=514f94f977711ec6f5fba4edc6dd8db5eccda0a8',
    '_csrfKey': '%2FRPZy8BmcytOzVDxtnO4FcMIIPA%3D%7C%7CwNViEKkE1D42FVJWyXxRKSiiSurqENwLKN7kNlm41qgrqdR6gtUqXG31btrJsa%2BAhq6cOxdbp%2BkWLST27GmwEA%3D%3D',
    'AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg': '1',
    'incap_ses_701_1738022': 'm+cWeH/DjiI2VgP9OHS6CaSpvGAAAAAAxk4kOpgY3G/Ehpw+NbWYWw==',
    'visid_incap_1738022': '4lpnMNWpQLKN6avRp7HF9KOpvGAAAAAAQUIPAAAAAABXmjyRXLf1u2VHgfd+fu2z',
}

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Host': 'coupons.safeway.com',
    'Origin': 'https://coupons.safeway.com',
    'Content-Length': '43',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Referer': 'https://coupons.safeway.com/weeklyad/?s=recommended/0',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
}

params = (
    ('size', '50'),
    ('startIndex', '0'),
)

#use the store code to change where you are
data = '{"storeCode":"3132","excludeCategories":[]}'

response = requests.post('https://coupons.safeway.com/services/gco', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://coupons.safeway.com/services/gco?size=50&startIndex=0', headers=headers, cookies=cookies, data=data)


print(response.json())

