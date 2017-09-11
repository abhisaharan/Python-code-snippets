file_location = "/home/abhisaharan/Desktop/practice.txt"
with open(file_location, "r+") as file_learn:
    print(file_learn.readline())

print(file_learn.closed)