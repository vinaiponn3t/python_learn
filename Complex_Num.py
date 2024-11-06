#Mathematical constants
from scipy.constants import pi, golden_ratio
from statistics import variance,stdev

print(f"pi = {pi}")
print(f"Golden ratio = {golden_ratio}")
print(f"variance = {variance}")
print(f"stdev = {stdev}")
print()
print(dir(variance))
print(dir(stdev))
print()

#จำนวนเชิงซ้อน (complex number)รูปแบบที่ 1
c_num1 = complex(-4.5,2)
print("value of c_num1 is:",c_num1)
print("real_number of c_num1 is:",c_num1.real)
print("imaginary_number of c_num1 is:",c_num1.imag)
print()

#จำนวนเชิงซ้อน (complex number)รูปแบบที่ 2
c_num2 = -4.5+2j
print("value of c_num2 is:",c_num2)
print("real_number of c_num2 is:",c_num2.real)
print("imaginary_number of c_num2 is:",c_num2.imag)
print()

c_num3 = 5.5+2j
print("value of c_num3 :",c_num3)
print("c_num2 + c_num3 :",c_num2+c_num3)
print("c_num2 x c_num3 is:",c_num2*c_num3)
print("c_num2 x 2 is:",c_num2*2)
print()
