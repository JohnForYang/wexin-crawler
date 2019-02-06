# 微信公众号爬虫
## step0 环境准备
- 安装mitmproxy并在手机上安装相应证书
- Anaconda3环境
- python -m pydoc -p 1234 查看API
- CHCP 65001将cmd控制台输出修改为utf-8
## step1 获取当前公众号信息
- 启动mitmweb(mitmdump -s mitm-demo.py)，点击微信全部消息，开始抓包
- GET https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIxNDMyNDAzOQ==&scene=126&bizpsid=1549345807&sessionid=1549345807&subscene=0&devicetype=iOS10.3.3&version=17000324&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=7l7Iaez4wxykKqGhfLNKa3oElnh2OSxgHa0nzIlPsg%2BJ1ByRR9L2Q9f7Cf2NrDi%2B&wx_header=1 HTTP/1.1 
用html格式请求返回了公众号的基本信息，其中\<img src="http://wx.qlogo.cn/mmhead/Q3auHgzwzM4jY0Sc459r0aYjhRxINQLoXrqccwuGJtNoDjpVqbdaBA/0" id="icon"\>为公众号图标
\<strong class="profile_nickname" id="nickname"\>
            四川高校脱单        \</strong\>为公众号名字
- BeautifulSoup解析出来名字和图标，并直接用requests包通过url发送Get获取图标
## step2获取全部历史消息
- 只需要修改有一个请求的页码就能获取全部历史消息概览，返回内容是json，包含了消息的标题和url
- 因此需要用requests包来不断发起请求获取全部消息概览（只需要修改页码，报文都是一样的）
## step3获取每篇文章
- 具体点击某文章可以获取内容+点赞数阅读量，返回内容是json
