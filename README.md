# InteractiveScore
A python script of zhihuishu interactive score
# 一个基于requests库的python脚本用于智慧树互动答题
需要填写以下内容:
1. uuid
2. coureseId
3. recruitId
4. cookies

获取方法如下：

1.打开互动问答页面，按下F12打开网页控制台，选择 `Network` 选项卡，寻找uuid。如下图：
<img src = 'https://s3.bmp.ovh/imgs/2021/10/91233aee0b39f737.png' />
2. `coureseId` 为互动问答网页 `questionDetail/` 后的第一串字符，`recruitId`也在`url`中。
<img src = 'https://s3.bmp.ovh/imgs/2021/10/0a2fdbbf27d321d7.png' />
3.`cookies`从F12控制台中相关选项卡中获得，如下图:
<img src = 'https://s3.bmp.ovh/imgs/2021/10/213aeb631b4c4231.png' />
注意：`cookies`需要复制全部cookies，并改写成符合Python字典的形式，如下图：
<img src = 'https://s3.bmp.ovh/imgs/2021/10/39adc24855f188a3.png' />

## 免责声明:

**本项目使用者在使用前应了解本项目所带来的风险！**

**本人不对此项目所造成的一切后果担责！**
