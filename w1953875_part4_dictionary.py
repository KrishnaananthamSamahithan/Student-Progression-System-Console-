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
version =0
loop_exit = True
list_student = []
list_total_progression = []
Student_Progression_dict = {}

# Funtion to print '#' for 60 times in a line
def print1():
    
    for i in range (0,60):
        print('#',end='')
        
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
        list_progress.extend([["Progress- ", Pass, Defer, Fail]])     #Extend the progress list to append the variables as nested list


    # Condition to check output as Progress (Module Trailer)
    elif Pass == 100:
        Trailing += 1
        print("Progress (module trailer)")
        print("")
        list_trailer.extend([["Progress (module trailer)- ", Pass, Defer, Fail]])      #Extend the progress list to append the variables as nested list

    # Condition to check the output as Exclude
    elif Fail >= 80:
        Exclude += 1
        print("Exclude")
        print("")
        list_exclude.extend([["Exclude- ", Pass, Defer, Fail]])      #Extend the progress list to append the variables as nested list  

    # Condition to check the output as Progress(Module Retriever)
    else:
        Retriever += 1
        print("Do not progrerss (module retriever)")
        print("")
        list_retriever.extend([["Do not progrerss (module retriever)- ", Pass, Defer, Fail]])    #Extend the progress list to append the variables as nested list

# Function for dictionary and take 2 main list 'list_total_progression' and 'list_student' to append all the inputs and print as a dictionary 
def dictionary (Pass, Defer, Fail):
#refer from (https://appdividend.com/2022/09/24/python-zip-dictionary/)  
    for item in list_progress:
        list_student
        list_total_progression.append(",".join(str(x)for x in item))
        Student_Progression_dict = dict(zip(list_student, list_total_progression))
    for item in list_trailer:
        list_student
        list_total_progression.append(",".join(str(x)for x in item))
        Student_Progression_dict = dict(zip(list_student, list_total_progression))
    for item in list_retriever:
        list_student
        list_total_progression.append(",".join(str(x)for x in item))
        Student_Progression_dict = dict(zip(list_student, list_total_progression))
    for item in list_exclude:
        list_student
        list_total_progression.append(",".join(str(x)for x in item))
        Student_Progression_dict = dict(zip(list_student, list_total_progression))
    #print (''.join("{} : {} ".format(list_student, list_total_progression) for list_student, list_total_progression in Student_Progression_dict.items()))
    print(Student_Progression_dict)
while True:
    # use try except method for integer require
    try:
        # Get input for pass defer fail and check
        Student_ID = input("Enter Your Student ID: ")
        if Student_ID in list_student:
            print("Student ID Already Exist")
            continue
        else:
            list_student.append(Student_ID)
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
                # get input to continue or quit the programme
                loop_exit = True
                while loop_exit is True:
                    quit = str(input("Please Press 'Y' to proceed Or press 'q' to exit:"))
                    if quit == 'y':
                        loop_exit = False
                    elif quit == 'q':
                        dictionary (Pass, Defer, Fail)
                        break
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
