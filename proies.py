import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
}


def Proxy_ip(url):
    FileProxy = open("Proxy.txt", "w")
    adb = requests.get(url=url, headers=headers).text.encode("UTF-8")
    adblxml = etree.HTML(adb)
    list_ip = adblxml.xpath("//table[1]/tbody[1]/tr[2]/td[1]")
    list_port = adblxml.xpath("//table[1]/tbody[1]/tr[2]/td[2]")
    for i1, i2 in zip(list_ip, list_port):
        proxy = i1.strip() + ":" + i2.strip()
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        try:
            reponse = requests.get(url="http://httpbin.org/", headers=headers, proxies=proxies)
            wzcode = reponse.status_code
            if wzcode == 200:
                print(f"{proxy} == 200")
                FileProxy.write(f"{proxy}\n\n")
        except:
            print(f"\033[31m{proxy} != 200\033[0m")
            continue


if __name__ == "__main__":
    for ie in range(2, 16):
        wzurl = f"http://www.66ip.cn/{ie}.html"
        Proxy_ip(wzurl)
        time.sleep(2)
