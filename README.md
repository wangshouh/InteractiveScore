# InteractiveScore
A python script of zhihuishu interactive score
# 一个基于requests库的python脚本用于智慧树互动答题

### 使用方法
1. 执行`pip install -r requirements`安装相关依赖
2. 请按终端指示输入账号、密码

### 注意
- 此脚本存储使用了json文件，如需更改请自行改造
- 脚本运行后不会自行删除json中的相应记录，如果程序运行中断，请自行删除对应json中的字段记录
- lxml安装需要C语言编译器，如不具备相关软件，请使用whl下载
- 请务必浏览本项目的源代码

### lxml安装教程
1. 前往`https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml`下载对应的`.whl`文件，说明cp37对应python 3.7, AMD64 对应64位系统
2. `pip install wheel`
3. 使用`pip install .whl文件地址` 安装lxml

## 免责声明:

**本项目使用者在使用前应了解本项目所带来的风险！**

**本人不对此项目所造成的一切后果担责！**
