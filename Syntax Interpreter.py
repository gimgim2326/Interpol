#INTERPOL INTERPRETER BY GIMELLE ANN DELA PEñA
#MASTER OF INFORMATION SYSTEMS
#UNIVERSITY OF THE PHILIPPINES OPEN UNIVERSITY
#FIRST SEMESTER A.Y. 2021-2022

#importing modules
import sys
import os
import math
import os.path
from os import path

#declare reserved words and operations
reserved_words = ["VARINT","VARSTR", "ADD", "SUB", "MUL", "DIV", "BEGIN", "END", "PRINTLN","PRINT","STORE","INPUT", "WITH", "MOD","RAISE", "ROOT", "MEAN","DIST","IN"]
first_words = ["ADD", "SUB", "MUL", "DIV", "MOD", "RAISE", "ROOT", "MEAN", "DIST","VARINT","VARSTR","PRINT","PRINTLN","INPUT","STORE"]
ops = ["ADD", "SUB", "MUL", "DIV", "MOD", "RAISE", "ROOT", "MEAN", "DIST"]
ops_basic = ["ADD", "SUB", "MUL", "DIV", "MOD"]
ops_adv =["RAISE", "ROOT", "MEAN", "DIST"]
dec_var = ["VARSTR","VARINT"]
ipol_print = ["PRINTLN","PRINT"]
float_char ="."
dummy_exp=[]
dummy_mean = []

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

#basic operations
#add
def ops_add(a,b):
    c= float(a)+float(b)
    return c
#sub
def ops_sub(a,b):
    c= float(a)-float(b)
    return c
#mul
def ops_mul(a,b):
    c= float(a)*float(b)
    return c
#div
def ops_div(a,b):
    c= float(a)/float(b)
    return c
#mod
def ops_mod(a,b):
    c= float(a)%float(b)
    return c

#advance arithmetic operations
#exponentiation
def ops_raise(a,b):
    c=math.pow(float(a),float(b))
    #c="math.pow(" + a + "," + b + ")"
    return c
#nth root of a number
def ops_root(a,b):
    c= float(b)**(1/float(a))
    return c
#average
def ops_avg(all_num):
    avg = 0
    total_num = float(len(all_num))
    for num in all_num:
        avg = avg + num
    avg = avg/total_num
    return avg
#distance between two points
def ops_dist(a,b,c,d):
    result_ = ((( float(c)- float(a) )**2) + ((float(d)-float(b))**2) )**0.5
    return result_

#check data type
#check if ascii
def check_ascii(a):
    b = ascii(a)
    b = b[1:len(a)+1]
    #b = b.replace("\'","")
    if b== a and "\"" not in a:
        c = "True"
    else:
        c = "False"
    return c
#check if number
def check_num(a):
    try:
        test = int(a)
        b = "True"
    except Exception as e:
        b = "False"
    return b

#nested expressions
def nes_exp(a,var_name,dummy_bool,dummy_rec):
    
    if dummy_bool == "VAR":
        num_end = len(a)
        start_num = 3
        if dummy_rec == "True":
            lem_tok_temp = [start_process+1, "DECLARATION_INT","VARINT"]
            lem_tok.append(lem_tok_temp)
            lem_tok_temp = [start_process+1, 'IDENTIFIER',var_name]
            lem_tok.append(lem_tok_temp)
            lem_tok_temp = [start_process+1, 'DECLARATION_ASSIGN_WITH_KEY','WITH']
            lem_tok.append(lem_tok_temp)
    if dummy_bool == "PRINT":
        num_end = len(a)
        start_num = 1
        if dummy_rec == "True":
            lem_tok_temp = [start_process+1, "OUTPUT", dummy_bool]
            lem_tok.append(lem_tok_temp)
    if dummy_bool == "PRINTLN":
        num_end = len(a)
        start_num = 1
        if dummy_rec == "True":
            lem_tok_temp = [start_process+1, "OUTPUT_WITH_LINE", dummy_bool]
            lem_tok.append(lem_tok_temp)
    if dummy_bool == "OPS":
        num_end = len(a)
        start_num = 0

    #depends on the position
    #num_end = len(a)
    #start_num = 3

    nested_exp = ""
    fin_exp =""
    dummy_exp = []

    for exp in range(start_num,num_end):
        l = str(a[exp])
        #nested_exp = nested_exp + " " + l

        if l in var_int:
            #record in lemexes
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, 'IDENTIFIER',l]
                lem_tok.append(lem_tok_temp)
            #get position of variable
            var_pos = var_int.index(l)
            #get the value of variable
            l = str(var_int_values[var_pos])
        elif l in ops_basic: #basic operations
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, "BASIC_OPERATOR_" + l, l]
                lem_tok.append(lem_tok_temp)
        elif l in ops_adv: #advance operations
            if l == "RAISE":
                t = "EXP"
            if l == "MEAN":
                t = "AVE"
            if l == "DIST" or l == "ROOT":
                t = l
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, "ADVANCE_OPERATOR_" + t, l]
                lem_tok.append(lem_tok_temp)
        elif check_num(l) == "True":
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, "NUMBER", l]
                lem_tok.append(lem_tok_temp)
        elif l == "AND":
             if dummy_rec == "True":
                lem_tok_temp = [start_process+1, "DISTANCE_SEPARATOR", l]
                lem_tok.append(lem_tok_temp)
        
        nested_exp = nested_exp + " " + l
                                                        
    nested_exp = nested_exp.strip()
    for word in nested_exp.split():
        dummy_exp.append(word)

    num_end_2 = len(dummy_exp) - 1
    num_end_3 = num_end_2

    for num in range(num_end_2,-1,-1):
        #dummy_ops = dummy_exp[num]
        pos = int(dummy_exp.index(dummy_exp[num]))
        if check_num(dummy_exp[pos]) == "True":
            pass
        elif (dummy_exp[pos] in ops_basic or dummy_exp[pos] in ops):
            if dummy_exp[pos] == "DIST" and dummy_exp[pos+3] == "AND" :
                res = ops_dist(dummy_exp[num+1],dummy_exp[num+2],dummy_exp[num+4],dummy_exp[num+5])
                dummy_exp.remove(dummy_exp[pos])
                dummy_exp.insert(pos,res)
                dummy_exp.remove(dummy_exp[pos+1])
                dummy_exp.remove(dummy_exp[pos+1])
                dummy_exp.remove(dummy_exp[pos+1])
                dummy_exp.remove(dummy_exp[pos+1])
                dummy_exp.remove(dummy_exp[pos+1])
                num_end_3 = num_end_3 - 5
            elif dummy_exp[pos] == "MEAN":
                dummy_mean = []
                for a in range(len(dummy_exp)):
                    try:
                        w = a + pos
                        dummy_mean.append(int(dummy_exp[w]))
                    except Exception as e:
                            pass
                res = ops_avg(dummy_mean)
                dummy_exp.insert(pos,res)
                del dummy_exp[pos+1:int(len(dummy_exp))]
            else:
                if dummy_exp[pos] == "RAISE":
                    res = ops_raise(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "ROOT":
                    res = ops_root(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "MOD":
                    res = ops_mod(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "MUL":
                    res = ops_mul(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "DIV":
                    res = ops_div(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "ADD":
                    res = ops_add(dummy_exp[num+1],dummy_exp[num+2])
                if dummy_exp[pos] == "SUB":
                    res = ops_sub(dummy_exp[num+1],dummy_exp[num+2])
                dummy_exp.remove(dummy_exp[pos])
                dummy_exp.insert(pos,res)
                dummy_exp.remove(dummy_exp[pos+1])
                dummy_exp.remove(dummy_exp[pos+1])
                num_end_3 = num_end_3 - 2
    
    #print(dummy_exp)
    dummy_bool = 0
    for num_2 in dummy_exp:
            fin_exp = fin_exp + str(num_2)
            dummy_bool = dummy_bool+1
    if dummy_bool == 1:
        fin_exp = eval(fin_exp)
        fin_exp = round(fin_exp)
    else:
        fin_exp = "STOP"
    return fin_exp
#store variables
def store_var(a,b,type,dummy_bool,dummy_rec):
    if a in var_int and type == "INT":
        var_pos = var_int.index(a)
        if dummy_bool == "True":
            var_int_values[var_pos] = b
            sym_var_pos = sym_tbl.index([a,"INTEGER",""])
            sym_tbl[sym_var_pos][2] = b
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, 'ASSIGN_KEY', 'STORE']
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'NUMBER', b]
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'ASSIGN_VAR_KEY', 'IN']
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'IDENTIFIER', a]
                lem_tok.append(lem_tok_temp)
    elif a in var_str and type == "STR":
        var_pos = var_str.index(a)
        if dummy_bool == "True":
            var_str_values[var_pos] = b
            sym_var_pos = sym_tbl.index([a,"STRING",""])
            sym_tbl[sym_var_pos][2] = b
            if dummy_rec == "True":
                lem_tok_temp = [start_process+1, 'ASSIGN_KEY', 'STORE']
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'STRING', b]
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'ASSIGN_VAR_KEY', 'IN']
                lem_tok.append(lem_tok_temp)
                lem_tok_temp = [start_process+1, 'IDENTIFIER', a]
                lem_tok.append(lem_tok_temp)
    else:
        var_pos = "ñ"
    return var_pos
#declare variables
def dec_variable(var_typ,var_name,var_value,dummy_var):
    #creating and storing new variables
    if var_typ == "VARINT":
        var_int.append(var_name)
        var_int_values.append(var_value)
        dec = "DECLARATION_INT"
        dec_typ = "VARINT"
        typ = "INTEGER"
    if var_typ == "VARSTR":
        var_str.append(var_name)
        var_str_values.append(var_value)
        dec = "DECLARATION_STRING"
        dec_typ = "VARSTR"
        typ = "STRING"
    #lemexes and tokens
    #[LINE NO., TOKENS, LEMEXES]
    if var_value == "" and dummy_var == "True":
        lem_tok_temp = [start_process+1, dec,dec_typ]
        lem_tok.append(lem_tok_temp)
        lem_tok_temp = [start_process+1, 'IDENTIFIER',var_name]
        lem_tok.append(lem_tok_temp)
    if var_value != "" and dummy_var == "True":
        lem_tok_temp = [start_process+1, dec,dec_typ]
        lem_tok.append(lem_tok_temp)
        lem_tok_temp = [start_process+1, 'IDENTIFIER',var_name]
        lem_tok.append(lem_tok_temp)
        lem_tok_temp = [start_process+1, 'DECLARATION_ASSIGN_WITH_KEY','WITH']
        lem_tok.append(lem_tok_temp)
        lem_tok_temp = [start_process+1, typ, var_value]
        lem_tok.append(lem_tok_temp)
    #symbols table
    #[VARIABLE NAME, TYPE, VALUE]
    sym_tbl_temp =[var_name,typ,var_value]
    sym_tbl.append(sym_tbl_temp)
#get variables:
def get_variable(var_name):
    if var_name in var_int:
        var_pos = var_int.index(var_name)
        var_value = var_int_values[var_pos]
    elif var_name in var_str:
        var_pos = var_str.index(var_name)
        var_value = var_str_values[var_pos]
    else:
        var_value = "ñ"
    return var_value
#input variables
def input_var(a,b,dummy_rec):
    #a = str(input())
    if b in var_int and check_num(a) == "True":
        var_pos = ""
        if dummy_rec == "True":
            var_pos = var_int.index(b)
            old_value = var_int_values[var_pos]
            var_int_values[var_pos] = a
            sym_var_pos = sym_tbl.index([b,"INTEGER",old_value])
            sym_tbl[sym_var_pos][2] = a
            lem_tok_temp = [start_process+1, 'INPUT', 'INPUT']
            lem_tok.append(lem_tok_temp)
            lem_tok_temp = [start_process+1, 'IDENTIFIER', b]
            lem_tok.append(lem_tok_temp)
    elif b in var_str and check_ascii(a) == "True":
        var_pos = ""
        if dummy_rec == "True":
            var_pos = var_str.index(b)
            old_value = var_str_values[var_pos]
            var_str_values[var_pos] = a
            sym_var_pos = sym_tbl.index([b,"STRING",old_value])
            sym_tbl[sym_var_pos][2] = a
            lem_tok_temp = [start_process+1, 'INPUT', 'INPUT']
            lem_tok.append(lem_tok_temp)
            lem_tok_temp = [start_process+1, 'IDENTIFIER', b]
            lem_tok.append(lem_tok_temp)
    else:
        var_pos = "STOP"
    return var_pos
#print
def print_var(a,b,type,e,f,var_name):
    if type == "PRINT" and check_ascii(str(a)) == "True":
        #a = a
        c = ""
        d = ""
    elif type == "PRINTLN" and check_ascii(str(a)) == "True":
        a = str(a) + '\n'
        c = ""
        d = "_WITH_LINE"
    else:
        c = "STOP"
        d = ""
    
    if b == "True":
        print(a)
        if f == "True":
            lem_tok_temp = [start_process+1, "OUTPUT"+d, type]
            lem_tok.append(lem_tok_temp)
            if e == "STR":
                str_ = str(a).strip()
                lem_tok_temp = [start_process+1, "STRING", str_]
                lem_tok.append(lem_tok_temp)
            if e == "IDR":
                lem_tok_temp = [start_process+1, "IDENTIFIER", var_name]
                lem_tok.append(lem_tok_temp)
    return c
#end of statement
def eos():
    lem_tok_temp = [start_process+1, 'END_OF_STATEMENT', 'EOS']
    lem_tok.append(lem_tok_temp)

#main process
while True:
    #booleans and indexes
    bool_ext=""
    BEGIN_line_index = ""
    BEGIN_bool = 0
    END_line_index = ""
    END_bool = 0
    ipol_exp = []
    #integer variables
    var_int = []
    var_int_values = []
    #string variables
    var_str = []
    var_str_values = []
    #lemexes and tokens
    lem_tok = []
    lem_tok_temp = ['LINE NO.', 'TOKENS','LEMEXES']
    lem_tok.append(lem_tok_temp)
    lem_tok_temp = ['1', 'PROGRAM_BEGIN','BEGIN']
    lem_tok.append(lem_tok_temp)
    lem_tok_temp = ['1', 'END_OF_STATEMENT','EOS']
    lem_tok.append(lem_tok_temp)
    #symbol tables
    sym_tbl = []
    sym_tbl_temp = ['VARIABLE NAME', 'TYPE','VALUE']
    sym_tbl.append(sym_tbl_temp)

    #start
    print("\n\n========  INTERPOL INTERPRETER STARTED   ========\n")

    #input ipol file name
    ipol_filename = input("Enter INTERPOL file (.ipol): ")

    #output
    print("\n================ INTERPOL OUTPUT ================\n")
    print("----------------  OUTPUT START  ---------------->\n")

    #check if file is in .ipol format
    if ipol_filename.lower().endswith('.ipol'):
        #check if path exists
        if path.exists(ipol_filename):
            #open file
            open_file = open(ipol_filename, "r")
            #check if empty
            if os.stat(ipol_filename).st_size != 0:
                #read file
                file_lines = open_file.read().splitlines()
                #get the position of BEGIN and END
                for line_index, line in enumerate(file_lines):
                    words = line.split()
                    words=str(words)
                    if words == "['BEGIN']" and BEGIN_bool != 1:
                        BEGIN_line_index = line_index
                        BEGIN_bool = 1
                    elif words == "['END']" and END_bool != 1:
                        END_line_index = line_index
                        END_bool = 1
                #check if there's beginning and ending
                if BEGIN_line_index != "" and END_line_index != "":
                    #check if Begin comes before END
                    if BEGIN_line_index < END_line_index:
                        start_process = BEGIN_line_index + 1
                        for start_process in range(END_line_index):
                            word_line = file_lines[start_process]
                            word_line = word_line.strip()
                            if word_line != "BEGIN" and word_line!="":
                                #get number of words
                                try:
                                    num_of_words = len(word_line.split())
                                except ValueError:
                                    num_of_words = 1
                                
                                #comment
                                if word_line.startswith("#"):
                                    #lemexes and tokens
                                    #[LINE NO., TOKENS, LEMEXES]
                                    lem_tok_temp = [start_process+1, 'COMMENT',word_line]
                                    lem_tok.append(lem_tok_temp)
                                    eos()
                                    pass
                                elif num_of_words == 1:
                                    print("Invalid syntax at line number [ " + str(start_process + 1) + " ]")
                                    print (" ----> " + word_line)
                                    bool_ext = "1"
                                    break
                                else:
                                    for x in word_line.split():
                                        ipol_exp.append(x)
                                    
                                    if ipol_exp[0] in first_words:
                                        #input value in variables
                                        if ipol_exp[0] == "INPUT" and num_of_words == 2:
                                            var_name = ipol_exp[1]
                                            if var_name in var_int or var_name in var_str:
                                                try:
                                                    if var_name in var_int:# and input_var(int(input()),var_name,"") != "STOP":
                                                        input_val = int(input())
                                                        if str(input_val).strip() != "":
                                                            if check_num(input_val)=="True":
                                                                input_var(input_val,var_name,"True")
                                                                eos()
                                                            else:
                                                                print("Invalid data type input at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        else:
                                                                print("Invalid syntax at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                    elif var_name in var_str:# and input_var(str(input()),var_name,"") != "STOP":
                                                        input_val = str(input())
                                                        if str(input_val).strip() != "":
                                                            if check_ascii(input_val)=="True":
                                                                input_var(input_val,var_name,"True")
                                                                eos()
                                                            else:
                                                                print("Invalid data type input at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        else:
                                                                print("Invalid syntax at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                    else:
                                                        print("Invalid data type input at line number [ " + str(start_process + 1) + " ]")
                                                        print (" ----> " + word_line)
                                                        bool_ext = "1"
                                                        break
                                                except Exception as e:
                                                    print("Invalid data type input at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                            else:
                                                print("Variable is not declared at line number [ " + str(start_process + 1) + " ]")
                                                print (" ----> " + word_line)
                                                bool_ext = "1"
                                                break
                                        #storing
                                        elif ipol_exp[0] == "STORE":
                                            try:
                                                second_word = str(ipol_exp[1])
                                                sym_pos = int(ipol_exp.index("IN"))
                                                var_name = ipol_exp[sym_pos+1]
                                                if var_name == ipol_exp[-1]:
                                                    if var_name in var_int or var_name in var_str:
                                                    #STRING
                                                        if second_word.startswith("\""):
                                                            start_char = int(word_line.find('\"')+1)
                                                            end_char = int(word_line.rfind('\"'))
                                                            org_value = word_line[start_char:end_char]
                                                            if check_ascii(org_value) == "True":
                                                                if store_var(var_name, org_value, "STR","","") != "ñ" and start_char != end_char and "\"" not in org_value:
                                                                    store_var(var_name, org_value, "STR","True","True")
                                                                    eos()
                                                                else:
                                                                    print("Invalid data type at line number [ " + str(start_process + 1) + " ]")
                                                                    print (" ----> " + word_line)
                                                                    bool_ext = "1"
                                                                    break
                                                            else:
                                                                print("Invalid data type at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        #INTEGER
                                                        elif check_num(second_word) == "True" and num_of_words == 4:
                                                            if str(ipol_exp[2]) == "IN" and store_var(var_name, second_word, "INT","","") != "ñ" :
                                                                store_var(var_name, second_word, "INT","True","True")
                                                                eos()
                                                            else:
                                                                print("Invalid data type at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        #OPERATIONS
                                                        elif second_word in ops:
                                                            org_value = ipol_exp[1:sym_pos]
                                                            if nes_exp(org_value,"","OPS","") != "STOP":
                                                                lem_tok_temp = [start_process+1, 'ASSIGN_KEY', 'STORE']
                                                                lem_tok.append(lem_tok_temp)
                                                                store_var(var_name, nes_exp(org_value,"","OPS","True"), "INT","True","")
                                                                lem_tok_temp = [start_process+1, 'ASSIGN_VAR_KEY', 'IN']
                                                                lem_tok.append(lem_tok_temp)
                                                                lem_tok_temp = [start_process+1, 'IDENTIFIER', var_name]
                                                                lem_tok.append(lem_tok_temp)
                                                                eos()
                                                            else:
                                                                print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        else:
                                                            print("Invalid data type at line number [ " + str(start_process + 1) + " ]")
                                                            print (" ----> " + word_line)
                                                            bool_ext = "1"
                                                            break
                                                    else:
                                                        print("Variable is not declared at line number [ " + str(start_process + 1) + " ]")
                                                        print (" ----> " + word_line)
                                                        bool_ext = "1"
                                                        break
                                                else:
                                                    print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                            except Exception as e:
                                                print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                print (" ----> " + word_line)
                                                bool_ext = "1"
                                                break
                                        #declaring variables
                                        elif ipol_exp[0] in dec_var:
                                            if ipol_exp[1] not in var_int and ipol_exp[1] not in var_str:
                                                var_name = ipol_exp[1]
                                                if var_name not in reserved_words and str(var_name).upper() not in reserved_words and len(var_name)<= 50 and var_name.isalpha() == True:
                                                    if num_of_words == 2:
                                                        dec_variable(ipol_exp[0],var_name,"","True")
                                                        eos()
                                                    elif num_of_words >= 4 and ipol_exp[2] == "WITH":
                                                        fourth_word = str(ipol_exp[3])
                                                        default_bool = str(check_num(ipol_exp[3]))
                                                        if ipol_exp[0] == "VARINT" and default_bool == "True" and num_of_words == 4:
                                                            dec_variable(ipol_exp[0],var_name,ipol_exp[3],"True")
                                                            eos()
                                                        elif ipol_exp[0] == "VARINT" and num_of_words > 4 and fourth_word in ops:
                                                            try:
                                                                dec_variable(ipol_exp[0],var_name, nes_exp(ipol_exp,var_name,"VAR","True"),"False")
                                                                b = nes_exp(ipol_exp,var_name,"VAR","")
                                                                if b != "STOP":
                                                                    eos()
                                                                else:
                                                                    print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                                    print (" ----> " + word_line)
                                                                    bool_ext = "1"
                                                                    break
                                                            except Exception as e:
                                                                print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        elif ipol_exp[0] =="VARSTR" and fourth_word.startswith("\""):
                                                            start_char = int(word_line.find('\"')+1)
                                                            end_char = int(word_line.rfind('\"'))
                                                            org_value = word_line[start_char:end_char]
                                                            if check_ascii(org_value) == "True" and start_char != end_char and end_char + 1 == len(word_line) and "\"" not in org_value:
                                                                dec_variable(ipol_exp[0],var_name,org_value,"True")
                                                                eos()
                                                            else:
                                                                print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                                print (" ----> " + word_line)
                                                                bool_ext = "1"
                                                                break
                                                        else:
                                                            print("Invalid data type at line number [ " + str(start_process + 1) + " ]")
                                                            print (" ----> " + word_line)
                                                            bool_ext = "1"
                                                            break
                                                    else:
                                                        print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                        print (" ----> " + word_line)
                                                        bool_ext = "1"
                                                        break
                                                else:
                                                    print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                            else:
                                                print("Duplicate variable declaration at line number [ " + str(start_process + 1) + " ]")
                                                print (" ----> " + word_line)
                                                bool_ext = "1"
                                                break
                                        #print
                                        elif ipol_exp[0] in ipol_print:
                                            second_word = str(ipol_exp[1])
                                            if second_word.startswith("\""):
                                                start_char = int(word_line.find('\"')+1)
                                                end_char = int(word_line.rfind('\"'))
                                                org_value = word_line[start_char:end_char]
                                                df = print_var(org_value,"",ipol_exp[0],"STR","","")
                                                if df != "STOP" and start_char != end_char and end_char + 1 == len(word_line) and "\"" not in org_value:
                                                    print_var(org_value,"True",ipol_exp[0],"STR","True","")
                                                    eos()
                                                else:
                                                    print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                            elif (second_word in var_int or second_word in var_str) and ipol_exp[-1] == second_word:
                                                if get_variable(second_word) != "ñ":
                                                    print_var(get_variable(second_word),"True",ipol_exp[0],"IDR","True",second_word)
                                                    eos()
                                                else:
                                                    print("Variable is not declared at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                            elif second_word in ops:
                                                try:
                                                    b = nes_exp(ipol_exp,"",ipol_exp[0],"")
                                                    if b != "STOP":
                                                        print_var(nes_exp(ipol_exp,"",ipol_exp[0],"True"),"True",ipol_exp[0],"","","")
                                                        eos()
                                                    else:
                                                        print("Invalid arithmetic operation at line number [ " + str(start_process + 1) + " ]")
                                                        print (" ----> " + word_line)
                                                        bool_ext = "1"
                                                        break
                                                except Exception as e:
                                                    print("Invalid arithmetic operation at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break

                                            else:
                                                    print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                                    print (" ----> " + word_line)
                                                    bool_ext = "1"
                                                    break
                                        #operations
                                        elif ipol_exp[0] in ops:
                                            try:
                                                nes_exp(ipol_exp,"","OPS","True")
                                                eos()
                                            except Exception as e:
                                                print("Invalid arithmetic operation at line number [ " + str(start_process + 1) + " ]")
                                                print (" ----> " + word_line)
                                                bool_ext = "1"
                                                break
                                        else:
                                            print("Invalid expression at line number [ " + str(start_process + 1) + " ]")
                                            print (" ----> " + word_line)
                                            bool_ext = "1"
                                            break
                                        ipol_exp = []
                                    else:
                                        print("Invalid syntax at line number [ " + str(start_process + 1) + " ]")
                                        print (" ----> " + word_line)
                                        bool_ext = "1"
                                        break
                elif BEGIN_line_index == "": #invalid start
                    ipol_output = "Invalid start of file"
                    print(ipol_output)
                    bool_ext = "1"
                    break
                elif END_line_index == "": #invalid end
                    ipol_output = "Invalid end of file"
                    print(ipol_output)
                    bool_ext = "1"
                    break
                else: #invalid end and start
                    ipol_output = "Invalid end of file"
                    print(ipol_output)
                    bool_ext = "1"
                    break
            else: #file is empty
                ipol_output = "File is empty"
                print(ipol_output)
                bool_ext = "1"
                break
        else: #file not found
            ipol_output = "File not found"
            print(ipol_output)
            bool_ext = "1"
            break
    else: #invalid file
        ipol_output= "Invalid file"
        print(ipol_output)
        bool_ext = "1"
        break

#print output
    if bool_ext!= "1":
        print("\n<----------------- OUTPUT END -------------------\n")
        print("========= INTERPOL LEXEMES/TOKENS TABLE =========\n")
        lem_tok_temp = [END_line_index+1, 'PROGRAM_END','END']
        lem_tok.append(lem_tok_temp)
        lem_tok_temp = [END_line_index+2, 'END_OF_FILE','EOF']
        lem_tok.append(lem_tok_temp)
        #print(lem_tok)
        s = [[str(e) for e in row] for row in lem_tok]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
        print("\n================= SYMBOLS TABLE =================\n")
        #print(sym_tbl)

        s = [[str(e) for e in row] for row in sym_tbl]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))

        print("\n======== INTERPOL INTERPRETER TERMINATED ========")
    break
    