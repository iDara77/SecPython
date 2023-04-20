#https://www.proxyscrape.com/free-proxy-list

import requests

proxies = {"http":"120.234.135.251:9002"}
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

r = requests.get("http://testing-ground.scraping.pro/whomai", proxies=proxies, headers=headers)

print(r.text)
for cookie in r.cookies:
    print(cookie)
