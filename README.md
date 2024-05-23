# docker启动浏览器
### docker镜像    selenium/standalone-chrome自带chrome浏览器
### 安装对应版本的chromedriver（找不到打一个版本也可以试试）
#### docker终端克隆项目并解压
```
yunda@users:/www/wwwroot$ wget url路径
...
yunda@users:/www/wwwroot$ git clone https://github.com/content1234/123.git
...
yunda@users:/www/wwwroot$ unzip 压缩包名
```
### docker      ls查看目录进入cd 123目录下

***列***
```c
    yunda@users:/www/wwwroot$ ls
    123            chrome.deb                demo           hj_ppt            TiktokService
    127.0.0.1      chromedriver-linux64      dow.u-sms.top  huanju
    192.168.0.118  chromedriver-linux64.zip  FakeData       logistics
    api            ddns                      frp            m.hangyunda.com
    beifen         default                   hangyunda.com  pc.hangyunda.com
    yunda@users:/www/wwwroot$ cd 123
    yunda@users:/www/wwwroot/123$ ls
    docker_url.py  README.md  url.txt
```

### 把要打开的网页url文本重命名和url.txt一样并替换后执行python3 docker_url.py

***列***
`yunda@users:/www/wwwroot/123$ python3 docker_url.py`


