# qq-music-list-to-kwl

> 导出qq音乐歌单的小工具，导出格式为.kwl，可以把.kwl导入到网易云、酷我里面去。

##1、使用步骤：

1. 安装`python3`
2. 获取qq音乐歌单列表id
3. 修改`qq-music-list-export.py`中的歌单`id`
4. 在命令行中运行`qq-music-list-export.py`
5. 将生成的文件上传到网易云音乐


### 1.1、安装`python3`
`python`的安装可以[参考官网的教程](https://www.python.org/about/gettingstarted/)，各个平台的方法都有。建议安装3.6版本或者更新的版本。

### 1.2、获取qq音乐歌单列表id
这一步建议在手机上面操作，选择要转移的歌单之后，使用分享功能，选择复制链接，将链接复制出来之后，查看`id`参数

> 这一步有个注意点，导出来的网址可能有两种，如果你的网址是类似：`https://y.qq.com/w/taoge.html?hostuin=498460828&id=2330669376`这样的，那么你的歌单id就是`2330669376`，如果你的网址是类似`https://y.qq.com/n/yqq/playlist/2330669376.html`
，那么你的歌单ID就是后面那串数字

###1.3、设置歌单id参数
用编辑器打开`qq-music-list-export.py`，修改上面的LIST_ID

```python
# 歌单id 需要替换成你自己的
LIST_ID = "2330669376"
```
###1.4、 在命令行中运行`qq-music-list-export.py`

* 由于这个工具依赖了两个第三方工具，需要先安装第三方依赖，在命令行中输入下面命令

```bash
pip3 install BeautifulSoup
pip3 install requests
```

* 安装完成之后,在命令行中，进入工具所在目录，执行下面的命令

```bash
python3 qq-music-list-export.py
```

###1.5、 将生成的文件上传到网易云音乐
* 打开[网易云音乐网页版](http://music.163.com/)，登录自己的帐号
* 在右上角个人信息处，选择导入歌单
* 选择导入酷我播放列表
* 导入完成
