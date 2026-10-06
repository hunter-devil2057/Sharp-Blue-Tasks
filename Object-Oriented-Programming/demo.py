class Std: 
    def __init__(self, name, marks):
        self.name = name 
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks     # private
    def set_marks(self, marks):
        if marks >= 0 and marks <=100:
            self.__marks = marks
        else:
            print("Invalid Marks!!!")

# Creating Object
std = Std("Manish", 90)
print(std.get_marks())