# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd1
# FileName:     sending
# Author:      张正桃Anthony
# Datetime:    11/29/2021 9:58 AM
# Description：封装的请求的方法
# -------------------------------------------------------------------------------------------------
import requests


class ReadyRequesting:
    """
    使用的session回话方法管理对象，支持cookie和session的自动取存；
    如果是token，则需要自己提取
    """

    def __init__(self):
        self.send = requests.Session()

    def requesting(self, link, request_method, request_head, parameters, content_type="application/json"):
        """
        只区分了请求方法，未讲究请求类型query, body！
        """
        if request_method.upper() in "GET":
            return self.send.get(url=link, params=parameters, headers=request_head)
        elif request_method.upper() in "POST":
            if content_type in "application/json":
                return self.send.post(url=link, json=parameters, headers=request_head)
            return self.send.post(url=link, data=parameters, headers=request_head)
        elif request_method.upper() in "PUT":
            if content_type in "application/json":
                return self.send.put(url=link, json=parameters, headers=request_head)
            return self.send.put(url=link, data=parameters, headers=request_head)
        elif request_method.upper() in "DELETE":
            if content_type in "application/json":
                return self.send.delete(url=link, json=parameters, headers=request_head)
            return self.send.delete(url=link, data=parameters, headers=request_head)
        else:
            print(">>>只支持GET, POST, DELETE, PUT这4种请求方法<<<")


if __name__ == "__main__":
    sq = ReadyRequesting()
    hea = {"api_key": "axxxxxx0", "api_secret": "efxxxxxmzaj",
           "Content-Type": "application/json"}
    p = {"deviceId": "0120100016c0aa02a00"}
    a = sq.requesting(r"http://172.xxx.xxx.xx:10001/aiot-device/v1/mac/api/kas/device-heartbeat", "post", hea, p)
    print(a.text)
    print(type(a.text))
    print(a.headers)
    print(a.json())
    print(type(a.json()))
