#encoding:UTF-8

import urllib.request
import json


# appstore：调用知乎上的一个人所说的苹果评论查看接口
# 缺陷：一次只能查询500条记录，而且接口返回的json数据没有评论时间
# 解决措施：由于对appstore的了解不够，应而没有好的方案

print("运行完毕后 将生成一个名为“app评论by苹果应用市场.csv”的文件")
page = 1;

appid=1085016815


f = open("app评论by苹果应用市场.csv","w")


while page < 11:  # 默认循环10次

    myurl = "https://itunes.apple.com/rss/customerreviews/page=" + str(page) + "/id=" + str(
        appid) + "/sortby=mostrecent/json?l=en&&cc=cn"

    response = urllib.request.urlopen(myurl)

    myjson = json.loads(response.read().decode())

    print("正在生成数据文件，请稍后......" + str(page * 10) + "%")

    del (myjson["feed"]["entry"][0])

    for i in myjson["feed"]["entry"]:

        temp = i["author"]["name"]["label"]+"\t"+str(i["im:rating"]["label"])+"\t"+i["content"]["label"]+"\n"

        f.writelines(temp)

    page = page + 1

print("生成完毕，请查阅相关文件")

f.close()