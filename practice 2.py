def capitalize(string):
    a = string.split(" ")
    new_list = []
    for w in a:
        if len(w) == 1:
            a = new_list.append(w[0])
        else:
            a = new_list.append(w[0].capitalize()+w[1:])
    return (" ".join(new_list))


