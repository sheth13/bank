#-------------------- layout functions -----------------------------#
from formatting import *
import os


#-------------------------------  Main page -----------------------------------#
def main1():
    os.system('clear')
    header(50)
    heading(50,"Sheth's bank")
    header(50)
    Newline()
    Newline()
    content("1. Login")
    content("2. Register for our bank")
    content("3. Exit")
    Newline()
    Newline()
    header(50)
    choose = int(input("choose > "))
    return choose


#-------------------------------- Registration main page ----------------------#
def reg():

    os.system('clear')
    header(50)
    heading(50,"Registration")
    header(50)
    Newline()
    Newline()
    content("1. Admin Regestration")
    content("2. User Regestration")
    content("3. Back")
    Newline()
    Newline()
    header(50)
    choose_reg = int(input("choose > "))
    return choose_reg
#-------------------------------- Admin Reg Page ------------------------------#
def admin_reg():
    os.system('clear')
    header(50)
    heading(50,"Enter Details For Registration")
    header(50)
    Newline()
    Newline()
    name = get_name()
    Newline()
    city = get_city()
    Newline()
    state = get_state()
    Newline()
    phn  =  get_phn()
    Newline()
    pw = get_pw()
    Newline()

#--------------------------- User Reg Page ------------------------------------#
def user_reg():
    os.system('clear')
    header(50)
    heading(50,"Enter Details For Registration")
    header(50)
    Newline()
    Newline()
    name = get_name()
    Newline()
    city = get_city()
    Newline()
    state = get_state()
    Newline()
    phn  =  get_phn()
    Newline()
    pw = get_pw()
    Newline()
