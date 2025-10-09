class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"File '{filename}' created!")

handler = FileHandler("data.txt")