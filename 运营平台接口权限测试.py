import time
import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuaWNrIjoiMTUw5p2O6Z2ZIiwiY3VycmVudFR5cGUiOjEsImV4cGlyZSI6MTY3ODM3NzY0NzgxOSwiaXNzIjoiNzM2MTYyNTM5OTA1MjIwNjA4IiwidGVuYW50SWQiOiIxMDAwNDQiLCJpZCI6IjczNjE2MjUzOTkwNTIyMDYwOCIsInVzZXJJZCI6IjczOTEwMDYwMjQ3ODM2MjYzMiJ9.yaIU0QbhNGhMj3AQQvj0Ege4M9cvRfoDxhWN1vEJ8QE'
}

headersuat = {
    'Content-Type': 'application/json',
    'Authorization': ''
}
way1 = "/manager/tenant/detail/pageList"
url1 = "https://cloud.qianliling.com" + way1
res1 = requests.get(url1, headers=headers)
# print(res1.text)

for line in open('way.txt', encoding='utf-8'):
    if line == '\n':
        continue
        # 如果这一行是换行符的话就跳过输出
    else:
        time.sleep(2)
        url = "http://10.10.27.210" + line.strip()
        # url = "" + line.strip()
        # strip函数用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        response = requests.get(url, headers=headers)
        print(response.text, line.strip())



