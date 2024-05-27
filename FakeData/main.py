# _*_ coding : UTF-8 _*_
# @Time : 2024/5/13 上午10:03
# @Auther : TrashMaker
# @File : FakeData
# @Project : FakeData
# @Desc :  假账单推送
import datetime
import time
from sign import sign
import requests
import threading
import random


def get_uerinfo(systemuser):
    """
    :action 获取用户信息
    :param systemuser:
    :param uuid:
    :return: 用户信息(user_info)
    """
    print(systemuser)
    url = "http://192.168.0.139:3000/user/username_tk_list"
    data = {"username": systemuser, "time": int(time.time())}
    data = sign(data=data, key="123456", uuid="uuid", ac=1)  # 请求用户信息
    response = requests.request("POST", url, json=data).json()
    print(response)
    user_info = response["data"]["tkNames"]
    return user_info


def send_msg(user_info, uuid, systemuser):
    """
    :action 对幸运账号随机发送1-3枚精致的钻石
    :param user_info:
    :param uuid:
    :return: response
    """
    url = 'http://192.168.0.139:3000/tk/tk_account_data'
    rand_coin = random.randint(1, 3)
    data = {
        "systemuser": systemuser,
        "account": user_info,
        "boxnumber": 1,
        "diamondnumber": rand_coin,
        "time": int(time.time()),
    }
    data = sign(data=data, key="123456", uuid=uuid, ac=1)
    print(data)
    response = requests.post(url=url, json=data)
    return response.json()


def random_user_send(systemuser, uuid):
    """
    :action 随机挑选幸运用户 进行账单推送
    :param systemuser:
    :param uuid:
    :return: None
    """
    user_list = get_uerinfo(systemuser=systemuser)
    acc_num = random.randint(2, 5)
    for i in range(acc_num):
        user = random.randint(1, len(user_list))
        print(user_list[user - 1])
        res = send_msg(user_info=user_list[user - 1], uuid=uuid, systemuser=systemuser)
        print(res)


def random_coin_send(systemuser, minner, maxer, uuid):
    """
    :action 通过控制账单推送频率控制整体推送数量
    :param systemuser:
    :param minner:
    :param maxer:
    :param uuid:
    :return: None
    """
    print(systemuser)
    rand = random.randint(minner, maxer)
    time.sleep(rand)
    random_user_send(systemuser, uuid=uuid)


if __name__ == '__main__':
    # get_uerinfo(systemuser="kgkj")
    while True:
        try:
            # zm = threading.Thread(target=random_coin_send, args=("zm", 1, 10, "26563e6322ad42489b738ec5d96a68ae"))
            kgkj = threading.Thread(target=random_coin_send, args=("kgkj", 20, 30, "dcb6957ed3d24267806cd14348e4b6f0"))
            # _466636 = threading.Thread(target=random_coin_send,
            #                            args=("466636", 80, 120, "22c7f06dbddb4f359106820925b24be8"))

            # zm.start()
            kgkj.start()
            # _466636.start()
            # _466636.join()
            kgkj.join()
            # zm.join()

        except Exception as e:
            print("发生异常！")
        time.sleep(1)
