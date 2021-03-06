import os.path
import json
import time


def getstudentinfo():
    """
    获取账号、密码并储存
    """
    if not os.path.exists('student.json'):
        username = input('请输入您的账号名：')
        password = input('请输入您的密码：')
        studentinfo = {'username': username, 'password': password}
        with open('student.json', 'w') as f:
            json.dump(studentinfo, f)


def getservertime():
    """
    获取服务器时间
    """
    tsp = time.time() - 28800
    timeArray = time.localtime(tsp)
    date = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", timeArray)
    return date


def getsharecourse(s, uuid):
    """
    获取课程列表并储存
    """
    url = 'https://onlineservice.zhihuishu.com/student/course/share/queryShareCourseInfo'
    data = {'status': '0',
            'pageNo': '1',
            'pageSize': '10',
            'uuid': uuid,
            'date': getservertime()
            }
    resp = s.post(url, data=data)
    sharecourseinfo = resp.json()['result']['courseOpenDtos']
    if not os.path.exists('courseinfo.json'):
        with open('courseinfo.json', 'w') as f:
            json.dump(sharecourseinfo, f)


def selectCourse():
    n = 0
    with open('courseinfo.json', 'r') as f:
        courseinfos = json.load(f)
    print("{:^5}{:^20}".format('序号', '课程名'))
    for item in courseinfos:
        print("{:^5}{:^20}".format(n, item['courseName']))
        n += 1
    selectCourseId = eval(input('请输入您选择的课程序号(一次仅可选择一个科目): '))
    return courseinfos[selectCourseId]
