from utils.growUpFaster import hackForGrowUpFaster
from config import brazilLegalAge
from global_variables import age

name = "Gabriel"

if age >= brazilLegalAge:
    print("You're of legal age.")
else:
    age = hackForGrowUpFaster(age)
    print(f"Now you are {age} years old and of legal age.")
