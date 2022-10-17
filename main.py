import random
import pandas as pd
import streamlit as st
import time


def openF():

    # create reset button here



    df = pd.read_csv('quotes2.csv' , delimiter=';')

    x = 1
    y = 6
    for x in range(1, y):
        num = randomGenNum()
        st.markdown(df.QUOTE[num])
        st.write("by: \n", df.AUTHOR[num])
        time.sleep(2)
        x+=1
        st.empty()

    # while True:
    #     num = randomGenNum()
    #     st.write("Your quote: \n", df.Quote[num],"\n", "by: \n", df.Author[num])
    #     time.sleep(2)


    st.button("rerun")



def randomGenNum():
    line_Num = random.randint(1,75968) # working 
    # line_Num = random.randint(1,8) # working 

    print()
    return line_Num

def main():
    # st.write()
    st.title("Your Motivation")
    st.subheader("Here are some quotes to keep you going strong")

    openF()


main()