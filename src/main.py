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
    
def calculateIncome() -> None:
    global perHour, perDay, perYear
    
    income = float(input("Please enter your monthly income. (float)\n>>> ")) #TODO try|except
    hours = int(input("\nPlease enter your work daily hours. (int)\n>>> ")) #TODO try|except
    days = int(input("\nPlease enter how many days in the week you work. (int)\n>>> ")) #TODO try|except
    
    print(f"\nincome: {income}")
    print(f"hours: {hours}")
    print(f"days: {days}")
    
    perHour = income / ((days * 4) * hours)
    
    perDay = perHour * hours

    perYear = income * 12
    
    # print(f"\nperHour: {perHour}")
    print("\nperHour: ${:0,.2f}".format(perHour))
    
    # print(f"perDay: {perDay}")
    print("perDay: ${:0,.2f}".format(perDay))
    
    # print(f"perYear: {perYear}")
    print("perYear: ${:0,.2f}".format(perYear))

    # print(f"perYear*: {perYear + income} (Christmas bonus)")
    print("perYear*: ${:0,.2f} (Christmas bonus)".format(perYear + income))

def main() -> None:
    clearConsole()
    calculateIncome()

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
