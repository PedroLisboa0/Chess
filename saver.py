import datetime

class Saver:
    def __init__(self, file: str):
        self.file = file
        
    def save(self, position: str):
        with open(self.file, "a") as file:
            file.write(position[:-1])

    def create_game(self):
        with open(self.file, "a") as file:
            current_datetime = datetime.datetime.now()
            file.write(str(current_datetime)[:16]+"\n")


