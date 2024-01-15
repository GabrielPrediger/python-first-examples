from config import brazilLegalAge

def hackForGrowUpFaster(yourAge):
    currentAge = yourAge
    while currentAge < brazilLegalAge:
        print("POWER ON!")
        currentAge += 1
    return currentAge
