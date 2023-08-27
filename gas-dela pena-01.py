print ("INTERPOL Syntax Checker")
print("Input BEGIN to begin. Input END to end.")

#initialize user input
user_input = str(input("$ "))
user_input = user_input.strip()
#user_input = user_input.replace("$ ","")

#check user input

while user_input != "BEGIN":
    if user_input == "END":
        print("Thank you for using the syntax checker.")
        break
    else:
        print("Input BEGIN to begin. Input END to end.")
        user_input = str(input("$ "))
        user_input = user_input.strip()
        #user_input = user_input.replace("$ ","")
else:
    print("The syntax is correct. Beginning syntax checker.")
    cnt1 = 1
    while user_input != "END":
        user_input = str(input("$ "))
        user_input = user_input.strip()
        #user_input = user_input.replace("$ ","")

        if user_input == "BEGIN" and cnt1 == 1:
            print("The syntax is correct.")
        elif user_input!= "BEGIN" and user_input!= "END":
            #user_input = user_input.replace("\" ","\"")
            #select the first letter
            first_letter = user_input[0]
            #select the first word
            first_word = user_input.split()[0]
            #number of words
            try:
                num_of_words = len(user_input.split())
            except ValueError:
                num_of_words = 1

            #comment
            if first_letter =="#":
                print("The syntax is correct.")
            #PRINT
            elif (first_word =="PRINT" or first_word =="PRINTLN") and num_of_words != 1 :
                if user_input.split()[1].startswith('\"'):
                    #check if ascii
                    a = ascii(user_input)
                    a = a.replace("'","")

                    if a == user_input and user_input[-1] == "\"":
                        print_word = user_input[int(user_input.find('\"')+1):int(user_input.rfind('\"'))]
                        #PRINTLN
                        #if "\"" in print_word:
                           # print("The syntax is incorrect.")
                        if first_word =="PRINTLN":# and "/n" in print_word:
                            print("The syntax is correct.")
                        elif first_word =="PRINT":
                            print("The syntax is correct.")
                        else:
                            print("The syntax is incorrect.")
                    else:
                        print("The syntax is incorrect.")
                else:
                    print("The syntax is incorrect.")
            #MATH KEYWORDS
            elif (first_word =="ADD" or first_word =="SUB" or first_word =="MUL" or first_word =="DIV" or first_word =="MOD") and num_of_words == 3:
                second_word = user_input.split()[1]
                third_word = user_input.split()[2]
                try:
                    first_number = int(second_word)
                    second_number = int(third_word)
                except ValueError:
                    print("The syntax is incorrect.")
                else:
                    if first_word == "DIV" or first_word =="MOD":
                        if second_number == 0:
                           print("The syntax is incorrect.")
                        else:
                            print("The syntax is correct.")
                    else:
                        print("The syntax is correct.")
            else:
                print("The syntax is incorrect.")
    else:
        print("Thank you for using the syntax checker.")