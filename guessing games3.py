#!/usr/bin/env python

import random

def main():
    """Start a number guessing type of popular game begin with alphabet b"""
    print ("SELAMAT DATANG KE KUIZ TEKA SUKAN !")

    games = [ 
        "badminton", 
        "bola sepak", 
        "bola tampar", 
        "bola jaring", 
        "boling padang"
    ]  
    x =random.choice(games)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("Apakah pemainan kesukaan orang ramai bermula dengan huruf B: "))
        
        if x == guess:
            print("Tahniah, tekaan anda betul!" (guess))
            break
        else:
            print("Maaf jawapan anda salah.".format(guess))
            print("Anda ada 2 lagi peluang" {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print("Jawapan yang tepat adalah {x}")
        
main()