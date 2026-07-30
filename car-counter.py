class Car: # Car class: stores the car number and the number of votes
    def __init__(self, num, votes):
        self.num = num
        self.votes = votes

def green():
    print("\033[32m")

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

def printResults(sortedCars):
    print("\n|----------------------------|")
    print("|        Final Results       |")
    print("|----------------------------|\n")
    for i in range(len(sortedCars)):
        if sortedCars[i].num >= 100:
            print(f"Car Number: {sortedCars[i].num} | Votes: {sortedCars[i].votes}")
        elif sortedCars[i].num >= 10:
            print(f"Car Number: {sortedCars[i].num}  | Votes: {sortedCars[i].votes}")
        else:
            print(f"Car Number: {sortedCars[i].num}   | Votes: {sortedCars[i].votes}")

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
        while nextNumber == "" or not nextNumber.isdigit() or int(nextNumber) < 1 or int(nextNumber) > totalCars:
            nextNumber = input("Car Number Not in Bounds, Enter Again (Type Results for Results): ")
        removeLastLine()
        if nextNumber == "Results": # put this after the bounds check to avoid errors if the user types "Results" when prompted for a car number
            break
        # code to increase vote number
        carObj = carObjList[int(nextNumber) - 1]
        carObj.votes += 1

    sortedCars = sortByMostVotes(carObjList)
    printResults(sortedCars)

    white()
    exit(0)

main()  # Call the Main Function