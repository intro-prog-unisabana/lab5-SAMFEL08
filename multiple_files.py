import utils

msj = input("Please type your message\n")
flipped = utils.flip(msj)
count_a = utils.count_letters(msj, letter='a')

print(f"Your encoded message is: {flipped}{count_a}")