'''Author: Anugrah Chandran
Date: 25-10-24
Description:Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a
 temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula
  '''
temp=int(input("Enter temperature:"))
scale=input("Is this in (C)elsius or (F)ahrenheit?")
if scale=="C":
    f = (9/5)*temp + 32
    print(temp,"Ceicius is",f,"Farenheit")
else:
    c = 5/9*(temp - 32)
    print(temp,"Ferenheit",c,"Ceisius")


