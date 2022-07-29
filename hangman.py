import random
print("******* Welcome to Hangman Game ********")
name=input("Enter Your Name : ")
print(f"***** Hello {name} welcome to this Game *****")
def hangman():
        words=["funny","lucky","oxygen","pixel","cycle","puppy","icebox","avenue"]
        ch_word=random.choice(words)
        if ch_word=="funny":
            print("F _ _ N _ ")
            a=input("Enter The first Vacant Letter : ")
            b=input("Enter The Second Vacant Letter : ")
            c=input("Enter The Third Vacant Letter : ")
            if a=="u" or a=="U" and b=="n" or b=="N" and c=="y" or c=="Y":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="lucky":
            print("L _ _ K _ ")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "u" or a == "U" and b == "c" or b == "C" and c == "y" or c == "Y":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="oxygen":
            print("O _ _ G _ N")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "x" or a == "X" and b == "y" or b == "Y" and c == "e" or c == "E":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="pixel":
            print("P _ _ E _ ")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "i" or a == "I" and b == "x" or b == "X" and c == "l" or c == "L":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="cycle":
            print("C _ _ L _ ")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "y" or a == "Y" and b == "c" or b == "C" and c == "e" or c == "E":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="puppy":
            print("P _ _ P _ ")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "u" or a == "U" and b == "p" or b == "P" and c == "y" or c == "Y":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="icebox":
            print("I _ _ B _ X")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "c" or a == "C" and b == "e" or b == "E" and c == "o" or c == "O":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")
        elif ch_word=="avenue":
            print("A _ _ N _ E")
            a = input("Enter The first Vacant Letter : ")
            b = input("Enter The Second Vacant Letter : ")
            c = input("Enter The Third Vacant Letter : ")
            if a == "v" or a == "V" and b == "e" or b == "E" and c == "u" or c == "U":
                print("Hurray ! You have Guessed Correct Word ")
            else:
                print("Better luck next Time")

hangman()
while True:
    print("Do you want to Play again : Y/N ")
    op=input("Enter Your Choice : ")
    if op=="Y" or op=="y":
        hangman()
    else:
        print("Thank You ! ")
        break