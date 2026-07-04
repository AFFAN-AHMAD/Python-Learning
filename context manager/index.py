class fileManager:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if(self.file):
            self.file.close()

with fileManager('myText.txt') as file:
    print('do some stuff')
    file.write('some todo')
