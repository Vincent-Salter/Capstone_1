bill = input('What is the bill price? ')
tip_percentage = input('What tip percentage would you like to give? ')
people = input('How many people are splitting the bill? ')


x = (float(bill) * ((float(tip_percentage) / 100)+1)) / int(people)

print(f'Each person should pay $',round (x, 2))


