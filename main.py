 print('''-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------''')
# inputs
salary = input('What is your annual salary? \n')
if not salary.isnumeric():
    print('Must enter positive integer for salary.')
    exit()
rent = input('How much is your monthly mortgage or rent? \n')
if not rent.isnumeric():
    print('Must enter positive integer for mortgage or rent.')
    exit()
bills = input('What do you spend on bills monthly? \n')
if not bills.isnumeric():
    print('Must enter positive integer for bills.')
    exit()
food = input('What are your weekly grocery/food expenses? \n')
if not food.isnumeric():
    print('Must enter positive integer for food.')
    exit()
travel = input('How much do you spend on travel annually? \n')
if not travel.isnumeric():
    print('Must enter positive integer for travel.')
    exit()
salary = int(salary)
rent = int(rent)
bills = int(bills)
food = int(food)
travel = int(travel)
# doing the math
if salary < 15000:
    tax_category = .1
elif salary < 75000:
    tax_category = .2
elif salary < 200000:
    tax_category = .25
else:
    tax_category = .3
tax = tax_category * salary
if tax >= 75000:
    tax = 75000
    tax_limit = '>>> TAX LIMIT REACHED <<<'
else:
    tax_limit = ''
tax_percent = round(float(int(tax) / salary * 100), 2)
tax_pun = format(float(tax), '11,.2f')
tax_tag = '#' * int(tax_percent)
annual_rent = rent * 12
rent_percent = round(float(int(annual_rent) / salary * 100), 2)
annual_rent_pun = format(float(annual_rent), '11,.2f')
rent_tag = '#' * int(rent_percent)
annual_bills = bills * 12
bills_percent = round(float(int(annual_bills) / salary * 100), 2)
annual_bills_pun = format(float(annual_bills), '11,.2f')
bills_tag = '#' * int(bills_percent)
annual_food = food * 52
food_percent = round(float(int(annual_food) / salary * 100), 2)
annual_food_pun = format(float(annual_food), '11,.2f')
food_tag = '#' * int(food_percent)
annual_travel = travel
travel_percent = round(float(int(annual_travel) / salary * 100), 2)
annual_travel_pun = format(float(annual_travel), '11,.2f')
travel_tag = '#' * int(travel_percent)
extra = salary - (annual_rent + tax + annual_bills + annual_food + annual_travel)
extra_pun = format(float(extra), '11,.2f')
extra_percent = round(float(int(extra) / salary * 100), 2)
if extra < 0:
    extra_warning = 0
    deficit = '>>> WARNING: DEFICIT <<<'
else:
    extra_warning = extra_percent
    deficit = ''
extra_tag = '#' * int(extra_warning)
bar_length = max(len(extra_tag), len(travel_tag), len(tax_tag), len(food_tag), len(bills_tag), len(rent_tag))
# output
print('')
print('-' * (bar_length + 42))
print('See the financial breakdown below, based on a salary of $' + str(salary))
print('-' * (bar_length + 42))
print('| mortgage/rent | $' + str(annual_rent_pun), '|' +
      format(rent_percent, '6,.1f') + '% |', rent_tag)
print('|         bills | $' + str(annual_bills_pun), '|' +
      format(bills_percent, '6,.1f') + '% |', bills_tag)
print('|          food | $' + str(annual_food_pun), '|' +
      format(food_percent, '6,.1f') + '% |', food_tag)
print('|        travel | $' + str(annual_travel_pun), '|' +
      format(travel_percent, '6,.1f') + '% |', travel_tag)
print('|           tax | $' + str(tax_pun), '|' +
      format(tax_percent, '6,.1f') + '% |', tax_tag)
print('|         extra | $' + str(extra_pun), '|' +
      format(extra_percent, '6,.1f') + '% |', extra_tag)
print('-' * (bar_length + 42))
print(deficit + tax_limit)
