number = int(input().strip())

space = number
# for n in range(number-1):
#     print(" ")
list = []
list_s = []

for n in range(1, number+1):
    list_s.append(n*"#")
pos_s = 0
for n in range(number-1, -1, -1 ):
    length_a = number
    print("{}{}".format(n*" ",list_s[pos_s]))
    pos_s += 1