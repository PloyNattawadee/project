from web_security import *

# def sendImage():
    # images = show_vid()
#     path = 'C:\\Users\\Nattawadee\\Desktop\\web_security\\image\\img106.jpg'
    # path = 'C:\\Users\\Nattawadee\\Desktop\\web_security\\image\\'
    # files = {'files ': path + image}
    # print(images)
#     files = {'files': path}

#     headers={'Content-Type': 'application/json'}
#     url = 'http://192.168.1.40:5000/image/callapi'
#     # url = 'http://10.255.44.63:5000/image/callapi'
#     response = requests.post(url,json=files,headers=headers)
#     print (response)
#     result = json.dumps(response.json(), indent=2, ensure_ascii=False)
#     value = json.loads(result)
#     data = value['result']
#     datalist = data['results']
#     # vdata = datalist['candidates']
#     for v_lists in datalist:
#         platename = v_lists['plate']
#         print(v_lists['plate'])

#     # callRest(platename)     
#         # print(_vdata)
#         # print (lists['plate'])
#     if result != None:
#         print ("result")
    # sendImage()

# def callRest(platename):
#     # platename = 'วข2273'
#     headers={'Content-Type': 'application/json'}
#     url = 'http://192.168.1.40:5000/check/license'
#     platename = {'platename':platename}
#     response = requests.post(url,json=platename ,headers=headers)
#     _result = json.dumps(response.json(), indent=2, ensure_ascii=False)
#     value = json.loads(_result)
#     print(value)
#     data = value['licenses']
#     # _list = data['results']
#     for dataValue in data:
#         name = dataValue['username']
#         lastname = dataValue['lastname']
#         address = dataValue['address']
#         if data != '' :
#             print(name)
#             print(lastname)
#             print(address)
#         else :
#             print("Not found")

#     if _result != None:
#         print ("result")
#     callRest(platename)