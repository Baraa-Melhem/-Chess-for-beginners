import numpy as nb
import pandas as pd
users = []
namesus=[]
agesus=[]
IDsus=[]
gendersus=[]
usersinfo={"Name ":namesus,
           "Age ":agesus,
           "Gender ":gendersus,
           "ID ":IDsus}
uradnumint=1
num=0
adnum=0
numbad=0
kad=[]
Admins = [["admin1","@jqhq21ll1","15633","0"]]
white_move=[]
black_move=[]
squaresnum = ['1','2','3','4','5','6','7','8']
squareslett =['a','b','c','d','e','f','g','h']
pieces = ['B','N','K','Q','R']
def names():
    while True:
        first_name = input("Please enter your first name (letters only): ")
        first_name = first_name.replace(" ", "")
        last_name = input("Please enter your last name (letters only): ")
        last_name = last_name.replace(" ", "")
        if first_name.isalpha() and last_name.isalpha():
            name = first_name+" "+last_name
            break
        else:
            print("First name and last name must contain only letters. Please try again.")
    
    return name 
def ages():
    while True:   
        age = input(" enter your age : ")
        agecheck=age.isdigit()
        if agecheck==True:
            break
        else:
            print(" only numbers allowed \n")
            continue
    return age 
def genders():
    while True:
        gender = input("Please enter your gender (male or female): ")
        gender = gender.replace(" ", "")
        if gender.lower() == "male":
            gender = "Male"
            break
        elif gender.lower() == "female":
            gender = "Female"
            break
        else:
            print("Gender must be male or female. Please try again.")

    return gender
def passwords():
    # password=str(input( " enter a password : "))
    while True:
        passw = input("Please enter a password with at least 8 characters, letters, at least 1 special character, and at least one number, with no spaces: ")
        has_letter = False
        has_number = False
        has_special = False
        has_space = False
        if len(passw) < 8:
            print("Password must be at least 8 characters. Please try again.")
            continue
        for char in passw:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif char.isspace():
                has_space = True
            else:
                has_special = True
        if has_letter and has_number and has_special and not has_space:
            password = passw
            break
        else:
            print("Password must contain at least 8 characters, letters, at least 1 special character, and at least one number, with no spaces. Please try again.")

    return password













ID=0

while True:
    while True:
        choose =input( " 1.sign up 2.log in : ")
        checkchoose=choose.isdigit()
        if checkchoose==False:
            print("## wrong input please choose one of the choices.. \n")
        elif checkchoose==True:
            choose=int(choose)
            if choose == 1 or choose == 2 or choose==254:
                break
            else:
                print("## wrong input please choose one of the choices.. \n")



        
    if choose == 1 :
        print(" #signing up : \n")
        name =names()
        age = ages()
        gender = genders()
        password = passwords()
        IDD=str(ID)
        listn=[name,age,gender,password,IDD]
        users.append(listn)
        print("\nthis is your ID number : ", IDD , " \n #save it we will ask for it when you login\n \n ")

        namesus.append(name)
        agesus.append(str(age))
        IDsus.append(str(IDD))
        gendersus.append(gender)
        ID=ID+1
        choose =0
    if choose ==2: 
        print(" #logging in ")
        urname=str(input(" enter your name : "))
        urpass=str(input(" enter your password : "))
        while True:
            urID = input("Please enter your ID number: ")
            if urID.isdigit()==False:
                print("ID number must be a number. Please try again.")
            if urID.isdigit()== True and int(urID) >=0 and int(urID) <=ID:
                k = users[int(urID)]
                break
            else :
                print('\n unvalid ID , please enter a valid ID \n ')

            
        if  k[0]==urname and k[3]==urpass and k[4]== urID:
            chareng =1
            print ("#joining..")
            if chareng == 1:

                while True :   
                    wantto =str(input(" would you like to \n 1.enter \n 2.learn moves \n 3.your information \n 4.exit \n  please enter the number of your choice :  "))
                    checkwantto = wantto.isdigit()
                    if checkwantto==False:
                        print(" not correct input \n")
                    choice =int(wantto) 
                    if choice == 1 :
                        while True:

                              m1=input ("\n enter the white move : ")
                              m2=input("\n enter the black move : ")
                              white_move.append(str(m1))
                              black_move.append(str(m2))
                              while True:
                                  choose_cl=input("1. complete \n 2.done \n : ")
                                  checkcl=choose_cl.isdigit()
                                  if checkcl==False:
                                      print(" incorrect input ")
                                  elif checkcl==True:
                                      choose_cl=int(choose_cl)
                                      break
                                  
                              if choose_cl==1:
                                  pass
                              elif choose_cl==2:
                                  break
                              else:
                                  print("incorrect input \n ")
                                  while True:
                                      choose_cl=input("1. complete \n 2.done \n : ")
                                      checkcl=choose_cl.isdigit()
                                      if checkcl==False:
                                          print(" incorrect input ")
                                      elif checkcl==True:
                                          choose_cl=int(choose_cl)
                                          break   
                        white_move.append("ii")
                        black_move.append("kk")
                        white_move.append("ii")
                        black_move.append("kk")                                 
                        if white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="d6" :
                            print (" this opining called philidor defense\n ")
                            False
                                    
                        elif white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="nf6" :
                            print (" this opining called russian defense ")    
                        elif white_move[0]=="e4" and  black_move[0]=="c5" and white_move[1]=="n3" and black_move[1]=="nc6" :
                            print (" this opining called sicilian defense ")
                        elif white_move[0]=="e4" and  black_move[0]=="d5"  :
                            print (" this opining called scandinavian defense ")    
                        elif white_move[0]=="e4" and  black_move[0]=="e6" and white_move[1]=="d4" and black_move[1]=="d5" :
                            print (" this opining called french defense ")  
                        elif white_move[0]=="e4" and  black_move[0]=="c6" and white_move[1]=="d4" and black_move[1]=="d5" :
                            print (" this opining called caro-kann defense ")  
                        elif white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="nc6" and white_move[2]=="bc4" :
                            print (" this opining called Italy game ") 
                        elif white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="nc6" and white_move[2]=="bb5":
                            print (" this opining called ruy lopez opening ") 
                        elif white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="nc6" and white_move[2]=="d4" :
                            print (" this opining called scotch opening ") 
                        elif white_move[0]=="d4" and  black_move[0]=="d5" and white_move[1]=="c4" and black_move[1]=="e6" :
                            print (" this opining called queen's gambit declined defense ") 
                        elif white_move[0]=="d4" and  black_move[0]=="d5" and white_move[1]=="c4" and black_move[1]=="d6" :
                            print (" this opining called slav defense ") 
                        elif white_move[0]=="d4" and  black_move[0]=="d5" :
                            print (" this opining called queen's gambit opining ") 
                        elif white_move[0]=="e4" and  black_move[0]=="e5" and white_move[1]=="nf3" and black_move[1]=="nc6" and white_move[2]=="d4" :
                            print (" this opining called scotch defense ") 
                        
                        
                        else:
                            print("we don't know about this yet \n ")    
 
                        
                            
                            
                    elif choice == 2:
                        lang=int(input (" language / اللغة    \n 1.english \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 2.العربية \n : "))
                        if lang==1:
                            kindof = str(input(" do you want to know \n 1. defense \n 2. opening \n please enter the number of your choice :"))
                            if int(kindof) == 1 :
                                defen = int(input(" do you want to know defenses against : \n 1.e4 \n 2.d4 \n please enter the number of your choice :"))
                                if defen == 1:
                                    choose1 = int(input("choose one of these defenses against e4 : \n 1.philidor defense \n 2.russian defense \n 3.sicilian defense \n 4.scandinavian defense \n 5.french defense \n 6.caro-kann defense \n please enter the number of your choice :"))
                                    if choose1 == 1 :
                                        print (" philidor defense moves are : 1. e4 e5 2. Nf3 d6.")
                                    elif choose1 ==2:
                                        print (" russian defense moves are : 1.e4 c5 2. Nf3 Nc6")
                                    elif choose1 ==3:
                                         print (" sicilian defense moves are : 1.e4 e5 2. Nf3 Nf6")
                                    elif choose1 ==4:
                                        print (" scandinavian defense moves are :1.e4 d5")
                                    elif choose1 ==5:
                                        print (" french defense moves are : 1.e4 e6 2.d4 d5")
                                    elif choose1 ==6:
                                        print (" caro-kann defense moves are : 1.e4 c6 2.d4 d5")
                                    else:
                                        print("we don't know about this yet ")
                                elif defen == 2:
                                    choose1 = int(input("choose one of these defenses against d4 : \n 1.queen's gambit declined defense \n 2.slav defense\n please enter the number of your choice :"))
                                    if choose1 == 1 :
                                        print (" queen's gambit declined defense moves are : 1. d4 d5 2. c4 e6 ")
                                    elif choose1 ==2:
                                        print (" slav defense moves are : 1. d4 d5 2. c4 c6 ")
                                    else:
                                        print("we don't know about this yet ")
                            elif int(kindof) == 2 :
                                defen = int(input(" do you want to know opening for white on : \n 1.e4 \n 2.d4 \n please enter the number of your choice :"))
                                if defen == 1:
                                    choose1 = int(input("choose one of these openings on e4 : \n 1.Italy  \n 2.ruy lopez  \n 3.scotch \n please enter the number of your choice :"))
                                    if choose1 == 1 :
                                        print (" Italy opening moves are : 1.e4 e5 2.Nf3 Nc6 3.Bc4 ")
                                    elif choose1 ==2:
                                        print (" ruy lopez opening moves are : 1.e4 e5 2.Nf3 Nc6 3.Bb5 ")
                                    elif choose1 ==3:
                                         print (" scotch opening moves are : 1.e4 e5 2.Nf3 Nc6 3.d4")
                                    else:
                                        print("we don't know about this yet ")
                                elif defen == 2:
                                    choose1 = int(input("choose one of these openings on d4 : \n 1.queen's gambit \n please enter the number of your choice :"))
                                    if choose1 == 1 :
                                        print (" queen's gambit opening moves are : 1.d4 d5 2.c4 ")
                                    else:
                                        print("we don't know about this yet ")   
                        elif lang == 2:
                            while True :   
                                wantto =1
                                choice =int(wantto) 
                                if choice == 1 :
                                    kindof = str(input("هل ترغب في معرفة \n 1. الدفاع \n 2. الافتتاح \n 3.exit \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                    if int(kindof) == 1 :
                                        defen = int(input("هل ترغب في معرفة الدفاع ضد : \n 1.e4 \n 2.d4 \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                        if defen == 1:
                                            choose1 = int(input("إختر واحدا من هذه الدفاعات ضد e4 : \n 1.دفاع فيليدور \n 2.دفاع روسي \n 3.دفاع سيشيلي \n 4.دفاع شمال أوروبي \n 5.دفاع فرنسي \n 6.دفاع كارو-كان \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                            if choose1 == 1 :
                                                print ("حركات دفاع فيليدور هي : 1. e4 e5 2. Nf3 d6.")
                                            elif choose1 ==2:
                                                print ("حركات الدفاع الروسي هي : 1.e4 e5 2. Nf3 Nf6")
                                            elif choose1 ==3:
                                                 print ("حركات الدفاع الصقلي هي : 1.e4 c5 2. Nf3 Nc6")
                                            elif choose1 ==4:
                                                print ("حركات الدفاع الاسكندنافي هي :1. e4 d5")
                                            elif choose1 ==5:
                                                print ("حركات دفاع فرنسي هي : 1.e4 e6 2.d4 d5")
                                            elif choose1 ==6:
                                                print ("حركات دفاع كارو-كان هي : 1.e4 c6")
                                            else:
                                                print("لا نعرف عن هذا بعد")
                                        elif defen == 2:
                                            choose1 = int(input("إختر واحدا من هذه الدفاعات ضد d4 : \n 1.تضحية الوزير المرفوضة \n 2.الدفاع السلافي \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                            if choose1 == 1 :
                                                print ("حركات تضحية الوزير المرفوضة هي : 1. d4 d5 2. c4 e6 ")
                                            elif choose1 ==2:
                                                print ("حركات الدفاع السلافي هي : 1. d4 d5 2. c4 c6 ")
                                            else:
                                                print("لا نعرف عن هذا بعد")
                                    elif int(kindof) == 2 :
                                        defen = int(input("هل ترغب في معرفة الافتتاح للأبيض على : \n 1.e4 \n 2.d4 \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                        if defen == 1:
                                            choose1 = int(input("إختر واحدا من هذه الافتتاحات على e4 : \n 1.إيطاليا \n 2.روي لوبيز \n 3.سكوتش \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                            if choose1 == 1 :
                                                print ("حركات الافتتاح الإيطالي هي : 1.e4 e5 2.Nf3 Nc6 3.Bc4 ")
                                            elif choose1 ==2:
                                                print ("حركات الافتتاح روي لوبيز هي : 1.e4 e5 2.Nf3 Nc6 3.Bb5 ")
                                            elif choose1 ==3:
                                                 print ("حركات الافتتاح السكوتش هي : 1.e4 e5 2.Nf3 Nc6 3.d4")
                                            else:
                                                print("لا نعرف عن هذا بعد")
                                        elif defen == 2:
                                            choose1 = int(input("إختر واحدا من هذه الافتتاحات على d4 : \n 1.الجبهة الملكية \n الرجاء إدخال رقم الخيار الذي تختاره :"))
                                            if choose1 == 1 :
                                                print ("حركات تضحية الوزير هي : 1.d4 d5 2.c4 ")
                                            else:
                                                print("لا نعرف عن هذا بعد")   
                                    elif int(kindof) == 3 :
                                        break
                        
                    elif choice == 3:
                        print("\n your information : ")
                        print("name :" ,k[0])
                        print("age :" ,k[1])
                        print("gender :" ,k[2])
                        print("ID :" ,k[4])
                    elif choice == 4:
                        break
                        
                    else:
                        print(" not correct ")
                choose = 0
                
                
                
                
    if choose==254:
        print(" #logging in ")
        uradname=str(input(" enter your name : "))
        uradpass=str(input(" enter your password : "))
        while True:
            urfadnum = input("Please enter your # number: ")
            if urfadnum.isdigit()==False:
                print(" your # number must be only a number. Please try again.")
            if urfadnum.isdigit()== True:
                urfadnum=int(urfadnum)
                break
        uradnum=str(urfadnum)
        while True:
            uradID = input("Please enter your ID number: ")
            if uradID.isdigit()==False:
                print("ID number must be a number. Please try again.")
            if uradID.isdigit()== True and int(uradID) >=0 and int(uradID) <=int(numbad):
                kad=Admins[int(uradID)]
                break
            else :
                print('\n unvalid ID , please enter a valid ID \n ')

        if  kad[0]!=uradname or kad[1]!=uradpass or kad [2]!= uradnum or kad[3]!= uradID:
            print(" incorrect input " )
            while True :
                print(" #logging in ")
                uradname=str(input(" enter your name : "))
                uradpass=str(input(" enter your password : "))
                uradnumint=input(" enter your # number : ")
                uradnum=str(uradnumint)
                while True:
                    uradID = input("Please enter your ID number: ")
                    if uradID.isdigit()==False:
                        print("ID number must be a number. Please try again.")
                    if uradID.isdigit()== True and int(uradID) >=0 and int(uradID) <=int(numbad):
                        kad=Admins[int(uradID)]
                        break
                    else :
                        print('\n unvalid ID , please enter a valid ID \n ')




                if  kad[0]==uradname and kad[1]==uradpass and kad [2]==uradnum  and kad[3]==uradID :
                    break
        if  kad[0]==uradname and kad[1]==uradpass and kad [2]==uradnum  and kad[3]== uradID:
            print(" hi admin ")
            while True:
                adchoose= int(input("\n 1.add a new admin\n 2.users information \n 3.exit \n your choice:"))
                if adchoose !=1 and adchoose !=2 and adchoose !=3:
                    while True:
                        adchoose= input("\n 1.add a new admin\n 2.users information \n 3.exit \n your choice:")
                        if adchoose ==1 and adchoose ==2 and adchoose ==3:
                            break
                if adchoose==1:
                    urplussid=uradnumint=uradnumint+1
                    addad=[]
                    addad.append("admin"+str(urplussid))
                    print(" Name : "+addad[0])
                    addad.append(passwords())
                    idnumb=nb.random.randint(1,7,(1,6))
                    string_without_spaces = ''.join(map(str, idnumb[0]))
                    addad.append(string_without_spaces)
                    numbadplussone=numbad=numbad+1
                    addad.append(str(numbadplussone))
                    Admins.append(addad)
                    
                    print("\n"," Name : "+addad[0])
                    print("\n","this is your # number :",string_without_spaces)
                    print("\n"," this is your ID number :",numbadplussone)
                    
                    
                    
                if adchoose==2:
                    usersdata= pd.DataFrame(usersinfo)
                    print(usersdata)
                    
                if adchoose == 3:
                    break
            choose=0