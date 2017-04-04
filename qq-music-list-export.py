from bs4 import BeautifulSoup
import requests


def getQQMusicList(url):
    '''
    获取qq音乐歌单列表信息
    :param url: 歌单网址
    :return: 歌单信息list [(歌名, 歌手, 专辑), ...]
    '''
    html = requests.get(url)
    # print(html.text)
    soup = BeautifulSoup(html.text, "html.parser")
    # print(soup.select("ul.songlist__list li", limit=2))
    lists = soup.select("ul.songlist__list li")
    ret = []
    for item in lists:
        ret.append((item.select_one(".songlist__songname_txt a").text, item.select_one(".songlist__artist a").text,
                    item.select_one(".songlist__album a").text))
        # print(item.select_one(".songlist__songname_txt a").text)
        # print(item.select_one(".songlist__artist a").text)
        # print(item.select_one(".songlist__album a").text)
    return ret


def list2kwl(list):
    '''

    :param list:歌单信息,[(歌名, 歌手, 专辑), ...]
    :return:返回kwl格式文本,转换文件需要 gb2312 编码!!!
    '''
    kwl = ''
    for item in list:
        kwl += '    <so name="%s" artist="%s" album="%s"></so>\r\n' % (item[0], item[1], item[2])
    kwl = '<so>\r\n%s</so>' % kwl
    return kwl


# arr是被分割的list，n是每个chunk中含n元素。
def chunks(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]


l = getQQMusicList("https://y.qq.com/n/yqq/playlist/3057195723.html")
partLists = chunks(l, 100)
# k = list2kwl(l)

for i in range(0, len(partLists), 1):
    k = list2kwl(partLists[i])
    with open('{0}.kwl'.format(i), 'w', encoding='gb2312', errors='ignore') as f:
        f.write(k)

print("成功导出", len(l), "首歌曲")
