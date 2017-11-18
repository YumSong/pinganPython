#encoding:UTF-8

import requests

import json


# 方法：network查看360应用商店的请求接口，get请求可解决
# 缺陷：无

# 根据offset请求url，获取返回的结果
def getDataByUrl(offset,f):

    url = "http://comment.mobilem.360.cn/comment/getComments?callback=jQuery1720589021558608624_1510933286959&baike=%E5%B9%B3%E5%AE%89%E4%BF%A1%E7%94%A8%E5%8D%A1+Android_com.pingan.paces.ccms&c=message&a=getmessage&start="+str(offset)+"&count=50&_=1510933288018"

    myjson = requests.get(url).text

    data = dealStr(myjson)

    writeFile(data["messages"],f)

    return None


# 处理json的text文件
def dealStr(json_text):
    lowStr = "("

    upStr = ")"

    upIndex = json_text.index(upStr)

    lowIndex = json_text.index(lowStr)

    data = json.loads(json_text[lowIndex + 1:upIndex])["data"]

    return data


#对json解析成的dict写入csv文件中
def writeFile(message,f):

    temp = ""

    for user in message:
        temp = user["username"] + "\t" + str(user["score"]) + "\t" + user["create_time"] + "\t" + user[
            "content"].replace("\n", "") + "\n"
        print(temp)
        f.writelines(temp)

    return None

def getTotal():
    return None

# 主函数
def main():

    print("运行完毕后 将生成一个名为“app评论by360应用市场.csv”的文件")

    url = "http://comment.mobilem.360.cn/comment/getComments?callback=jQuery1720589021558608624_1510933286959&baike=%E5%B9%B3%E5%AE%89%E4%BF%A1%E7%94%A8%E5%8D%A1+Android_com.pingan.paces.ccms&c=message&a=getmessage&start="+str(0)+"&count=10&_=1510933288018"

    myjson = requests.get(url).text

    data = dealStr(myjson)

    total = data["total"]

    print(total)

    f = open('app评论by360应用市场.csv', 'w')

    i = 0;

    while i < total/50:

        i = i + 1

        getDataByUrl(i,f)

    f.close()

    return None



main()


