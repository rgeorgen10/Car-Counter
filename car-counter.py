class Car: # Car class: stores the car number and the number of votes
    def __init__(self, num, votes):
        self.num = num
        self.votes = votes

def green():
    print("\033[32m")

def white():
    print("\033[0m")

def removeLastLine():
    print("\e[F")

def main():   # The Main Function: Where the program is mainly operated
    green()
    print("|----------------------------|")
    print("| Welcome To The Car Counter |")
    print("|----------------------------|\n")
    
    totalCars = int(input("Enter The number of cars to count (Make Sure it's at the least the number of cars in the show: "))

    carObjList = []
    for i in range(totalCars):     # This loop creates all of the car objects and puts them in the carObjList
        newObj = Car(i+1, 0)
        carObjList.append(newObj)
    
    contToResults = False
    while contToResults == False:  # While the user hasn't requested final results, continue prompting for voting numbers
        nextNumber = input("Type the number of the next car voted on (Type Results for Final Results): ")  # Prompt for next car number
        if nextNumber == "Results":
            break

        # check Bounds of the number entered
        if nextNumber < 0 or nextNumber > totalCars:
            removeLastLine();
            

    
    white()
    exit(0)

main()  # Call the Main Function