class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()

with OpenFile("sample.txt", 'w') as r:
    r.write("testing")

print(r.closed)