class Saver:
    def __init__(self, file: str):
        self.file = file
        
    def save(self, position: str):
        with open(self.file, "w") as file:
            file.write(position)


