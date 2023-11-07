import os
import time

def menu():
    mainChoice = 0
    inChoice = 0
    gotoMenu = 0

    print("\t\t      * FiveStar *\n")
    print("----------------------- Main Menu --------------------------\n")
    print("\t * * * * * * * * * * * * * * * * * * * * ")
    print("\t*\t\t\t\t\t*")
    print("\t*\tCustomer Management  -> 1\t*")
    print("\t*\tPurchased Management -> 2\t*")
    print("\t*\tCharges & Bill       -> 3\t*")
    print("\t*\tPersonal Trainers    -> 4\t*")
    print("\t*\tExit                 -> 5\t*")
    print("\t*\t\t\t\t\t*")
    print("\t * * * * * * * * * * * * * * * * * * * * ")

    mainChoice = int(input("\nEnter Your Choice: "))
    os.system("CLS")

    a3 = Customer()
    a4 = Purchase()
    a5 = Chargers()

    if mainChoice == 1:
        print("------Customers------\n")
        print("1. Register a New Customer")
        print("2. See Previous Customers")
        inChoice = int(input("\nEnter Your choice: "))
        os.system("CLS")

        if inChoice == 1:
            a3.getDetails()
        elif inChoice == 2:
            a3.showDetails()
        else:
            print("Something went wrong! Redirecting back to Previous Menu\nPlease Wait!")
            time.sleep(1.1)
            os.system("CLS")
            menu()
        
        gotoMenu = int(input("Press 1 to Redirect back Main Menu: "))
        os.system("CLS")
        if gotoMenu == 1:
            menu()
        else:
            menu()
    elif mainChoice == 2:
        print("--> Purchase a Fitness 1<--\n")
        a4.fitness()
    elif mainChoice == 3:
        print("-->Get your Payment<--\n")
        a5.printBill()
        print("Your payment is already printed.")
        print("Show your payment by pressing 1(Press another key to go back to the main menu): ")
        gotoMenu = int(input())
        if gotoMenu == 1:
            os.system("CLS")
            a5.showBill()
            print("Press 1 to Redirect back Main Menu: ")
            gotoMenu = int(input())
            os.system("CLS")
            if gotoMenu == 1:
                menu()
            else:
                menu()
        else:
            os.system("CLS")
            menu()
    elif mainChoice == 4:
        print(" -->Personal Trainers<--\n")
        print("#1 - Ross Dickerson --> 500 Euro per Month, | Tel.Number = 0697766215")
        print("#2 - Justin Gelband --> 400 Euro per Month, | Tel.Number = 0694574122")
        print("#3 - Nick Mitchelle --> 320 Euro per Month, | Tel.Number = 0684523655")
        print("#4 - Aaron Williams --> 250 Euro per Month, | Tel.Number = 0695784559")
        print("\n")
        print("Press 1 to Redirect back Main Menu: ")
        gotoMenu = int(input())
        os.system("CLS")
        if gotoMenu == 1:
            menu()
        else:
            menu()
    elif mainChoice == 5:
        print("\n\n\t--GOOD BYE! Have a great time!--")
        time.sleep(1.1)
        os.system("CLS")
        ManageMenu()
    else:
        print("Something went wrong! Redirecting back to Previous Menu\nPlease Wait!")
        time.sleep(1.1)
        os.system("CLS")
        menu()

class ManageMenu:
    def __init__(self):
        os.system("color 0B")
        self.userName = input("\n\n\n\n\n\tPlease, Enter Your Name to Continue as Admin: ")
        os.system("CLS")
        menu()

class Customer:
    custID = 0

    def __init__(self):
        self.name = ""
        self.surname = ""
        self.gender = ""
        self.eaddress = ""
        self.age = 0
        self.mobileNum = 0
        self.menuBack = 0

    def getDetails(self):
        with open("previous-customers.txt", "a") as out:
            Customer.custID = int(input("Please, Enter Customer ID: "))
            self.name = input("Please, Enter Name: ")
            self.surname = input("Please, Enter Surname: ")
            self.age = int(input("Please, Enter Age: "))
            self.eaddress = input("Please, Enter Email Address: ")
            self.mobileNum = int(input("Please, Enter Mobile Number: "))
            self.gender = input("Please, Enter Gender: ")

            out.write(f"Customer ID: {Customer.custID}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nEmail Address: {self.eaddress}\nMobile Number: {self.mobileNum}\nGender: {self.gender}\n")
        print("\n** Your details have been saved successfully **\n")

    def showDetails(self):
        with open("previous-customers.txt", "r") as on:
            if not on:
                print("File Error!")
            for line in on:
                print(line)

class Purchase:
    fitnessCost = 0.0

    def __init__(self):
        self.choiceFitness = 0
        self.packChoice1 = 0
        self.gotoMenu = 0

    def fitness(self):
        fitnessNo = ["Fitness 1 (5 star)", "Fitness 2 (6 star)", "Fitness 3", "Fitness 4"]
        for a, fitness in enumerate(fitnessNo):
            print(f"{a + 1}. {fitness}")

        print("\nCurrently we own the aforementioned fitness!")

        self.choiceFitness = int(input("\nPlease, Enter number of the fitness you want to see the details (Press any key to get back): "))
        os.system("CLS")

        if self.choiceFitness == 1:
            print("\t\t********** WELCOME TO Fitness 1 (5 star) **********\n")
            print("----------- | Bathroom | Free Wifi | Restaurants | Proteins | -----------.")
            print("\nPackages for Fitness 1:\n")
            print("1. Basic Pack")
            print("\tHave a good training with the basic pack only for: 40 Euro")
            print("2. Regular Pack")
            print("\tHave an excellent training with the regular pack only for: 55 Euro")
            print("3. Premium Pack")
            print("\tYou will have a trainer for only: 75 Euro")

            self.packChoice1 = int(input("\nEnter Package number you want to see (Press any key to get back): "))

            if self.packChoice1 == 1:
                Purchase.fitnessCost = 40
                print("\nYou have successfully purchased Basic Pack at Fitness 1 (5 Star)")
                print("Go to Menu and there you can take the payment receipt")
            elif self.packChoice1 == 2:
                Purchase.fitnessCost = 55
                print("\nYou have successfully purchased Regular Pack at Fitness 1 (5 Star)")
                print("Go to Menu and there you can take the payment receipt")
            elif self.packChoice1 == 3:
                Purchase.fitnessCost = 75
                print("\nYou have successfully purchased Premium Pack at Fitness 1 (5 Star)")
                print("Go to Menu and there you can take the payment receipt")
            else:
                print("Something went wrong! Redirecting back to the Previous Menu\nPlease Wait!")
                time.sleep(1.1)
                os.system("CLS")
                self.fitness()

            self.gotoMenu = int(input("\nPress 1 to Redirect back to Main Menu: "))
            os.system("CLS")
            if self.gotoMenu == 1:
                menu()
            else:
                menu()
        elif self.choiceFitness == 3:
            print("\t\t********** WELCOME TO FITNESS 3 **********\n")
            print("----------- Amazing offer for one year: 190 Euro per Year!! -----------")
            print("\nIncludes:")
            print("\n-Basic Pack of Fitness 1")

            packChoice1 = int(input("\nPlease, press 1 to purchase this package (Press another key to go back): "))
            if packChoice1 == 1:
                Purchase.fitnessCost = 190
                print("You have successfully purchased the offer for Fitness 3")
                print("\nGo to Menu, and there you can take the payment receipt")
            else:
                print("Something went wrong! Redirecting back to the Previous Menu\nPlease Wait!")
                time.sleep(1.1)
                os.system("CLS")
                self.fitness()
            
            gotoMenu = int(input("\nPress 1 to Redirect Main Menu: "))
            os.system("CLS")
            if gotoMenu == 1:
                menu()
            else:
                menu()
        elif self.choiceFitness == 4:
            print("\t\t********** WELCOME TO FITNESS 4 **********\n")
            print("----------- All Inclusive: 2000 Euro per Year!! -----------")
            print("\n\tIncludes:")
            print("\n-Bathroom")
            print("-Strong Wifi")
            print("-10+ Years Experienced Personal Trainer")
            print("-Free Proteins with high quality")
            print("-Restaurant and Bar")
            print("-All equipment available\n")
            
            packChoice1 = int(input("\nPlease, press 1 to purchase this package (Press another key to go back): "))
            if packChoice1 == 1:
                Purchase.fitnessCost = 2000
                print("You have successfully purchased the offer for Fitness 4")
                print("\nGo to Menu, and there you can take the payment receipt")
            else:
                print("Something went wrong! Redirecting back to the Previous Menu\nPlease Wait!")
                time.sleep(1.1)
                os.system("CLS")
                self.fitness()

            gotoMenu = int(input("\nPress 1 to Redirect Main Menu: "))
            os.system("CLS")
            if gotoMenu == 1:
                menu()
            else:
                menu()
        else:
            print("Something went wrong! Redirecting back to the Previous Menu\nPlease Wait!")
            time.sleep(1.1)
            os.system("CLS")
            menu()

class Chargers(Purchase, Customer):
    def printBill(self):
        with open("payment.txt", "w") as outff:
            outff.write("****** FiveStar ******\n")
            outff.write("-------------Payment-------------\n")
            outff.write("___________\n")
            outff.write(f"Customer ID: {Customer.custID}\n\n")
            outff.write("\t\t\t Total\n")
            outff.write(f"Fitness cost:\t\t {Purchase.fitnessCost:.2f}\n")
            outff.write("___________\n")
            outff.write(f"Total Charge:\t\t {Purchase.fitnessCost:.2f}\n")
            outff.write("___________\n")
            outff.write("------------THANK YOU FOR YOUR PURCHASE------------\n")

    def showBill(self):
        with open("payment.txt", "r") as inff:
            if not inff:
                print("File Error!")
            for line in inff:
                print(line)

if __name__ == "__main__":
    startObj = ManageMenu()
