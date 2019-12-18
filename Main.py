import MachineClass as Turing
import FileOpen as file

def main():
    openFile = input("Do you want to launch from a file? ")
    
    if openFile == "yes" or openFile == "y" or openFile == "1" or openFile == "Yes":
        fileChosen = int(input("Enter a question number "))
        tape_values, start, final, transition_rules, head = file.getRules(fileChosen)
        tape_length = (len(tape_values)-1)
        print(tape_length)

        examQuestion(tape_values, start, final, transition_rules, head, tape_length)
        
    elif openFile == "no" or openFile == "n" or openFile == "0" or openFile == "No":
        tape_values = ("1","0","1","/","0","1","1","0","/","1","0")
        tape_length = 11
        head = 5
        start = 0
        final = 0
        transition_rules = None
        
        userRan(tape_values, start, final, transition_rules, head, tape_length)
    else:
        print("Enter yes or no")


def examQuestion(tape_values, start, final, transition_rules, head, tape_length):
    machine = Turing.TuringMachine(tape_length, tape_values, head, start, final, transition_rules)
    machine.makeTape()
    currentState = start.strip()
    #print(transition_rules)
    headItem = machine.HeadItem()
    print(headItem, currentState)

    while currentState != final.strip():
        for rule in transition_rules:
            #print(rule)
            if currentState in rule and headItem in rule:
                #print(rule)
                #print("yeet")
                ruleList = list(rule)

                if currentState == ("".join(ruleList[1:3])) and headItem == ("".join(ruleList[5])):
                    print(rule)
                    print("big yeet")
                
                    #get new state
                    newState = "".join(ruleList[11:13])
                    print(newState)

                    #get new head value
                    newHeadItem = "".join(ruleList[15])
                    print(newHeadItem)

                    #get direction
                    headMove = "".join(ruleList[18])
                    print(headMove)

                    #run rules########
                    
                    #change state
                    currentState = newState

                    #change head item
                    error = machine.editHead(newHeadItem)

                    if error != (""):
                        currentState = final.strip()
                        print(error)

                    #move head
                    error2 = machine.moveHead(headMove)
                    headItem = machine.HeadItem()
                    
                    if error2 != (""):
                        currentState = final.strip()
                        print(error2)


                    print(machine.TapeData)
                    print(machine.head)
                    print(machine.HeadItem())
                    print(currentState)

def userRan(tape_values, start, final, transition_rules, head, tape_length):
    machine = Turing.TuringMachine(tape_len0gth, tape_values, head, start, final, transition_rules)
    machine.makeTape()
    print(machine.HeadItem())
    print(machine.moveHead("Left"))
    print(machine.TapeData)
    print(machine.HeadItem())
    print("____")
    print(machine.editHead(0))
    print("----")
    print(machine.TapeData)
    print(machine.moveHead("R"))
    print(machine.moveHead("R"))
    print(machine.editHead("Blank"))
    print(machine.TapeData)

    
   
if __name__ == "__main__":
    main()
                    
