# Convert celsius to other temperature mesaures
c_tempt=float(input("Enter temperature in Celsius: "))
print("Enter F for Fahrenheit and K for Kelvin")
choice=input("Convert to Fahrenheit or Kelvin? : ")
if choice=='F' or choice=='f':
    f_tempt=(c_tempt*9/5)+32
    print(f"{c_tempt}C= {f_tempt} F")
elif choice=='K' or choice=='k':
    k_tempt=c_tempt+273.15
    print(f"{c_tempt}C= {k_tempt} K")