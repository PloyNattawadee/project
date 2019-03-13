# from gui import *

# def test():
#     url = "http://192.168.1.40:5000/select/report"
#     response = requests.get(url, data=data)
#     print(response=response)
def callRest():
    headers={'Content-Type': 'application/json'}
    url = 'http://192.168.1.40:5000/select/report'
    response = requests.get(url,headers=headers)
    result = json.dumps(response.json(), indent=2, ensure_ascii=False)
    value = json.loads(result)

    if result != None:
        print (result)