subject, student = map(int, input().split())
marks = []
for i in range(student):
        marks.append([map(float, input().split())])

print(zip(marks))
for i in zip(*marks):
    print( sum(i)/len(i) )

