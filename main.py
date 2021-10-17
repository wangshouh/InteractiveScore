import requests
import json
import time
import re


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


uuid = "VBxD6Jnb"
courseId = "1000006835"
recruitId = "92281"
cookies = 'JSESSIONID=7051BC67A85AAAA5CA902DC6D4432CC0; Z_LOCALE=2; exitRecod_VBxD6Jnb=2; privateCloudSchoolInfo_804537949=",1,,https://image.zhihuishu.com/testzhs/ablecommons/demo/201605/98d2d89f44d3411db7490f359090314f.jpg,,316,//school.zhihuishu.com/sdufe,"; CASTGC=TGT-5604848-EbuFengiLxiJFIoyDM6Ge9zQJuDpRX6yWf3yaT2BbtDHx3S71Q-passport.zhihuishu.com; CASLOGC=%7B%22realName%22%3A%22%E7%8E%8B%E9%A6%96%E8%B1%AA%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A804537949%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2F4b2d425390924f39948e3370ceca7984_s3.jpg%22%2C%22uuid%22%3A%22VBxD6Jnb%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%22676a0959278f4634be6a1855f4752eaf%22%7D; staus=1; o_session_id=978C5BC665472A554FEA1382FC4BB704; INGRESSCOOKIE=1634514255.8.179328.186762'
id_list = getQuestionsId(uuid, courseId, recruitId)
for questionId in id_list:
    print(questionId)
    answer = getAnswer(uuid, courseId, recruitId, questionId)
    result = postAnswer(uuid, questionId, answer, courseId, recruitId, cookies)
    print(result)
    time.sleep(3)
