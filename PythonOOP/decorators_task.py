# task - create a function do display the current time. (je na to knihovna day time - viz chat GPT)
# the function takes no parameters.
# Decorate the function using another function without decorator syntax, Possible output:

"""
******************************
15:25
******************************
"""
# ty hvezdicky budou jako decorator a cas mezi to vlozeny

import datetime


def my_current_time():

    print(datetime.datetime.now().strftime("%H:%M"))


def stars(myFunction):
     def simpleWrapper():
         print("*****************************")
         myFunction()
         print("*****************************")


     return simpleWrapper


current_time = stars(my_current_time)
current_time()