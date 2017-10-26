import sys

def timeConversion(s):
    split_st = s.split(sep=":")
    split_3rd = split_st[2]
    new_date = []
    if "PM" in split_3rd:
        if split_st[0] == "12":
            new_date.append(split_st[0])
            new_date.append(split_st[1])
            new_date.append(split_3rd[:2])
        else:
            new_date.append(str(int(split_st[0]) + 12))
            new_date.append(split_st[1])
            new_date.append(split_3rd[:2])

    elif "AM" in split_3rd:
        if split_st[0] == "12":
            new_date.append("00")
            new_date.append(split_st[1])
            new_date.append(split_3rd[:2])
        else:
            new_date.append(split_st[0])
            new_date.append(split_st[1])
            new_date.append(split_3rd[:2])

    return  ":".join(new_date)



s = input().strip()
result = timeConversion(s)
print(result)
