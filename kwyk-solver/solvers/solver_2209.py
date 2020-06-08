from fractions import Fraction
from functions import fraction_input


def solve():
    p = fraction_input("Entrez le paramètre de la loi exponentielle : ")
    x = fraction_input("Entrez le nombre auquel X est comparé : ")
    sign = input(
        "Le signe de la comparaison dans P() est <= ou >= ? ").strip()

    exponent = Fraction(- p * x).limit_denominator()
    if sign == ">=" or sign == "≥":
        result = f"e^({exponent})"
    elif sign == "<=" or sign == "≤":
        result = f"1 - e^({exponent})"
    else:
        print("Seuls les symboles <= et >= sont acceptés. Veuillez recommencer.")
        return
    print(f"La probabilité P est de {result}")
