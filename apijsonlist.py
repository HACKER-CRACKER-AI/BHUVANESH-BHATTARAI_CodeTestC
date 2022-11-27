import json
array = '{"Color": ["Red", "Blue", "Green", "Yellow", "Orange", "Purple","Brown","Black","White","Lime","Cyan","Grey","Pink","Crimson"]}'
data  = json.loads(array)
listofdata = data['Color']
if len(listofdata)<=13:
    print(listofdata)
else:
    for i in range(13):
        print(listofdata[i])
