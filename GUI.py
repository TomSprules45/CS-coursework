import MachineClass as Turing
import FileOpen as File

from tkinter import *
import re
from tkinter.font import Font
import os



class GUIFrame():
    def __init__(self, master):
        master.configure(bg= '#f141f4')
        master.title("Turing Machine")
        myFont = Font(family="Comic Sans MS", size = 9)
        master.option_add("*Font", myFont)
        master.option_add("*Background", "#b79de8")
        master.option_add("*Label.Font", myFont)
        master.geometry("1920x1080")

        self.stateVAR = StringVar()

        self.seg1 = StringVar()
        self.seg2 = StringVar()
        self.seg3 = StringVar()
        self.seg4 = StringVar()
        self.seg5 = StringVar()
        self.seg6 = StringVar()
        self.seg7 = StringVar()
        self.seg8 = StringVar()
        self.seg9 = StringVar()
        self.seg10 = StringVar()
        self.seg11 = StringVar()

        self.seg1.set("/")
        self.seg2.set("/")
        self.seg3.set("/")
        self.seg4.set("/")
        self.seg5.set("/")
        self.seg6.set("/")
        self.seg7.set("/")
        self.seg8.set("/")
        self.seg9.set("/")
        self.seg10.set("/")
        self.seg11.set("/")

        self.step = False

        self.currentRuleVAR = StringVar()

        self.fileNameVAR = StringVar()

        self.frameA = Frame(master)
        self.frameA.pack(fill = "both", expand = False, anchor=NW)

        self.frameB = Frame(master, relief=GROOVE, borderwidth=1)
        self.frameB.pack(fill = "both", expand = True, anchor=SW)

        self.frameC = Frame(master)
        self.frameC.pack(fill = "both", expand = True, anchor=SW)
   
 
        
        self.build_frame_A()
        self.build_frame_B()
        self.build_frame_C()

        

    def build_frame_A(self):

        frameA1 = Frame(self.frameA)

        frameA1.pack(side=LEFT, pady=10, padx=30)


###########A############################################################

        
        labelA = Label(frameA1)
        labelA.config(text = "Turing Machine Learning tool", font=("Comic Sans MS", "16", "bold"))
        labelA.pack(side=LEFT, padx = 10, pady = 10)


        self.startEntry = Entry(frameA1, width=11)
        self.startEntry.pack(pady=20, padx=10)
        startButton = Button(frameA1, text="Start", command=self.start_machine)
        startButton.pack(pady=5, padx=10)
        
        


###########B##############################################################

    def build_frame_B(self):
        
        
        frameB1 = Frame(self.frameB, relief=GROOVE, borderwidth=1)
        
        frameB1.pack(side=LEFT, fill=Y)


##########B1###########################################################


        for i in range(13):
            frameB1.columnconfigure(i, pad=30)
            
        tapeLabel = Label(frameB1, text = ("Tape:"))
        tapeLabel.grid(row=0, column=0)

        stateLabel = Label(frameB1, textvariable=self.stateVAR, width=4, height=3 ,relief=SUNKEN)
        stateLabel.grid(row=2, column=0)

        self.tapeLabel1 = Label(frameB1, textvariable=self.seg1, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=1)
        self.tapeLabel2 = Label(frameB1, textvariable=self.seg2, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=2)
        self.tapeLabel3 = Label(frameB1, textvariable=self.seg3, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=3)
        self.tapeLabel4 = Label(frameB1, textvariable=self.seg4, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=4)
        self.tapeLabel5 = Label(frameB1, textvariable=self.seg5, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=5)
        self.tapeLabel6 = Label(frameB1, textvariable=self.seg6, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=6)
        self.tapeLabel7 = Label(frameB1, textvariable=self.seg7, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=7)
        self.tapeLabel8 = Label(frameB1, textvariable=self.seg8, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=8)
        self.tapeLabel9 = Label(frameB1, textvariable=self.seg9, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=9)
        self.tapeLabel10 = Label(frameB1, textvariable=self.seg10, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=10)
        self.tapeLabel11 = Label(frameB1, textvariable=self.seg11, width=6, height = 3, bg="white", relief=SUNKEN).grid(row=2, column=11)

        stateCurrent = Label(frameB1, text="Current State")
        stateCurrent.grid(row=3, column=0)
        
        self.headPoint = Label(frameB1, text="Head")
        self.headPoint.grid(row=3, column=6)
        
        self.headRight = Button(frameB1, text=">", command=self.move_right, width=3)
        self.headRight.grid(row=4, column=7)
        
        self.headLeft = Button(frameB1, text="<", command=self.move_left, width=3)
        self.headLeft.grid(row=4, column=5)

        self.headItemVar = StringVar()
        self.headItemVar.set("/")
        self.headOptions = ("/", "0", "1")
        self.headEdit = OptionMenu(frameB1, self.headItemVar, *self.headOptions)
        self.headEdit.grid(row=4, column=6)

        self.confirmEdit = Button(frameB1, text="✓", command=self.edit_head)
        self.confirmEdit.grid(row=5, column=6)



        
        self.stepButton = Button(frameB1, text="Step", command=(self.step_GUI))
        self.stepButton.grid(row=2, column=12)
        self.finished = Label(frameB1, text="Finished")


    def build_frame_C(self):

        typeRuleTitle = Label(self.frameC, text="Enter custom rules", relief=RAISED)
        typeRuleTitle.grid(row=1, column=1, columnspan=1, rowspan=1, sticky='ew')

        typeConfirm = Button(self.frameC, text="Save", command = self.save_rules)
        typeConfirm.grid(row=1, column=2)

        self.saveName = Entry(self.frameC, textvariable = self.fileNameVAR)
        self.saveName.grid(row=2, column=2)

        self.typeRules = Text(self.frameC, borderwidth=3, relief=SUNKEN)
        self.typeRules.config(font=("Comic Sans MS", 12), undo=True, wrap='word')
        self.typeRules.grid(row=3, column=1, columnspan=1, rowspan=1, sticky='ew')

        ruleInstruct = Text(self.frameC, borderwidth=3, relief=SUNKEN, width=40)
        ruleInstruct.config(font=("Comic Sans MS", 12), undo=True, wrap='word')
        ruleInstruct.grid(row=3, column=2, sticky='ew')

        ruleInstruct.insert(END, """ Tape data (any length)\n\n Start state\n\n End state\n\n-Come down a line-----\n\n Rules:\n (current state, current item) :\n (new state, new item, movement[R/L])
                            \n Items can be (0,1,/,e,o,#,x,y)\n\n\n Rules can be edited in text file""")
        

        displayRuleTitle = Label(self.frameC, text="Previous rule followed by all rules", relief=RAISED)
        displayRuleTitle.grid(row=1, column=3, columnspan=1, rowspan=1, sticky='ew', padx=50)
        
        self.displayRule = Label(self.frameC, textvariable = self.currentRuleVAR, relief=SUNKEN, font=("Comic Sans MS", 12))
        self.displayRule.grid(row=2, column=3, columnspan=1, rowspan=1, sticky='ew', padx=50)

        self.showRules = Text(self.frameC, borderwidth=3, relief=SUNKEN)
        self.showRules.config(font=("Comic Sans MS", 12), undo=True, wrap='word')
        self.showRules.grid(row=3, column=3, columnspan=1, rowspan=1, sticky='ew', padx=50)
        

#########Methods##################################################################################################

    def start_machine(self):
        self.finished.grid_forget()
        self.stepButton.grid(row=3, column=12)
        if (self.startEntry.get()) != "":
            try:
                int(self.startEntry.get())
                fileType = "Exam"
            except:
                fileType = "Custom"

            if fileType == "Exam":
                fileChosen = int(self.startEntry.get())
                tape_values, start, final, transition_rules, head, raw_rules = File.getRules(fileChosen)
                tape_length = (len(tape_values)-1)
                print(tape_length)

                self.exam_question(tape_values, start, final, transition_rules, head, tape_length, raw_rules)
                
            elif fileType == "Custom":
                fileChosen = self.startEntry.get()
                tape_values, start, final, transition_rules, head, raw_rules = File.getRules(fileChosen)
                tape_length = (len(tape_values)-1)

                self.exam_question(tape_values, start, final, transition_rules, head, tape_length, raw_rules)
                
            
        else:             
            tape_values = (self.seg1.get(), self.seg2.get(), self.seg3.get(), self.seg4.get(), self.seg5.get(), self.seg6.get(), self.seg7.get(), self.seg8.get(), self.seg9.get(), self.seg10.get(), self.seg11.get())
            print(tape_values)
            tape_length = 11
            head = 5
            start = 0
            final = 0
            transition_rules = None
            
            self.user_ran(tape_values, start, final, transition_rules, head, tape_length)
        


    def exam_question(self, tape_values, start, final, transition_rules, head, tape_length, raw_rules):
        self.machine = Turing.TuringMachine(tape_length, tape_values, head, start, final, transition_rules)
        self.machine.make_tape()
        
        self.tape_length = tape_length
        self.tape_values = tape_values
        self.head = head
        self.start = start
        self.final = final
        self.transition_rules = transition_rules
        self.raw_rules = raw_rules
        self.currentState = start.strip()
        
        self.headItem = self.machine.head_item()
        print(self.headItem, self.currentState)

        for i in range(len(self.raw_rules)):
            self.showRules.insert(END, str(self.raw_rules[i])+"\n")
        
        self.update_tape()
        self.stateVAR.set(self.currentState)
            
        self.headPoint.grid(row=3, column=(self.machine.head+1))
        self.headRight.grid(row=4, column=(self.machine.head+2))
        self.headLeft.grid(row=4, column=(self.machine.head))
        self.headEdit.grid(row=4, column=(self.machine.head+1))
        self.confirmEdit.grid(row=5, column=(self.machine.head+1))             


    def step_GUI(self):
        if self.currentState != self.final.strip():
            for rule in self.transition_rules:
                if self.currentState in rule and self.headItem in rule:
                    ruleList = list(rule)


                    if self.currentState == ("".join(ruleList[1:3])) and self.headItem == ("".join(ruleList[5])):
                        self.currentRuleVAR.set(rule)
                    
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
                        self.currentState = newState

                        #change head item
                        error = self.machine.edit_head(newHeadItem)

                        if error != (""):
                            self.currentState = self.final.strip()
                            print(error)

                        #move head
                        error2 = self.machine.move_head(headMove)
                        self.headItem = self.machine.head_item()
                        
                        
                        if error2 != (""):
                            self.currentState = self.final.strip()
                            print(error2)

                        #move GUI head
                        self.headPoint.grid(row=3, column=(self.machine.head+1))
                        self.headRight.grid(row=4, column=(self.machine.head+2))
                        self.headLeft.grid(row=4, column=(self.machine.head))
                        self.headEdit.grid(row=4, column=(self.machine.head+1))
                        self.confirmEdit.grid(row=5, column=(self.machine.head+1))

                        #show new state on GUI
                        self.stateVAR.set(self.currentState)

                        #print results
                        print(self.machine.TapeData)
                        print(self.machine.head)
                        print(self.machine.head_item())
                        print(self.currentState)
                        break
                    
        else:
            self.stepButton.grid_forget()
            self.finished.grid(row=3, column=12)
            self.showRules.delete(1.0, END)
            self.currentRuleVAR.set("")
            
                
        
        #display results to GUI
        self.update_tape()



    def update_tape(self):
        try:
            self.seg1.set(self.machine.TapeData[0])
        except:
            self.seg1.set("/")
        try:
            self.seg2.set(self.machine.TapeData[1])
        except:
            self.seg2.set("/")
        try:
            self.seg3.set(self.machine.TapeData[2])
        except:
            self.seg3.set("/")
        try:
            self.seg4.set(self.machine.TapeData[3])
        except:
            self.seg4.set("/")
        try:
            self.seg5.set(self.machine.TapeData[4])
        except:
            self.seg5.set("/")                            
        try:
            self.seg6.set(self.machine.TapeData[5])
        except:
            self.seg6.set("/")                           
        try:
            self.seg7.set(self.machine.TapeData[6])
        except:
            self.seg7.set("/")                           
        try:
            self.seg8.set(self.machine.TapeData[7])
        except:
            self.seg8.set("/")                          
        try:
            self.seg9.set(self.machine.TapeData[8])
        except:
            self.seg9.set("/")                          
        try:
            self.seg10.set(self.machine.TapeData[9])
        except:
            self.seg10.set("/")                            
        try:
            self.seg11.set(self.machine.TapeData[10])
        except:
            self.seg11.set("/")


                        
    def user_ran(self, tape_values, start, final, transition_rules, head, tape_length):
        self.machine = Turing.TuringMachine(tape_length, tape_values, head, start, final, transition_rules)
        self.machine.make_tape()



    def move_right(self):
        try:
            self.machine.move_head("Right")
            self.headPoint.grid(row=3, column=(self.machine.head+1))
            self.headRight.grid(row=4, column=(self.machine.head+2))
            self.headLeft.grid(row=4, column=(self.machine.head))
            self.headEdit.grid(row=4, column=(self.machine.head+1))
            self.confirmEdit.grid(row=5, column=(self.machine.head+1))
        except:
            print("press start")
        


    def move_left(self):
        try:
            self.machine.move_head("Left")
            self.headPoint.grid(row=3, column=(self.machine.head+1))
            self.headRight.grid(row=4, column=(self.machine.head+2))
            self.headLeft.grid(row=4, column=(self.machine.head))
            self.headEdit.grid(row=4, column=(self.machine.head+1))
            self.confirmEdit.grid(row=5, column=(self.machine.head+1))

        except:
            print("press start")
        

    def edit_head(self):
        try:
            self.machine.edit_head(self.headItemVar.get())
        except:
            print("press start")
            
        self.update_tape()
        

    def save_rules(self):
        lastLine = int(self.typeRules.index('end-1c').split('.')[0])
        ruleLines = []

        tapeNew = self.typeRules.get("1.0", "1.79")
        startState = self.typeRules.get("2.0", "2.79")
        endState = self.typeRules.get("3.0", "3.79")
        headPoint = self.typeRules.get("4.0", "4.79")

        for i in range(6, lastLine+1):
            index = str(i)
            rule = self.typeRules.get(index+".0", index+".79")
            rulesTest = re.search("^\(s[a-z0-9], [0-9/eo#xy]\) : \(s[a-z0-9], [0-9/eo#xy], [R/L]\)", rule)
            if not rulesTest:
                self.typeRules.insert(END, "\nEntered data is not in the correct format, please remove and try again")
                break
            ruleLines.append(rule)


        headTest = re.search("[0-9]+", headPoint)
        print(tapeNew, startState, endState)
        tapeTest = (re.search("1|0", tapeNew))


        stateTest = (re.search("^s", startState))
        stateTest2 = (re.search("^s", endState))
                     
        if stateTest and stateTest2 and rulesTest and headTest and tapeTest:
            if os.path.isfile(self.fileNameVAR.get()+".txt"):
                self.saveName.delete(0, END)
                self.saveName.insert(END, "File name is invalid")
            else:
                print("saving...")
                FileWrite = open((self.fileNameVAR.get()+".txt"), "w+")
                
                ruleString = ""
                for rule in ruleLines:
                    ruleString += (rule+"\n")
                lines = (tapeNew+"\n"+ startState+"\n"+ endState+"\n"+ headPoint+"\n\n"+ ruleString)
                
                FileWrite.write(lines)
                FileWrite.write("---fin---")
                FileWrite.close()
                self.saveName.delete(0, END)
        
        else:
            self.typeRules.insert(END, "\nEntered data is not in the correct format, please remove and try again")
        
      
def main():   
    root = Tk()
    app=GUIFrame(root)
    root.mainloop()


if __name__ == "__main__":
    main()













    
