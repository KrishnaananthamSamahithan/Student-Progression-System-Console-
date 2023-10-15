# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1953875
# Student Name: Samahithan Krishnaanantham
# Date: 14/12/2022

credit = 0
total_credit = 0
Progress = 0
Trailing = 0
Retriever = 0
Exclude = 0
list_progress = []
list_trailer = []
list_retriever = []
list_exclude = []
version = 0
loop_exit = True
loop_Start = True

# Funtion to print '-' for 60 times in a line
def print1():
    for i in range (0,60):
        print('-',end='')

#Function to Print "Out of range" whether the input credits are not in the range 0 ,20, 40, 60, 80, 100 and 120
def check_input_range (credit):
    #refer from (https://www.javatpoint.com/python-sys-module)
    import sys
    if credit % 20 == 0 and credit <= 120:
        pass          
    else:
        print("Out of range")
        sys.exit()
        

#function to predict progression outcomes for the input Credits
def progression_outcome (Pass,Defer,Fail):
    
    #Define variables such as (Progress, Trailing, Exclude, Retriever) to Global to use these variable in different functions 
    global Progress 
    global Trailing
    global Exclude
    global Retriever
    
    # Condition to check output as Progress
    if Pass == 120:
        Progress += 1
        print("Progress")
        print("")
        list_progress.extend([[Pass, Defer, Fail]])     #Extend the progress list to append the variables as nested list

    # Condition to check output as Progress (Module Trailer)
    elif Pass == 100:
        Trailing += 1
        print("Progress (module trailer)")
        print("")
        list_trailer.extend([[Pass, Defer, Fail]])      #Extend the progress list to append the variables as nested list

    # Condition to check the output as Exclude
    elif Fail >= 80:
        Exclude += 1
        print("Exclude")
        print("")
        list_exclude.extend([[Pass, Defer, Fail]])      #Extend the progress list to append the variables as nested list  

    # Condition to check the output as Progress(Module Retriever)
    else:
        Retriever += 1
        print("Do not progrerss (module retriever)")
        print("")
        list_retriever.extend([[Pass, Defer, Fail]])    #Extend the progress list to append the variables as nested list
   
    
#Function to print the out put as histogram
def histogram (Progress,Trailing,Retriever,Exclude):
    print1()
    print ("")
    star = "*"
    print("Histogram ")
    print("Progress " ,Progress,":",star * Progress)
    print("Progress (Module Trailer) " ,Trailing,":",star* Trailing)
    print(" Module Retriever" ,Retriever,":",star * Retriever)
    print("Excluded " ,Exclude,":",star * Exclude)
    total_outcome=Progress+Trailing+Retriever+Exclude
    print("")
    print(total_outcome,"outcomes in total.")
    print("")
    print1()

# Function to put the inputs to the list while the progression outcome 
def extend_list (Pass, Defer, Fail):
    # this reference from (https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/)
    print("")
    print("Part2 - List(Extention)")
    for item in list_progress:
        print("Progress - ",',' . join(str(x) for x in item))
    for item in list_trailer:
        print("Progress (Module Trailer) - ",',' . join(str(x) for x in item))
    for item in list_retriever:
        print("Module Retriver - ",',' . join(str(x) for x in item))
    for item in list_exclude:
        print("Exclude - ",',' . join(str(x) for x in item))
    print ("")
    print1()
    
    
# Function for create a text file and apend the output on it and again read it
#Referance From Lecture Slides
def file_handle(Pass, Defer, Fail):
    print("")
    print("Part3 - Text File(Extension)")
    f = 0
    f = open("Student_Progression_Report.txt", "w")
    
    f.close()
    
    f = open("Student_Progression_Report.txt", "a")
    for item in list_progress:
        f.write("Progress - "+',' . join(str(x) for x in item)+ "\n")
    for item in list_trailer:
        f.write("Progress (Module Trailer) - "+',' . join(str(x) for x in item)+ "\n")
    for item in list_retriever:
        f.write("Module Retriver - "+',' . join(str(x) for x in item)+ "\n")
    for item in list_exclude:
        f.write("Exclude - "+',' . join(str(x) for x in item))
    
    f.close()

    f = open("Student_Progression_Report.txt", "r")
    for line in f:
        print (line, end = "")

    f.close()
    print ("\n")
    print1()
    

        

#Take input from Users for Pass, Defer and Fails
# try: except: to validate whether the inputs are in integers
   
# Main Programme
print("================ Welcome to the Student Progression Program ================")
while True:
    #use try except for menu validation
    try:
        #Create a menu for the programme option
        print("\n Please Select a Option to Continue the Programme")
        print("1. Student Version")
        print("2. Staff Version")
        print("3. Close the Program\n")
        version =int(input("Please Enter the version No: ")) #Get input for programme version
        print1()
        print('')
        if version == 1:
            while True:
                try:
                    # Get input for pass defer fail and check
                    print("To Check Your Progression Please Enter the Following Details. ")
                    Pass = int(input("\nPlease Enter the credits at pass: "))
                    check_input_range(Pass)
                    Defer = int(input("Please Enter the Credits at Defer: "))
                    check_input_range(Defer)
                    Fail = int(input("Please Enter the Credits af Fail: "))
                    check_input_range(Fail)
                    total_credit = Pass + Defer + Fail         # Add three input
                    if total_credit == 120:                    #check the total of input is 120
                        progression_outcome(Pass, Defer, Fail) # call Student ptogression function
                        break
                    else:
                        print("Total incorrect")
                        print('')
                except ValueError:
                    print("Integer required")
                    print('')
                
        elif version == 2:
            loop_Start = True
            while loop_Start is True:
                # use try except method for integer require
                try:
                    # Get input for pass defer fail and check
                    print("To Check Your Progression Please Enter the Following Details. ")
                    Pass = int(input("\nPlease Enter the credits at pass: "))
                    check_input_range(Pass)
                    Defer = int(input("Please Enter the Credits at Defer: "))
                    check_input_range(Defer)
                    Fail = int(input("Please Enter the Credits af Fail: "))
                    check_input_range(Fail)
                    total_credit = Pass + Defer + Fail            # Add three input
                    if total_credit == 120:                       #check the total of input is 120
                        progression_outcome(Pass, Defer, Fail)    # call Student ptogression function
                        #try and except for the error handling to check continue or quite the programme
                        try:
                            loop_exit = True
                            while loop_exit is True:
                                # get input to continue or quit the programme
                                quit = str(input("Please Press 'Y' to proceed Or press 'q' to exit:"))
                                if quit == 'y':
                                    loop_exit = False
                                elif quit == 'q':
                                    histogram (Progress,Trailing,Retriever,Exclude)  #Call Histogram function
                                    extend_list (Pass, Defer, Fail)                  #Call list function
                                    file_handle(Pass, Defer, Fail)                   #Call file handling function
                                    loop_exit = False
                                    loop_Start = False
                                
                                     
                        except ValueError:
                            print("You Enter Wrong input")
                            quit = str(input("Please Press 'Y' to proceed Or press 'q' to exit:"))
                      
                    else:
                        print("Total incorrect")
                        print('')
                except ValueError:
                    print("Integer required")
                    print('')
                    quit = str(input("Please Press 'Y' to proceed Or press 'q' to exit:"))
        elif version == 3:
            print("========== Thank You For Using The Programme ==========")
            break
            
        else:
            print ("Please Enter the the menu value only")
            print('')
    except ValueError:
        print ("Please Enter the the menu value only")
        print('')

    
        
        
    
