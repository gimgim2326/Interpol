print ("INTERPOL Compiler")
print("Input BEGIN to begin. Input END to end.")

#round off
def normal_round(num, ndigits=0):
    if num<0:
        str_num = str(num)
        dummy_num = str_num.replace("-","")
        int_num = float(dummy_num)
    else:
        int_num = num

    if ndigits == 0:
        res = int(int_num + 0.5)
    else:
        digit_value = 10 ** ndigits
        res = int(int_num * digit_value + 0.5) / digit_value

    if num<0:
        res = "-" + str(res)

    return res

#initialize user input
user_input = str(input("$ "))
user_input = user_input.strip()

#check user input

while user_input != "BEGIN":
    if user_input == "END":
        print("Ending program.")
        break
    else:
        print("Input BEGIN to begin. Input END to end.")
        user_input = str(input("$ "))
        user_input = user_input.strip()
else:
    print("Starting program")
    cnt1 = 1
    while user_input != "END":
        user_input = str(input("$ "))
        user_input = user_input.strip()

        if user_input == "BEGIN" and cnt1 == 1:
            pass
        elif user_input!= "BEGIN" and user_input!= "END":
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
                pass
            #PRINT
            elif (first_word =="PRINT" or first_word =="PRINTLN") and num_of_words != 1 :
                if user_input.split()[1].startswith('\"'):
                    #check if ascii
                    a = ascii(user_input)
                    a = a.replace("'","")

                    if a == user_input and user_input[-1] == "\"":
                        print_word = user_input[int(user_input.find('\"')+1):int(user_input.rfind('\"'))]
                        #PRINTLN
                        #check escape characters
                        if "\"" in print_word or "\\" in print_word:
                            print("The syntax is incorrect.")
                        elif first_word =="PRINTLN":# and "/n" in print_word:
                            print(print_word + "\n")
                        elif first_word =="PRINT":
                            print(print_word)
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
                    if first_word == "ADD":
                        print_result = first_number + second_number
                    if first_word == "SUB":
                        print_result = first_number - second_number
                    if first_word == "MUL":
                        print_result = first_number * second_number
                    if first_word == "MOD":
                        if second_number != 0:
                            print_result = first_number % second_number
                        else:
                            print_result = "Error: Division by zero"
                    if first_word == "DIV":
                        if second_number != 0:
                            print_result = normal_round(first_number / second_number)
                        else:
                            print_result = "Error: Division by zero"
                    print(print_result)
            else:
                print("The syntax is incorrect.")
    else:
        print("Ending program.")