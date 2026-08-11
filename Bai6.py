import streamlit as st
import time 
st.title("Order food")
food1 = st.text_input('What do you want to eat? ')
drink1 = st.text_input('What do you want to drink?')

if st.button("Confirm Order"):
    st.write("Your oder: ")
    st.write("Food: ",food1)
    st.write("Drink: ",drink1)


st.title("My progress bar: ")
myBar = st.progress(0)

for percentComplete in range(100):
    time.sleep(0.05)
    myBar.progress(percentComplete+1)

st.balloons()
st.write('toy can 10 diem TIENG ANH')