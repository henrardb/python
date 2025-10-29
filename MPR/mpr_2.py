#!/usr/bin/env python3

import pandas as pd

def generate_mpr(n1:int, n2:int) -> int:
    """
    Panda library usage is not needed for this kind of exercice but it is used as eductional purpose
    """

    moitie: list[int] =[n1]
    double: list[int] =[n2]

    while(min(moitie) != 1):
        moitie.append((min(moitie)//2))

    while(len(double) != len(moitie)):
        double.append(max(double) * 2)

    df_numbers = pd.DataFrame(zip(moitie, double))
    df_numbers_rest = df_numbers.loc[(df_numbers[0] % 2 != 0),:]
    result = sum(df_numbers_rest[1])

    return result

if __name__ == "__main__":
    n1=89
    n2=18

    result = generate_mpr(n1, n2)

    print(f"Le résultat de {n1} multiplié par {n2} est {result}")
