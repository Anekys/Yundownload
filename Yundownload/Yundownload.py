import requests
from bs4 import BeautifulSoup
import os
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8",
}
def getDownloadurl():
    list=[]
    url=input("请输入百度云分享链接:")
    res = requests.get("http://pan.naifei.cc/?" + url, headers=header)
    soup=BeautifulSoup(res.text,"html.parser")
    for tr in soup.find_all('tr'):
        for i,td in enumerate(tr.find_all('td')):
            if(i!=2):
                list.append(td.text)
            else:
                list.append(td.find("a").get('href'))
    return list
def Downloadfile(fileurl,filename):
    fileurl=fileurl.replace('&','"&"')
    UA=' --user-agent=netdisk;4.4.0.6;PC;PC-Windows;6.2.9200;WindowsBaiduYunGuanJia'
    cmd=path+'\\tools\\aria2c.exe -c -o'+filename+UA+' -x 16 -s 32 -j 32'+' -d'+path+'/Downloads '+fileurl
    os.system(cmd)
if __name__ == "__main__":
    print("受限于P2P下载的原因,部分冷门资源可能依然出现下载速度不佳的问题")
    path=os.getcwd()
    try:
        list=getDownloadurl()
        for i,item in enumerate(list):
            if i%3==0 :
                print(f"文件名:{item}",end="\t")
            elif i%3 == 1 :
                print(f"文件大小:{item}")
            elif i%3 ==2 :
                Downloadfile(item,list[i-2])
    except Exception as error:
        print(error)