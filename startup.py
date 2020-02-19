#-----------------python bank management project ------------------------------#
from layout import *
import os
import time



x=1                      #--------------- temp variable for infinite while loop



while(x):

    #------------------------- Main while loop--------------------#

    status = main1()

    if status == 3:

        os.system('clear')
        break

    elif status == 1:

        print("login")
        time.sleep(3)

    elif status  == 2:

        while(x):

            reg_status = reg()
            if reg_status == 1:

                admin_reg()
                time.sleep(3)

            elif reg_status == 2:

                user_reg()
                time.sleep(3)

            elif reg_status == 3:

                print("back to main menu")
                break
                time.sleep(3)

            else:

                print("Wrong choice")
                time.sleep(3)

        time.sleep(3)
    else:
        print("wrong choice")
        time.sleep(3)
