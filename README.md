# 📘EduReptile项目📘
En：EduReptile was developed for: Because the time that digs edu flaw has the website that goes to edusrc tomorrow to see the school that has flaw today. (Looking for target)
<br>Ch：开发EduReptile原因：因为挖掘edu漏洞的时候明天都有去edusrc的网站去看今日有漏洞的学校.（寻找目标）


# Use of EduReptile：
📄安装lxml和requests：
> pip install requests

> pip install lxml
<br>

📄【1】：Loophole
获取edusrc 10天的漏洞
（Get edusrc 10-day vulnerability ）
<br>
> python EduReptile.py Loophole
<br>


📄【2】：Developers
获取网站开发商
（Get a Website Developer ）
> python EduReptile.py Developers
<br>


📄【3】：Search 获取大学网站
（Get the University Website ）
> python EduReptile.py Search 清华大学
<br>

📄【4】：Adeyfuzz 模糊测试
（fuzzy test ）
> EduReptile.py  Adeyfuzz 'http:www.xxx.edu.cn?id='
<br>


📄【5】：Dirscan 路径扫描
（path scanning ）
> EduReptile.py  Dirscan url dict.txt  

(url例子:https://www.xx.edu.cn 注意域名后面不要带'/',dict.txt为字典文件)


# 💻Author💻：
公众号：Griy日记
<br>作者：Griy
