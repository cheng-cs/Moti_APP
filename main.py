import random
import pandas as pd
# import streamlit as st


def openF():
    
    df = pd.read_csv('quotes.csv' , delimiter=',')

    # num = randomGenNum()

    # print(df.Author[num])
    # print(df.Quote[num])

    # print("Your quote: \n", df.Quote[num], "by: \n", df.Author[num])

    # print using st.write. 

    x = 1
    y = 8
    for x in range(1, y):
        num = randomGenNum()
        print("Your quote: \n", df.Quote[num],"\n", "by: \n", df.Author[num])
        x+=1

def randomGenNum():
    line_Num = random.randint(1,1666) # working 
    print()
    return line_Num

def main():
    # st.write()
    openF()


main()