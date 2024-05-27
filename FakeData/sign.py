# _*_ coding : UTF-8 _*_
# @Time : 2024/5/13 上午10:03
# @Auther : TrashMaker
# @File : FakeData
# @Project : sign校验/加密
# @Desc :  sign校验/加密
import hashlib
from urllib.parse import urlencode


def sign(data, key, ac, uuid=""):
    """
    :action 加密/校验 sign
    :param data:
    :param key:
    :param ac:
    :param uuid:
    :return: ac==0:Ture/False, ac==1:data
    """
    try:
        signer = data["sign"]
        del data["sign"]
    except:
        signer = ""
    try:
        del data["uuid"]
    except:
        pass
    sigh_str = ""
    for k in sorted(data.keys()):
        sigh_str = sigh_str + str(k) + "=" + str(data[k]) + "&"
    sigh_str = sigh_str + "key=" + key
    res = hashlib.md5(sigh_str.encode(encoding='utf-8')).hexdigest()

    if ac == 0:  # 校验
        if signer == res:
            return True
        else:
            return False
    elif ac == 1:  # 加密
        data["sign"] = res
        data["uuid"] = uuid
        # data["time"] = int(time.time())
        return data


if __name__ == "__main__":
    data = {
        "acc": "denisnorman837@gmail.com",
        "code": 3,
        "msg": "error",
        "sign": "1e11d67e0e1e26225cdc29767c6a8449",
        "time": 1715935086,
        "uuid": ""
    }
    print(sign(data, key="123456", ac=1))  # 测试加密
