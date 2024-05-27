import json
import requests
import time
from sign import sign

def get_uerinfo(systemuser, uuid):
    """
    :action 获取用户信息
    :param systemuser:
    :param uuid:
    :return: 用户信息(user_info)
    """
    print(systemuser)
    url = "https://text.hangyunda.com/api?method=getAccount"
    data = {
        "uuid": uuid,
        "systemuser": systemuser,
        "time": int(time.time() * 1000),
    }
    data = sign(data=data, key="654321", uuid=uuid, ac=1)#请求用户信息
    response = requests.request("POST", url, json=data, verify=False).json()
    print(response)
    with open('uerinfo.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)
    user_info = response["data"]["list"]
    return user_info

if __name__ == '__main__':
    res = get_uerinfo(systemuser="xl",uuid="26563e6322ad42489b738ec5d96a68ae")
    print(res)