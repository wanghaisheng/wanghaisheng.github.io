1.在根目录新增文件.gitmodules 再次提交源码到master ,hexo d部署到gh-pages 显示部署成功
```
[submodule " themes/jacman"]
      path = themes/jacman
      url = https://github.com/wanghaisheng/jacman.git
```
2.安装git nodejs hexo
3.安装theme
git clone https://github.com/wanghaisheng/jacman.git  themes/jacman
4.本地测试
hexo g
hexo s
就可以在浏览器上键入localhost:4000
5 发布到远程分支 
hexo d