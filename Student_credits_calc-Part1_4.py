# I declare that my work contains no examples of misconduct, such as plagiarism, or 
#collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1899717
 
# Date: 23/11/2022

grades = range(0,121,20)
outcome =[]
outcome_dict=[]
user=[]
def writetxt():
    text='out_dict.txt'
    with open(r'out_dict.txt', 'w') as o:
        for list in outcome_dict:
            o.write('%s' %list)
    o.close()
    text=open('out_dict.txt', 'r')
    content=text.read()
    text.close()
    print(content, end="")
    print('\n','Done')
    #https://www.pythontutorial.net/python-basics/python-write-text-file/     
def FinishLine():
    x= outcome.count('Progress')
    y= outcome.count('Retriever')
    w=outcome.count('Trailer')
    z= outcome.count('Excluded')
    u= x+y+w+z
    print("\n-------------------------------------------------------")
    print("Histogram")
    print("Progress ",+x,":",("*"*x))
    print("Trailer",+w,":",("*"*w))
    print("Retriever ",+y,":",("*"*y))
    print("Excluded",+z,":",('*'*z))
    print("\n",u,"outcomes in total")
    print("\n-------------------------------------------------------")
    writetxt()
    #write a code to read a every line of the list
def LeaveRequest():
    q=input(("Press'q' to leave or press 'y' to continue:").lower())
    if q == "q":
        FinishLine()
    elif q=="y":
        program()
    else:
        print("Wrong input, please continue with 'q' or 'y'")
        LeaveRequest()
def program():
    p=int(input("Please enter your credits at pass: "))
    if p not in grades:
        print("Out of range")
        LeaveRequest()
    d=int(input("Please enter your credits at defer: "))
    if d not in grades:
        print("Out of range")
        LeaveRequest()
    f=int(input("Please enter your credits at fail: "))
    if f not in grades:
        print("Out of range")
        LeaveRequest()
    elif p and d and f>120:
         print("Total incorrect")
    elif p+d+f>120:
        print("Toltal incorrect")
    elif p == 120 and d <=120 and f<=120:
        outcome.append("Progress")
        print("Progress\n")
        # part2
        pro_add='\n','{[0]} : Progress- {},{},{}'.format(user,p,d,f)
        outcome_dict.extend(pro_add) 
    elif p== 100 and d+f == 20:                                                                                                
        outcome.append("Trailer")
        print("Progress (module trailer)\n")
        # part2
        pro_add='\n','{[0]} : Trailer-{},{},{}'.format(user,p,d,f)
        outcome_dict.extend(pro_add)
    elif p<=80 and d<=120 and f<=60:
        outcome.append("Retriever")
        print("Module retriever\n")
        # part2
        pro_add='\n','{[0]} : Retriever-{},{},{}'.format(user,p,d,f)
        outcome_dict.extend(pro_add)

    elif p<=40 and d<=20 and f <=80:
        outcome.append("Excluded")
        print("Excluded\n")
        # part2
        pro_add='\n','{[0]} : Excluded-{},{},{}'.format(user,p,d,f)
        outcome_dict.extend(pro_add)
    # https://docs.python.org/3/library/string.html#format-string-syntax
    LeaveRequest()
# try loop
def loop_body():
    while True:
        try:
            l=input("please enter User ID:")
            user.append(l)
            program()
        except:
            print("intiger required")
            LeaveRequest()
        else:
            break
loop_body()
