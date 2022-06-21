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
    
    print(f"\nincome: {income}\nhours: {hours}\ndays: {days}")

def main() -> None:
    clearConsole()
    calculateIncome()

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
