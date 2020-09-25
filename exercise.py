annual_salary= int(input("The employees annual salary"))
contract_type= str(input(" permanent or part time"))

if contract_type == "permanent":
    print("income_tax equal to 0.295")

elif contract_type == "part time": #it is in percentage
    print("income_tax equal to 0.25")

income_tax = float(input("tax percentage"))

gross_monthly_salary=( annual_salary / 12)
print("gross_monthly_salary" , gross_monthly_salary)

monthly_payable_tax=(gross_monthly_salary * income_tax)
print("monthly payable salary", monthly_payable_tax)

net_monthly_salary= (gross_monthly_salary - monthly_payable_tax)
print("net monthly salary", net_monthly_salary)
