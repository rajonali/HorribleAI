import os

def __main__():
    greetings = "Good morning Tasnim Ali"
    os.system("espeak -ven-us+f3 --stdout '%s' -a 300 -s 130 | aplay" % greetings)




