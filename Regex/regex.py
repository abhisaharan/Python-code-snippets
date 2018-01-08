import re

data = "010.123.121 hello hii how are you. 21.33.11.003 man int he armour sunday monday, " \
       "tuesday 111.00.1.11.11 abhi.sah/a123/ran@gmail.com jyoti.saharan@gmail.com"

p1 = r'[a-zA-Z0-9./]*@[a-zA-Z0-9]*\.com'
p2 = r'hello'
result = re.findall(p1, data)

dict = {}

for i in range(len(result)):
    dict[i] = result[i]
print(dict)