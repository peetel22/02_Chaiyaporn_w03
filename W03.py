# BMI calculator
# Result = W / H^2 = h*h

W = float(input("กรุณากรอกน้ำหนัก :"))
H = int(input("กรุณากรอกส่วนสูง :"))
R = W/(H/100*(H/100))
print(f"ค่า BMI :{R:.2f}")

