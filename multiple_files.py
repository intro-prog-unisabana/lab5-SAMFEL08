from utils import *
mensaje= input("Please type your message\n")
inmensaje= flip(mensaje)
a= count_letters(mensaje, "a")
print(f"Your encoded message is: {inmensaje}{a}")