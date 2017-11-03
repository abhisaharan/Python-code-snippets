def gemstones(arr):
    new_list = []
    for list_string in arr:
        for word in list_string:
            if word in arr[list_string]:
                new_list








n = int(input().strip())
arr = []
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
