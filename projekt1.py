"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jiří Bernas
email: jiri.bernas@nacr.cz
discord: jirka B.#0164
"""

from task_template import TEXTS as text

users = {
    'bob':'123',
    'ann':'pass123',
    'mike':'password123',
    'liz':'pass123',
}

userName = input("Zadej uživatelské jméno: ")
userPassword = input("Zadej heslo: ")

if userPassword == users[userName]:
    print ("Vítej uživateli",userName)
    print ("V nabídce jsou tři texty, které je možno analyzovat. texty jsou očíslovány od 1 do 3")
    textNumber = input ("Zadej prosím číslo textu, který chceš analyzovat:")
    
    if textNumber.isnumeric():
        intNumber=int(textNumber)-1
        if intNumber in range(0,3):
            selectedText=text[intNumber]
            numberWords=0
            numberFirstUp=0
            numberAllUp=0
            numberAllLow=0
            numberNumbers=0
            sumNumbers=0
            
            selectedText=selectedText.strip()
            selectedText=selectedText.replace("\n"," ")
            words=selectedText.split(" ")
            
            numberWords=len(words)
            
            statistic=dict()
            maxNumber=0;
            
            for word in words:
                word=word.strip(".,")
                lenghtWord=len(word)
                
                if lenghtWord in statistic:
                    statistic[lenghtWord] += 1
                else:
                    statistic[lenghtWord]=1
                
                if statistic[lenghtWord]>maxNumber:
                    maxNumber=statistic[lenghtWord]
                
                if word.isupper():
                    numberAllUp += 1
                if word[0].isupper():
                    numberFirstUp += 1
                if word.isnumeric():
                    numberNumbers += 1
                    sumNumbers += int(word)
                if word.islower():
                    numberAllLow += 1
            
            titleLenght=40
            title="STATISTIKA TEXTU "+textNumber
            print(titleLenght*"-")
            print(title.center(titleLenght))
            print("Počet slov:",numberWords)
            print("Počet slov s prvním velkým písmenem:",numberFirstUp)
            print("Počet slov psaných velkými písmeny:",numberAllUp)
            print("Počet slov psaných malými písmeny:",numberAllLow)
            print("Počet čísel:",numberNumbers)
            print("Součet čísel:",sumNumbers)
            
            print(titleLenght*"-")
            
            title="STATISTIKA POČTU SLOV TEXTU "+textNumber

            print(title.center(titleLenght))

            title1="počet znaků"
            title2="počet slov"
            title1Lenght=len(title1)
            title2Lenght=len(title2)
            
            if maxNumber>title2Lenght:
                title2Lenght=maxNumber
            
            partialText=(title1Lenght+5+title2Lenght+5)*"-"
            print(partialText.center(titleLenght))
            
            partialText="| "+title1+" | "+title2.center(title2Lenght+3)+" |"
            print(partialText.center(titleLenght))
            
            partialText=(title1Lenght+5+title2Lenght+5)*"-"
            print(partialText.center(titleLenght))
            
            for key,value in sorted(statistic.items()):
                valueString=value*"*"+" "+str(value)
                partialText=("| "+str(key).rjust(title1Lenght)+" | "+valueString.ljust(title2Lenght+3)+" |")
                print(partialText.center(titleLenght))

            partialText=((title1Lenght+5+title2Lenght+5)*"-")
            print(partialText.center(titleLenght))
            
        else:
            print("Text s číslem",textNumber,"neexistuje.")
    else:
        print("Nebylo zadáno číslo.")
else:
    print ("Neplatné uživatelské jméno nebo heslo.")

