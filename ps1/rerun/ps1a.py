# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:10:24 2021

@author: a5020
"""

while True:
    try:
        annual_salary = float(input("Enter your annual salary:"))
        if(annual_salary <= 0):
            raise Exception
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
        if not(0 <= portion_saved < 1):
            raise Exception
        total_cost = float(input("Enter the cost of your dream home:"))
        if(total_cost <= 0):
            raise Exception
        break
    except ValueError:
        print("numbers please")
    except Exception:
        print("Integer for annual salary and cost of home, decimal between 0 and 1 for percentage savings please")
        

portion_down_payment = total_cost * 0.25

current_savings = 0

monthly_salary = annual_salary / 12

monthly_saving = monthly_salary * portion_saved

month_counter = 0

while (current_savings < portion_down_payment):
    current_savings += ((current_savings*0.04)/12)
    current_savings += monthly_saving
    month_counter += 1
    
print("Number of months:", month_counter)