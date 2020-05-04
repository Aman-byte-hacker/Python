class students:
    def __init__(self):
        self.name="Aman"
        self.rollno=12
        self.lap=self.Laptop()
    class Laptop:
        def __init__(self):
            self.name="hp"
            self.processor="i5"
            self.ram=8
        def show(self):
            return(self.ram,self.processor,self.name)

s=students()
s.name="priya"
s.rollno=14

def show(self):
    return(self.name,self.rollno,self.lap.show())

print(show(s))