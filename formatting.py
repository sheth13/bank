#------------------------------- headder padding ------------------------------#
def header(size):
    va='*'
    for value in range(size):
        new = va * value
        pass
    print(new)
    pass

#-----------------------------------bank heading with padding -----------------#
def heading(size,head_str):
    head = head_str.center(size," ")
    print(head)
    pass

#------------------------------------ new line function -----------------------#
def Newline():
    print()
    pass

#------------------------------------main content of page ---------------------#
def content(str):
    con = str
    print("     "+con)

#------------------------------------------------------------------------------#
def get_name():
    temp = str(input("      Name : "))
    return temp

#------------------------------------------------------------------------------#
def get_city():
    temp = str(input("      City : "))
    return temp
#------------------------------------------------------------------------------#
def get_state():
    temp = str(input("      State : "))
    return temp

#------------------------------------------------------------------------------#
def get_phn():
    temp = int(input("      Phone : "))
    return temp

#------------------------------------------------------------------------------#
def get_pw():
    temp = str(input("      Password : "))
    return temp

#------------------------------------------------------------------------------#    
