def getRules(question):
    if question == 1:
        fileName = ("ExamQuestion1.txt")
    elif question == 2:
        fileName = ("ExamQuestion2.txt")
    elif question == 3:
        fileName = ("ExamQuestion3.txt")
    else:
        fileName = (question+".txt")

    
    FileRead = open(fileName, "r")
    lines = FileRead.readlines()

    #get tape values
    tape_values = lines[0]
    print("Tape data: ", tape_values.strip())

    #get start and finish states
    start = lines[1]
    final = lines[2]

    #get head place
    head = lines[3].strip()
    head = int(head)
    #get transition rules
    for y in range(len(lines)):
        if "--fin--" in lines[y]:
            lastRule = y
            
    transition_rules = []
        
    for line in lines[5:lastRule]:
        transition_rules.append(line.strip())

    raw_rules = []
    
    for line in lines[5:lastRule]:
        raw_rules.append(line.strip())

    
    FileRead.close()
    return tape_values, start, final, transition_rules, head, raw_rules



