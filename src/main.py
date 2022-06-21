# pip freeze > requirements.txt
#* -- Imports
import os

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

perHour = 0
perDay = 0
perYear = 0

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")
    
def calculateIncome(income:float, hours:int, days:int) -> dict:
    global perHour, perDay, perYear
    
    perHour = income / ((days * 4) * hours)
    
    perDay = perHour * hours

    perYear = income * 12
    
    return {
        "perHour": perHour,
        "perDay": perDay,
        "perYear": perYear,
        "perYear*": perYear + income
    }

def main() -> None:
    while True:
        clearConsole()
        try:
            income = float(input("Please enter your monthly income. (float)\n>>> "))
            hours = int(input("\nPlease enter your work daily hours. (int)\n>>> "))
            days = int(input("\nPlease enter how many days in the week you work. (int)\n>>> "))
        except Exception as e:
            print(f"\nERROR: {e}\nPlease insert the right value!\n")
            os.system("pause")
            continue
        
        output = calculateIncome(income, hours, days)
        
        print("\n- - - - - - - - - - - - - - - - - - - - - - - -\n")
        for item in output:
            if item == "perYear*":
                print(f"{item}: " + "${:0,.2f}".format(output[item]) + " (Christmas bonus)\n")
            else:
                print(f"{item}: " + "${:0,.2f}\n".format(output[item]))
        print("- - - - - - - - - - - - - - - - - - - - - - - -\n")
        
        if input("Run again? (y/n)\n>>> ").lower() == "n":
            break

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
