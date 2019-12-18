class TuringMachine():
    def __init__(self,
                 tape_length,
                 tape_values,
                 head = 0,
                 start = 0,
                 final = 0,
                 transition_rules = None):
        self.TapeData = {}
        self.head = head
        self.tape_length = tape_length
        self.Blank = "/"
        self.possibleValues = ("0", "1", self.Blank, "e", "o", "#", "x", "y")
        self.tape_values = tape_values
        
        #self.tape = TapeClass.MakeTape(self.tape_length, tape_values)
        
    def make_tape(self):
        if self.tape_values == None:
            for i in range(self.tape_length):
                self.TapeData[i] = self.Blank
        elif self.tape_values != None:
            for y in range(self.tape_length):
                if self.tape_values[y] == "blank" or self.tape_values[y] == "/":
                    self.TapeData[y] = self.Blank
                else:
                    self.TapeData[y] = self.tape_values[y]
        


    def move_head(self, direction):
        if self.head >= 0 and self.head <= (self.tape_length-1):
            if direction == "Right" or direction == "R":
                self.head += 1
                return("")
            elif direction == "Left" or direction == "L":
                self.head -= 1
                return("")
            elif direction == "/" or direction == "Blank":
                self.head = self.head
            else:
                return ("Direction must be Left, Right or Blank")
        else:
            return ("Attempting to edit index not in dictionary")

    def head_item(self):
        return self.TapeData[self.head]

    def edit_head(self, value):
        if self.head >= 0 and self.head <= self.tape_length-1:
            if value in self.possibleValues:
                self.TapeData[self.head] = value
                return("")
            elif value == "Blank" or value == "blank":
                self.TapeData[self.head] = self.Blank
                return("")
            else:
                return "Value supplied does not match requirements"
        else:
            return "Attempting to edit index not in dictionary"

        


if __name__ == "__main__":
    
    #tape_values = ("1","0","1","blank","0","1","1","0","blank","1","0")
    #tape_values1 = None
    tape_values, start, final, transition_rules, head = file.getRules(1)
    
    machine = TuringMachine(10, tape_values, 5)
    print(machine.returnHeadItem())
    print(machine.moveHead("Left"))
    print(machine.tape.TapeData)
    print(machine.returnHeadItem())
    print("____")
    print(machine.editHead("blank"))
    print("------")
    print(machine.tape.TapeData)
    
    
