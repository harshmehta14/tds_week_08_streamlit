import streamlit as st
st.title("Largest among 3 numbers")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):
  st.write("A is greater than B & C")
elif (b>a) and (b>c):
  st.write("B is greater than A & C")
elif (c>a) and (c>b):
  st.write("C is greater than A & B")
else:
  st.write("Enter values for A B and C")
