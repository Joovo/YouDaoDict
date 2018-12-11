import requests
from  lxml import etree

def parse(html):
    # class='ol'的 div的xpath
    details_xpath='//*[@id="collinsResult"]/div/div/div/div/ul' 
    tree=etree.HTML(html)
    #print(dir(tree.xpath(details_xpath)[0]))
    # print(tree.xpath(details_xpath)[0].text)
    # //*[@id="collinsResult"]/div/div/div/div/ul/li[1]
    # 遍历下方的li节点
    for li in range(1,len(tree.xpath(details_xpath)[0])+1):
        print(str(li)+'.')
        # 构造li节点的xpath
        li_xpath='//*[@id="collinsResult"]/div/div/div/div/ul/li['+str(li)+']'
        # 获取所有的test，直接用 strip() 方法
        all=tree.xpath(li_xpath+'/div[1]/p//text()')
        string=''
        all=[i.strip('\t') for i in all]
        for i in range(1,len(all)):
            string+=all[i]
            if i ==1:
                string+='.\n'
        print(string)
        # 与上同理
        example_xpath=li_xpath+'/div[2]/div//text()'
        example_all=tree.xpath(example_xpath)
        print('例:')
        example_str=''
        example_all=[i.strip('\t') for i in example_all]
        for i in range(1,len(example_all)):
            example_str+=example_all[i]
            if i ==1:
                example_str+=' '
        print(example_str)
        # 保存文件 追加写入
        file=open('save.txt','a+',encoding='utf-8')
        file.write(str(li)+'.\n')
        file.write(string+'\n')
        file.write('例:\n')
        file.write(example_str+'\n')


def crawl(url):
    header = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'cookie': "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1768574849@220.181.76.83; webDict_HdAD=%7B%22req%22%3A%22http%3A//dict.youdao.com%22%2C%22width%22%3A960%2C%22height%22%3A240%2C%22showtime%22%3A5000%2C%22fadetime%22%3A500%2C%22notShowInterval%22%3A3%2C%22notShowInDays%22%3Afalse%2C%22lastShowDate%22%3A%22Mon%20Nov%2008%202010%22%7D; ___rl__test__cookies=1544516405027; JSESSIONID=abc3R7KYsXhP_9_VAwCEw; _ntes_nnid=a59fbbb6d3092682996becd378092a3d,1544516385701; OUTFOX_SEARCH_USER_ID_NCOO=928410427.493158; OUTFOX_SEARCH_USER_ID=\"486593599@10.169.0.83\"",
        'host': "youdao.com",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    }
    response = requests.request('GET', headers=header,url=url)
    response.encoding = response.apparent_encoding
    return response.text

if __name__ == '__main__':
    word = 'scene'
    # http://youdao.com/w/eng/scene/
    url = 'http://youdao.com/w/eng/' + word + '/' # 构造url
    html=crawl(url) # 返回网页源代码
    parse(html) # 解析网页 并保存

