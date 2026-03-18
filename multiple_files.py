import utils
msj=input("Please type your message\n")
print(f"Your encoded message is: {utils.flip(msj)}{utils.count_letters(msj, letter="a")}")