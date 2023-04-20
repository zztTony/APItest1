@设备心跳
Feature: 设备心跳

  Scenario Outline:
    Given 用例编号<caseID>和描述<description>
    When 接口信息: 接口名和请求方法<api>; api账号<api_kv>
    Then 上报设备心跳: 请求参数<parameter>和预期值<expected>

    Examples: 设备心跳的用例
      | caseID  | description           | api                             | api_kv                                                                            | parameter                           | expected                         |
      | 设备心跳001 | 一体机(已注册且激活)上报心跳       | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "0120100016c0aa02a00"} | {"code": 200, "msg": "设备心跳上报成功"} |
      | 设备心跳002 | 门禁盒子(已注册且激活)上报心跳      | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "FE990A0F"}            | {"code": 200, "msg": "设备心跳上报成功"} |
      | 设备心跳003 | 一体机(已注册未激活)上报心跳       | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "0120100016c0aa03a00"} | {"code": 400, "msg": "设备未激活"}    |
      | 设备心跳004 | 门禁盒子(已注册未激活)上报心跳      | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "FE990A9F"}            | {"code": 400, "msg": "设备未激活"}    |
      | 设备心跳005 | 一体机(未注册)上报心跳          | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "0120100016c0aa99b00"} | {"code": 400, "msg": "设备ID不存在"}  |
      | 设备心跳006 | 门禁盒子(未注册)上报心跳         | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"} | {"deviceId": "FE990A8F"}            | {"code": 400, "msg": "设备ID不存在"}  |
      | 设备心跳007 | 一体机(同空间异api账号)上报心跳    | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "98h35f4e50xoe6m4", "api_secret": "k30oyz58fb7j0sfx4iaqa8n0s3vmiivj"} | {"deviceId": "0120100016c0aa02a00"} | {"code": 200, "msg": "设备心跳上报成功"} |
      | 设备心跳008 | 门禁盒子(同空间异api账号)上报心跳   | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "98h35f4e50xoe6m4", "api_secret": "k30oyz58fb7j0sfx4iaqa8n0s3vmiivj"} | {"deviceId": "FE990A0F"}            | {"code": 200, "msg": "设备心跳上报成功"} |
      | 设备心跳009 | 一体机(同租户异空间api账号)上报心跳  | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "150qw761lcolwssc", "api_secret": "b9vrjzvg1dorejp1d4rw1ad7rr3mknx8"} | {"deviceId": "0120100016c0aa02a00"} | {"code": 400, "msg": "设备ID不存在"}  |
      | 设备心跳010 | 门禁盒子(同租户异空间api账号)上报心跳 | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "150qw761lcolwssc", "api_secret": "b9vrjzvg1dorejp1d4rw1ad7rr3mknx8"} | {"deviceId": "FE990A0F"}            | {"code": 400, "msg": "设备ID不存在"}  |
      | 设备心跳011 | 一体机(异租户api账号)上报心跳     | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "uafpktjevv9pebcl", "api_secret": "nvs1gb3lct3fxy4ji4xzarxs7zt3nwxc"} | {"deviceId": "0120100016c0aa02a00"} | {"code": 400, "msg": "设备ID不存在"}  |
      | 设备心跳012 | 门禁盒子(异租户api账号)上报心跳    | {"接口名": "设备心跳", "请求方法": "POST"} | {"api_key": "uafpktjevv9pebcl", "api_secret": "nvs1gb3lct3fxy4ji4xzarxs7zt3nwxc"} | {"deviceId": "FE990A0F"}            | {"code": 400, "msg": "设备ID不存在"}  |