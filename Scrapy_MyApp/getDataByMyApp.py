#encoding:UTF-8

import json
import time
import requests
import random


# 可能出现问题：requests.exceptions.ConnectionError：（'Connection aborted。'，error（104，'Connection reset by peer'））
# 连接次数过多导致服务器将你的连接关闭
# 解决措施：1、申请代理（）  2、加上fresh参数缓存（最佳方案）
f = open("app 评论by应用宝.csv","w")

url = 'http://android.myapp.com/myapp/app/comment.htm'

i=1

contextData=""

d = {'apkName': 'com.pingan.paces.ccms', 'apkCode': '420',"p":str(i),"contextData":contextData}

while(1):

    r = requests.post(url, data=d)

    myJsonFirst = json.loads(r.text)

    if(myJsonFirst["success"]):

        break

print("--------------------")

print(i)

details = myJsonFirst["obj"]["commentDetails"]

for detail in details:

    createdTime = detail["createdTime"]

    timeArray = time.localtime(createdTime)

    temp = str(detail["nickName"])+"\t"+str(detail["score"])+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", timeArray)+"\t"+detail["content"]+"\n"

    f.writelines(temp)

    print(temp)

time.sleep(1)

if(myJsonFirst["success"]):

    contextData = myJsonFirst["obj"]["contextData"]

    i += 1

    total = myJsonFirst["obj"]["total"] / 5

    while (1):

        print("--------------------")

        print(i)

        d2 = {'apkName': 'com.pingan.paces.ccms', 'apkCode': '420', "p": str(i), "fresh":str(random.uniform(0,1)),"contextData": contextData}

        r = requests.post(url, data=d2)

        myJson2 = json.loads(r.text)

        if(myJson2["success"]):

            i+=1

            contextData = myJson2["obj"]["contextData"]

            details = myJson2["obj"]["commentDetails"]

            for detail in details:

                createdTime = detail["createdTime"]

                timeArray = time.localtime(createdTime)

                temp = str(detail["nickName"]) + "\t" + str(detail["score"]) + "\t" + time.strftime(
                    "%Y-%m-%d %H:%M:%S", timeArray) + "\t" + detail["content"] + "\n"

                f.writelines(temp)

                print(temp)

            time.sleep(2)

        if(i >= total):

            break

f.close()

