import random
import pandas as pd

def openF():
    df = pd.read_csv('quotes.csv' , delimiter=',')
    num = randomGenNum()
    print()
    print("by: ",df.values[num])
    print()


def randomGenNum():
    quote_Num = random.randint(1,1666) # working 
    print()
    return quote_Num

def main():
    openF()


main()