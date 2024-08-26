from random import randint

a = -1
guesses = 1
n = randint(89,999)

while(a != n):

    a =int(input( "Guess the number:"))
    if(a > n):
        print("Guess Lower Number !") 
        guesses +=1
    elif(a < n):
        print("Guess Higher Number !")
        guesses +=1

print(f"You have guesses the number {n} is correctly in {guesses} attempts")        


      
