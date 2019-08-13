import datetime
import dateutil
import time

#Get Principal: the ammount you want to borrow from the bank.
try:
    p = int(input("Principal ($): "))
except ValueError:
    print("Please enter a valid number.")
    p = int(input("Principal ($): "))

#Get annual interest rate
try:
    rate = float(input("Annual interest rate (%): "))
except ValueError:
    print("Please enter a valid number.")
    rate = float(input("Annual interest rate (%): "))

#Monthly rate to percentage
rate_p = float(rate)/100
#Monthly rate
m_rate = float(rate_p)/12

#Get loan period
try:
    n = int(input("Loan periot (in years): "))
except ValueError:
    print("Please enter a valid number.")
    n = int(input("Loan periot (in years): "))
#Convert years to months
nm = float(n)*12

#Monthly Payment
#1+r
r_plus_1 = m_rate + 1
#(1+r)^n
r1_pow = float(pow(r_plus_1, nm))
#r(1=r)^n
r1_pow_r = r1_pow*m_rate
#(1+r)^n-1
r1_pow_minus_1 = r1_pow-1
#calculate
MP = float(p)*(r1_pow_r/r1_pow_minus_1)


#Get start date
input_date = input("Enter first payment date (YYYY-MM-DD): ")
year, month, day = map(int, input_date.split('-'))
start_date = datetime.date(year, month, day)
tdelta = datetime.timedelta(nm*30)
#Last Payment
last_pay_day = (start_date + tdelta)


print(f"Your monthly payment is: ${round(MP, 2)}")
time.sleep(1.1)
print(f"Your last payment will be on: {last_pay_day}")



