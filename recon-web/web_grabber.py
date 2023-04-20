#https://www.proxyscrape.com/free-proxy-list

import requests, random, hashlib

http_proxies = ["120.234.135.251:9002", "218.57.210.186:9002", "103.190.232.186:80", "200.52.148.10:999"]
user_agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            ]

def rand_proxy():
    i = random.randrange(0, len(http_proxies))
    return http_proxies[i]

def rand_useragent():
    i = random.randrange(0, len(user_agents))
    return user_agents[i]

def grab(url):
    proxies = {"http": rand_proxy()}
    headers = {"user-agent": rand_useragent()}
    print(f"Connecting to {url} with proxy {proxies['http']} and user-agent {headers['user-agent']}")
    r = requests.get(url, proxies=proxies, headers=headers)
    return r.headers, r.text, r.cookies

def main():
    url = "http://testing-ground.scraping.pro/whomai"
    h, t, c = grab(url)
    print("====================================")
    print(h)
    print("====================================")
    print(t)
    print("====================================")
    for cookie in c:
        print(cookie)
    with open(url[7:].replace("/","_")+".html","w") as f:
        f.write(t)
    with open(url[7:].replace("/","_")+".txt","w") as f:
        for header in h:
            f.write(f"{header}: {h[header]}\n")
        f.write("====================================\n")
        for cookie in c:
            f.write(f"{cookie.name}: {cookie.value}\n")

if __name__ == "__main__":
    main()