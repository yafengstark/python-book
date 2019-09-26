
- 查看版本

- 查看是否安装了包
$ pip show --files [安装包名]
 Name:SomePackage    # 包名
 Version:1.0         # 版本号
 Location:/my/env/lib/pythonx.x/site-packages   # 安装位置
 Files:              # 包含文件等等
  ../somepackage/__init__.py
  [...]
  
  
pip检查哪些包需要更新
$ pip list --outdated
1
pip升级包
$ pip install --upgrade [要升级的包名]
1
pip卸载包
$ pip uninstall [要卸载的包名]
