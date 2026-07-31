class Car: # Car class: stores the car number and the number of votes
    def __init__(self, num, votes):
        self.num = num
        self.votes = votes

def green():
    print("\033[92m")

def white():
    print("\033[0m")

def removeLastLine():
    print("\033[A\033[G\033[2K", end='')

def sortByMostVotes(carObjList):
    sortedObjList = []
    maxVotesRemaining = 0
    maxVotesRemainingIndex = 0
    while len(carObjList) > 0:
        for k in range(len(carObjList)):
            if carObjList[k].votes > maxVotesRemaining:
                maxVotesRemainingIndex = k
                maxVotesRemaining = carObjList[k].votes
        sortedObjList.append(carObjList[maxVotesRemainingIndex])
        carObjList.pop(maxVotesRemainingIndex)
        maxVotesRemaining = 0
        maxVotesRemainingIndex = 0
    return sortedObjList

def printResults(sortedCars, takeTop):
    print("\n|----------------------------|")
    print("|        Final Results       |")
    print("|----------------------------|\n")
    for i in range(takeTop):
        if sortedCars[i].num >= 100:
            print(f"Car Number: {sortedCars[i].num} | Votes: {sortedCars[i].votes} | Rank: {i + 1}")
        elif sortedCars[i].num >= 10:
            print(f"Car Number: {sortedCars[i].num}  | Votes: {sortedCars[i].votes} | Rank: {i + 1}")
        else:
            print(f"Car Number: {sortedCars[i].num}   | Votes: {sortedCars[i].votes} | Rank: {i + 1}")

def exportResults(sortedCars):
    with open("results.txt", "w") as f:
        f.write("|----------------------------|\n")
        f.write("|        Final Results       |\n")
        f.write("|----------------------------|\n\n")
        for i in range(len(sortedCars)):
            if sortedCars[i].num >= 100:
                f.write(f"Car Number: {sortedCars[i].num} | Votes: {sortedCars[i].votes} | Rank: {i + 1}\n")
            elif sortedCars[i].num >= 10:
                f.write(f"Car Number: {sortedCars[i].num}  | Votes: {sortedCars[i].votes} | Rank: {i + 1}\n")
            else:
                f.write(f"Car Number: {sortedCars[i].num}   | Votes: {sortedCars[i].votes} | Rank: {i + 1}\n")

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
            contToResults = True
            break
        # check Bounds of the number entered
        if nextNumber == "" or not nextNumber.isdigit() or int(nextNumber) < 1 or int(nextNumber) > totalCars:
            invalidNumber = True
            while invalidNumber:
                nextNumber = input("Car Number Not in Bounds, Enter Again (Type Results for Results): ")
                if nextNumber == "Results":
                    invalidNumber = False
                    contToResults = True
                    break
                if nextNumber != "" and nextNumber.isdigit() and int(nextNumber) > 0 and int(nextNumber) <= totalCars:
                    invalidNumber = False
                    break
                removeLastLine()
            
        removeLastLine()
        # code to increase vote number
        if not contToResults:
            carObj = carObjList[int(nextNumber) - 1]
            carObj.votes += 1


    sortedCars = sortByMostVotes(carObjList)
    takeTop = input(f"How many of the top cars would you like to see? (1-{totalCars}): ")
    while True:
        if not takeTop.isdigit() or int(takeTop) < 1 or int(takeTop) > totalCars:
            removeLastLine()
            takeTop = input(f"Invalid Number, Please Enter a number between 1 and {totalCars}: ")
        else:
            break
    printResults(sortedCars, int(takeTop))

    while True:
        export = input("Would you like to export the results to a text file? (Y/N): ")
        if export == "Y" or export == "y":
            exportResults(sortedCars)
            print("Results exported to results.txt")
            break
        elif export == "N" or export == "n":
            break
        else:
            removeLastLine()
            print("Invalid Input, Please Enter Y or N")
            removeLastLine()

    white()
    exit(0)

main()  # Call the Main Function