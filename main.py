import requests
import json
import time
from bs4 import BeautifulSoup
import login
from basicinfo import getstudentinfo, getsharecourse, selectCourse


def getQuestionsId(uuid, courseId, recruitId, s, numberOfQuestions) -> list:
    """
    获取前50条问题
    """
    questionid_list = []
    questionUrl = "https://creditqa.zhihuishu.com/creditqa/web/qa/getHotQuestionList"
    headers = {"Host": "creditqa.zhihuishu.com"}
    params = {
        "uuid": uuid,
        "courseId": courseId,
        "pageIndex": "0",  # 开始题目的索引
        "pageSize": numberOfQuestions,  # 题目总数
        "recruitId": recruitId
    }
    questionData = s.get(questionUrl, params=params, headers=headers)
    r = json.loads(questionData.text)
    question_list = r["rt"]["questionInfoList"]

    for item in question_list:
        questionid_list.append(item["questionId"])
    return questionid_list


def getAnswer(uuid, courseId, recruitId, questionId, s) -> str:
    """
    获取最近一条答案
    """
    answerUrl = "https://creditqa.zhihuishu.com/creditqa/web/qa/getAnswerInInfoOrderByTime"
    headers = {"Host": "creditqa.zhihuishu.com"}
    params = {
        "uuid": uuid,
        "questionId": questionId,
        "courseId": courseId,
        "recruitId": recruitId,
        "sourceType": "2",
        "pageIndex": "0",
        "pageSize": "1"
    }
    answerData = s.get(answerUrl, params=params, headers=headers)
    r = json.loads(answerData.text)
    answerContent = r["rt"]["answerInfos"][0]["answerContent"]
    return answerContent


def postAnswer(uuid, qid, answer, courseId, recruitId, s):
    '''
    发送答案
    '''
    url = "https://creditqa.zhihuishu.com/creditqa/web/qa/saveAnswer"
    data = {
        "uuid": uuid,
        "qid": qid,
        "annexs": "[]",
        "source": "2",
        "aContent": answer,
        "courseId": courseId,
        "recruitId": recruitId
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "creditqa.zhihuishu.com",
        "Content-Length": "140",
    }

    returnmsg = s.post(url, data=data, headers=headers)
    r = json.loads(returnmsg.text)
    msg = r["msg"]
    return msg


getstudentinfo()
with open('student.json', 'r') as f:
    student = json.load(f)
username = student['username']
password = student['password']
s, uuid = login.mainlogin(username, password)
getsharecourse(s, uuid)

courseinfo = selectCourse()
numberOfQuestions = eval(input('请输入刷题个数：'))

courseId = courseinfo['courseId']
recruitId = courseinfo['recruitId']
coursename = courseinfo['courseName']
try:
    id_list = getQuestionsId(uuid, courseId, recruitId, s, numberOfQuestions)
except:
    print("出现问题，请打开main.py，调整getAnswer函数中的params参数")
print('正在进行{}的回答'.format(coursename))
for questionId in id_list:
    answer = getAnswer(uuid, courseId, recruitId, questionId, s)
    result = postAnswer(uuid, questionId, answer, courseId, recruitId, s)
    print('{:<15}{}'.format(questionId, result))
    time.sleep(3)
