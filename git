import  requests
from urllib.parse import urlencode
import pprint
def picture(b):
    x=0
    PAGE=int(input("页数："))
    for page in range(PAGE):
        base_url="https://www.toutiao.com/search_content/?"
        params={
                "offset":0*page,
                "format":"json",
                "keyword":b,
                "autoload":"True",
                "count":20,
                "cur_tab":3,
                "from":"gallery"
        }
        #print(base_url+urlencode(params))
        reponse=requests.get(base_url+urlencode(params))
        #pprint.pprint(reponse.json())
        reponse_jion=reponse.json()
        data=reponse_jion.get("data")
        for i in data:
            pprint.pprint(i.get("title"))
            image=i.get("image_list")
            for tupian in image:
                #print(tupian["url"])
                (u1,u2,u3,u4,u5)=tupian["url"].split('/',4)
                li="http://p99.pstatp.com/origin/"+u5
                li_url = requests.get(li)
                li_url.encoding = 'utf-8'
                li_html = li_url.content
                x += 1
                with open(i.get("title") +str(x)+ '.jpg', 'wb') as f:  # 保存图片
                    f.write(li_html)
                    print("正在下载")
a=input("请输入关键字：")
picture(a)
