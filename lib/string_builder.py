class StringBuilder:
    def __init__(self) -> None:
        self.str = ""
    
    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)
    
    def output(self):
        return self.str