import requests
import json
import openpyxl as op

wb = op.Workbook()
ws = wb['Sheet']

url = "http://10.10.27.210/manager/order/queryOrderList"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'xxxx每次登录不一样'
}
data = {
    "queryType": 2,  # 0:我的;1:我团队的;2:全部
    "tenantId": "",  # 客户ID
    "isMakeInvoice": -1,  # 发票状态(-1:全部;0:未开票;1:开票中;2:已开票)
    "isMakeContract": -1,  # 合同状态(-1:全部;0:未开具;1:开具中;2:已开具)
    "startTime": "",
    "endTime": "",
    "orderNo": "",  # 订单编号
    "status": -1,  # 订单状态(-1:全部;0:未支付;1:已支付;2:已取消;3:已退款;5:凭证待审核)
    "managerId": "",
    "isAssigned": -1,  # 分配状态(-1:全部;0:未分配;1:已分配)
    "currentPage": 1,
    "pageSize": 10
}
response = requests.post(url, json=data, headers=headers)  # 接口返回值
r = json.dumps(response.json(), indent=2, ensure_ascii=False)  # 将返回值转为json格式
# print(r)
r_py = json.loads(r)  # 将json对象转换为python对象,python字典

# 循环输出第0-data['pageSize']条订单的客户名称（buyerName）、订单来源（orderSource）……
for num in range(0, data['pageSize']):
    r_buyerName = r_py['data']['dataList'][num]['buyerName']
    r_orderSource = r_py['data']['dataList'][num]['orderSource']
    r_orderType = r_py['data']['dataList'][num]['orderType']
    r_orderStatus = r_py['data']['dataList'][num]['orderStatus']
    r_thirdInfo = r_py['data']['dataList'][num]['thirdInfo']['info'][0]['label']
    print(r_buyerName, r_orderSource, r_orderType, r_orderStatus, r_thirdInfo)

# print(r)
# print(r_py)
