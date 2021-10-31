from bs4 import BeautifulSoup
import requests
import time
import json


def get_ticker(s):
    """
    获取lt参数，用于登录
    """

    url = 'https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    lt = soup.find("input", attrs={'name': "lt"}).attrs['value']
    return lt


def do_login(s, username, password, lt):
    """
    登入系统
    """
    url = 'https://passport.zhihuishu.com/login?service=https%3A%2F%2Fcreditqa.zhihuishu.com%2Fcreditqa%2Flogin%2Fgologin%3Ffromurl%3Dhttps%253A%252F%252Fqah5.zhihuishu.com%252Fqa.html%2523%252Fweb%252Fhome%252F1000006835%253Frole%253D2%2526recruitId%253D92281%2526VNK%253D7386e6e4'
    data = {'lt': lt,
            'execution': 'e1s1',
            '_eventId': 'submit',
            'username': username,
            'password': password,
            'clCode': '',
            'clPassword': '',
            'tlCode': '',
            'tlPassword': '',
            'remember': 'on', }
    resp = s.post(url, data=data)
    soup = BeautifulSoup(resp.content.decode('utf8'), 'lxml')


def getuuid(s):
    """
    通过API获取uuid
    """
    url = 'https://onlineservice.zhihuishu.com/login/getLoginUserInfo'
    resp = s.get(url)
    uuid = resp.json()['result']['uuid']
    return uuid


def transcookie(s, lt):
    """
    进行cookie转域
    """
    url = "https://creditqa.zhihuishu.com/creditqa/login/gologin?fromurl=https://qah5.zhihuishu.com/qa.html#/web/home&ticket=" + lt
    resp = s.get(url)


def mainlogin(username, password):
    s = requests.Session()
    lt = get_ticker(s)
    do_login(s, username, password, lt)
    uuid = getuuid(s)
    transcookie(s, lt)
    return s, uuid
