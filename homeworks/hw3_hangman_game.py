import random

words = ["python","algorithm","statement","reflection","community",
         "enthusiasm","recommendation","administration","possibility",
         "assessment","assignment","cognitive","recognition","satisfaction",
         "subscription","artificial","engineering","atmosphere","collaboration"]

draw =['''
____
    |
    |
    |
    |''','''
____
    |
 O  |
    |
    |''','''
____
    |
 O  |
 |  |
    |''','''
____
    |
 O  |
/|  |
    |''','''
____
    |
 O  |
/|\ |
    |''','''
____
    |
 O  |
/|\ |
/   |''','''
____
    |
 O  |
/|\ |
/ \ |''','''
____
 |  |   
 O  |
/|\ |
/ \ |''']

name = input("Hey! Who are you?: ")
print("Welcome",name,",","Let's begin!")

word = random.choice(words)
guess = ""
right = 7
draw_count = 1
print(draw[0])

while(1):
    
    if right == 0:
        print("\nYou have no right anymore. Game Over!")
        break
    count = 0
    
    for i in word:
        if i in guess:
            print(i,end="")
        else:
            print("_",end="")
            count += 1
    
    if count == 0:
        print("\nYou won!")
        break
    
    letter = input("\nEnter a letter: ")
    
    if len(letter) != 1:
        print("Please enter only one character.")
    else:
        guess += letter
        if letter not in word:
            print(draw[draw_count])
            draw_count += 1
            print("Try again. You have",right,"more rights to find.")
            right -= 1

print("The correct word:",word)
