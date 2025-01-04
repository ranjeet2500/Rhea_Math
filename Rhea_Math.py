# Write a program with methods to compute two numbers
import streamlit as st
def Add_Num(num_1, num_2):
    add_number=num_1+num_2
    return add_number

def Diff_Num(num_1, num_2):
    diff_number=num_1-num_2
    return diff_number

def Prod_Num(num_1, num_2):
    prod_number=num_1*num_2
    return prod_number

def Div_Num(num_1, num_2):
    div_number=num_1/num_2
    return div_number

def Power_Num(num_1, num_2):
    power_number=num_1**num_2
    return power_number

#number_1= float(input("Input the First number "))
#number_2= float(input("Input the second number "))

number_1= float(st.number_input("Input the First number Number 1 "))
number_2= float(st.number_input("Input the Second  number Number 2"))

add_num1_num2=Add_Num(number_1,number_2)
diff_num1_num2=Diff_Num(number_1,number_2)
prod_num1_num2=Prod_Num(number_1,number_2)
div_num1_num2=Div_Num(number_1,number_2)
power_num1_num2=Power_Num(number_1,number_2)

st.write("The sum of number 1 and number 2:", add_num1_num2)
st.write("The difference of number 1 and number 2:", diff_num1_num2)
st.write("The product of number 1 and number 2:", prod_num1_num2)
st.write("The division of number 1 and number 2:", div_num1_num2)
st.write("The power of number 1 and number 2:", power_num1_num2)

#print("The sum of "+ str(number_1)+" and " +str(number_2)+" is "+str(add_num1_num2))
#print("The diffrence of "+ str(number_1)+" and " +str(number_2)+" is "+str(diff_num1_num2))
#print("The product of "+ str(number_1)+" and " +str(number_2)+" is "+str(prod_num1_num2))
#print("The division of "+ str(number_1)+" and " +str(number_2)+" is "+str(div_num1_num2))
#print("The power of "+ str(number_1)+" and " +str(number_2)+" is "+str(power_num1_num2))