#encoding:UTF-8

import json
import time
import requests

# 前期准备
# 1、pip3 install selenium
# 2、apt purge phantomjs
# 3、wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
# 4、tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
# 5、sudo cp ～/phantom/bin/phantomjs /usr/bin/
from selenium import webdriver

f = open("app评论by华为应用市场.csv","w")

url = 'http://app.hicloud.com/app/C10465259'

driver = webdriver.PhantomJS()

driver.get(url)   #加载网页

data = driver.page_source   #获取网页文本

# driver.save_screenshot('1.png')   #截图保存

pageIndexSize = len(driver.find_element_by_id("commentListPage").find_elements_by_tag_name("a"))


# total_str = driver.find_element_by_id("commentListPage").find_elements_by_tag_name("a")[0].get_attribute("href")
#
# print(total_str==None)


while(1):

    for element in driver.find_elements_by_class_name('comment'):
        score_str = element.find_element_by_class_name('sub').find_elements_by_tag_name("span")[0].get_attribute(
            "class")

        flag_str = '_'

        n2 = score_str.index(flag_str)

        user = element.find_element_by_class_name('sub').find_elements_by_tag_name("span")[1].text

        score = score_str[n2 + 1:n2 + 2]

        createTime = element.find_element_by_class_name('sub').find_element_by_class_name("frt").text

        content = element.find_element_by_class_name('content').text

        print(user)
        print(score)
        print(createTime)
        print(content)
        print("-------------")

        temp = user + "\t" + score + "\t" + createTime + "\t" + content + "\n"

        f.writelines(temp)

    pageIndexSize = len(driver.find_element_by_id("commentListPage").find_elements_by_tag_name("a"))

    next_page = driver.find_element_by_id("commentListPage").find_elements_by_tag_name("a")[pageIndexSize - 2]

    total_str = driver.find_element_by_id("commentListPage").find_elements_by_tag_name("a")[pageIndexSize-1].get_attribute("href")

    next_page.click()

    if(total_str==None):break

    time.sleep(2)



driver.quit()

f.close()

