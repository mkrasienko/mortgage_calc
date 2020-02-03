from datetime import *
from dateutil.relativedelta import *
import calendar
import time

#Welcome messages
welcome = "WELCOME TO THE MORTGAGE CALCULATOR"
txt = welcome.center(80,'*')
print(txt)

time.sleep(1.5)
prompt = "<PLEASE ENTER THE INFORMATION WHEN PROMPTED>"
txt2 = prompt.center(80)
print(txt2)
time.sleep(1)

#Get Principal: the ammount you want to borrow from the bank.
try:
    p = float(input("What is your principal? ($): "))
except ValueError:
    print("Please enter a valid number.")
    p = float(input("What is your principal? ($): "))

#Get annual interest rate
try:
    rate = float(input("What is that annual interest rate? (%): "))
except ValueError:
    print("Please enter a valid number.")
    rate = float(input("What is that annual interest rate? (%): "))

#Monthly rate to percentage
rate_p = float(rate)/100
#Monthly rate
m_rate = float(rate_p)/12

#Get loan period
try:
    n = int(input("How long is the loan period? (in years): "))
except ValueError:
    print("Please enter a valid number.")
    n = int(input("How long is the loan period? (in years): "))
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
MP = (p)*(r1_pow_r/r1_pow_minus_1)


#Get start date
try:
    input_date = input("Enter first payment date (YYYY-MM-DD): ")
    year, month, day = map(int, input_date.split('-'))
    start_date = datetime.date(datetime(year, month, day))
    #Last Payment
    last_pay_day = (start_date + relativedelta(months=+nm))
except ValueError:
    print("Please enter a valid number.")
    input_date = input("Enter first payment date (YYYY-MM-DD): ")
    year, month, day = map(int, input_date.split('-'))
    start_date = datetime.date(datetime(year, month, day))
    #Last Payment
    last_pay_day = (start_date + relativedelta(months=+nm))

print("------------------------------------------------")
print(f"Your monthly payment will be: ${round(MP, 2)}")
time.sleep(1.1)
print(f"Your last payment will be on: {last_pay_day}")

time.sleep(2)
thank_you_prompt = "THANK YOU FOR USING THE MORTGAGE CALCULATOR"
thank_you = thank_you_prompt.center(80, '*')
print(thank_you)

