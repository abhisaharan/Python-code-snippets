def median(numbers):
    new=sorted(numbers)
    l=len(numbers)
    if l%2==0:
        median=(new[int(l/2)]+new[int((l-2)/2)])/2
    else:
        median=new[int((l-1)/2)]
    return median
print(median([4,5,5,4]))