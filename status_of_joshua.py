import random

def main():
    
    
    while True:
        print('')
        status_of_joshua = random.randint(1,7)
        if status_of_joshua == 1:
            print("Josh is a giant poopyhead.")
        elif status_of_joshua == 2:
            print("Josh is a stoopidface. A big ol' Silly Sandra.")
        elif status_of_joshua == 3:
            print("Josh is a goofy guy. What a goof ball!")
        elif status_of_joshua == 4:
            print("Josh is one of the wackiest people ever. Zany, even!")
        elif status_of_joshua == 5:
            print("'Hey Bob how's it goin.?' 'Oh it's goin' alright, Jim. Hey you know that Josh character by chance, Bobby, ol' boy?' 'Why, yes I do, in fact! He is quite the character!' 'Indeed, indeed!' *chortle chuckle chortle*")
        elif status_of_joshua == 6:
            print("I believe Josh was awarded goofiest man in all of Collinsville in 2020. Don't quote me but I think thats correct!")
        elif status_of_joshua == 7:
            print("My back hurts from moving that piano.")
        else:
            print("An error occured. Josh is a fool.")
            
        x = input("\nWould you like to check the status of Josh? Please type yes or no, then press enter. ")
        if x == ("no"):
            print("\nJust kidding, that guy's alright. So are David, Mom, and Dad, I guess <3.")
            break
            

main()
