
from edusrc import main0
from edumake import main1
from Search import search
from adeyfuzz import adeyfuzz
from Dirscan import Dirscan
from datetime import datetime
from AdeyScan import ip_main
import threading
import time
import sys
time_now = datetime.now().strftime("%H:%M:%S")

b = fr"""
 _____     _        ______              _    _  _
|  ___|   | |       | ___ \            | |  (_)| |      
| |__   __| | _   _ | |_/ / ___  _ __  | |_  _ | |  ___
|  __| / _` || | | ||    / / _ \| '_ \ | __|| || | / _ \
| |___| (_| || |_| || |\ \|  __/| |_) || |_ | || ||  __/
\____/ \__,_| \__,_|\_| \_|\___|| .__/  \__||_||_| \___|
                                | |
作者：Griy日记   时间：[{time_now}]   
Parameter：
 
   [+] Loophole    # 获取10天edu漏洞
   [+] Developers  # 获取所有开发商
   [+] Search      # 获取大学官网Url
   [+] Adeyfuzz    # 混合模糊测试
   [+] Dirscan     # 路径扫描
   
Usage Method：
 
   [+] EduReptile.py  Loophole    
   [+] EduReptile.py  Developers  
   [+] EduReptile.py  Search 清华大学    
   [+] EduReptile.py  Adeyfuzz url(需要传递参数)
   [+] EduReptile.py  Dirscan  url dict.txt
   
Windows/Linux：

   [Windows]  python EduReptile.py
   [ Linux ]  python3 EduReptile.py
   
"""
f=rf"""
 _____     _        ______              _    _  _
|  ___|   | |       | ___ \            | |  (_)| |      
| |__   __| | _   _ | |_/ / ___  _ __  | |_  _ | |  ___
|  __| / _` || | | ||    / / _ \| '_ \ | __|| || | / _ \
| |___| (_| || |_| || |\ \|  __/| |_) || |_ | || ||  __/
\____/ \__,_| \__,_|\_| \_|\___|| .__/  \__||_||_| \___|
                                | |
作者：Griy日记   时间：[{time_now}]   
"""
try:
    parameter = sys.argv[1]
    if parameter == "Loophole":
        print(f)
        if __name__ == "__main__":
            nm = 1
            for i in range(1, 11):
                print(f"====================Page{nm}====================")
                nm += 1
                wzurl = f"https://src.sjtu.edu.cn/list/?page={i}"
                main0(url=wzurl)
                time.sleep(2)

    elif parameter == "Developers":
        print(f)
        if __name__ == "__main__":
            nm = 1
            for i in range(1, 15):
                print(f"====================Page{nm}====================")
                nm += 1
                wzurl = f"https://src.sjtu.edu.cn/rank/company/?page={i}"
                main1(url=wzurl)
                time.sleep(2)
    elif parameter == "Search":
        print(f)
        name = sys.argv[2]
        if __name__ == "__main__":
            wzurl = f"https://cn.bing.com/search?q={name}"
            search(url=wzurl, eduname=name)
            time.sleep(2)
    elif parameter == "Adeyfuzz":
        print(f)
        url = sys.argv[2]
        if __name__ == "__main__":
            thr0 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr0.start()
            thr1 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr1.start()
            thr2 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr2.start()
            thr3 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr3.start()
            thr4 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr4.start()
            thr5 = threading.Thread(target=adeyfuzz, kwargs={"url": url})
            thr5.start()
    elif parameter == "Dirscan":
        print(f)
        url = sys.argv[2]
        dicto = sys.argv[3]
        if __name__ == "__main__":
            Dirscan(url=url, dicto=dicto)



except:
    print(b)
