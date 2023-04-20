@设备日志
Feature: 设备上报运行日志

  Scenario Outline:
    Given 测试用例编号<caseID>和用例描述<description>
    Then 请求参数<parameter>和预期结果<expected>

    Examples: 用例
      | caseID  | description | parameter                                                                                                                                                                   | expected                           |
      | 设备日志001 | 一体机上报日志     | {"deviceId": "0120100016c0aa02a00", "time": "%Y-%m-%d %H:%M:%S", "log": {"type": "warn", "error": "fjhkvfjkfjk旧卡不具备jkjhsdhfvkjvfvf fvfen   fjhkfejkhwfbjkkj kvnvs,j那就看到你"}} | {"code": 200, "msg": "设备运行日志上报成功"} |
      | 设备日志002 | 门禁盒子上报日志    | {"deviceId": "FE990A0F", "time": "%Y-%m-%d %H:%M:%S", "log": {"type": "warn", "error": "fjhkvfjkfjk旧卡不具备jkjhsdhfvkjvfvf fvfen   fjhkfejkhwfbjkkj kvnvs,j那就看到你"}}            | {"code": 200, "msg": "设备运行日志上报成功"} |
      | 设备日志003 | 上报格式错误的日志   | {"deviceId": "FE990A0F", "time": "%Y-%m-%d %H:%M:%S", "log": {"typ": "warn", "error": "fjhkvfjkfjk旧卡不具备jkjhsdhfvkjvfvf fvfen   fjhkfejkhwfbjkkj kvnvs,j那就看到你"}}             | {"code": 400, "msg": "日志格式错误"}     |
      | 设备日志004 | 上报空日志       | {"deviceId": "0120100016c0aa02a00", "time": "%Y-%m-%d %H:%M:%S", "log": {}}                                                                                                 | {"code": 400, "msg": "日志对象不能为空"} |
      | 设备日志005 | 未注册设备上报日志   | {"deviceId": "0120100016c0aa02f00", "time": "%Y-%m-%d %H:%M:%S", "log": {"type": "warn", "error": "fjhkvfjkfjjkjhsdhfvkjvfvf fvfen   fjhkfejkhwfbjkkj kvnvs,j"}}            | {"code": 400, "msg": "设备ID不存在"}    |
      | 设备日志006 | 用错误时间格式上报日志 | {"deviceId": "0120100016c0aa02f00", "time": "%Y-%m%d %H:%M:%S", "log": {"type": "warn", "error": "fjhkvfjkfjjkjhsdhfvkjvfvf fvfen   fjhkfejkhwfbjkkj kvnvs,j"}}             | {"code": 400, "msg": "操作时间格式不正确"}     |
