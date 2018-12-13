import urllib.request,re,requests
#1.获取源代码
def get():#见名思意
    hd = {'user'}
    url = 'http://www.budejie.com/video/'
    html = requests.get(url,headers=hd).text
    #print(heml)

#2.解析视频+名字
    url_content = re.compile(r'(<div class="j-r-list-c:>.*?</div>.*?</div>)',re.S)
    url_content = re.findall(url_content,html)#匹配 list
    #
    for i in url_contentts:#如果视频存在,标题就获取
        url_reg = r'date-mp4="(.*?)"'#地址
        url_items = re.findall(url_reg,i)  #list
        #print(url_items)
        if url_items:#如果视频存在
            name_reg = re.compile(r'<a href=:/detail-{8}?.html">(.*?)</a>',re.S)
            name_items = re,findall(name_reg,i)#标题
            #print(name_items)
            for i,k in zip(name_items,url_items):
                url_name.append([i,k])
                 #print(i,k)
    for i in url_name:
        urllib.request.urlretrieve(i[i],'video\\%s.mp4'%i[0])
a = get()
