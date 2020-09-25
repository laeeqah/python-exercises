annual_salary= int(input("please the the annual salary"))
dept_code= str(input("enter department code"))
percentage_increase= float(input("PLease enter percentage increase")) #enter as a percentage

if dept_code == "A":
    print(annual_salary * 0.072)


if dept_code == "B":
    print(annual_salary * 0.068)


if dept_code == "other":
    print(annual_salary * 0.063)

monthly_salary= (annual_salary / 12)
print("monthly salary", monthly_salary)
net_monthly_salary= monthly_salary + (monthly_salary * percentage_increase)
print("net monthly salary", net_monthly_salary)







