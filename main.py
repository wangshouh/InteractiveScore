import requests
import json
import time


def getQuestionsId(uuid, courseId, recruitId) -> list:
    """
    获取前50条问题
    """
    questionid_list = []
    questionUrl = "https://creditqa.zhihuishu.com/creditqa/web/qa/getHotQuestionList"
    headers = {"Host": "creditqa.zhihuishu.com"}
    params = {
        "uuid": uuid,
        "courseId": courseId,
        "pageIndex": "0",
        "pageSize": "50",
        "recruitId": recruitId
    }
    questionData = requests.get(questionUrl, params=params, headers=headers)
    r = json.loads(questionData.text)
    question_list = r["rt"]["questionInfoList"]

    for item in question_list:
        questionid_list.append(item["questionId"])
    return questionid_list


def getAnswer(uuid, courseId, recruitId, questionId) -> str:
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
    answerData = requests.get(answerUrl, params=params, headers=headers)
    r = json.loads(answerData.text)
    answerContent = r["rt"]["answerInfos"][0]["answerContent"]
    return answerContent


def postAnswer(uuid, qid, answer, courseId, recruitId, cookies):
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
        "Cookie": cookies
    }

    returnmsg = requests.post(url, data=data, headers=headers)
    r = json.loads(returnmsg.text)
    msg = r["msg"]
    return msg


def getCookie(cookies):
    dicts = {}
    lis = re.split(';|=', cookies)
    for i in range(0, len(lis)-1, 2):
        dicts[lis[i].strip()] = lis[i+1]
    return dicts


uuid = ""
courseId = ""
recruitId = ""
cookies = ''
id_list = getQuestionsId(uuid, courseId, recruitId)
for questionId in id_list:
    print(questionId)
    answer = getAnswer(uuid, courseId, recruitId, questionId)
    result = postAnswer(uuid, questionId, answer, courseId, recruitId, cookies)
    print(result)
    time.sleep(3)
