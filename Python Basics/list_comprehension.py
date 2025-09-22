# Normal
numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)


players = ['Messi', 'Neymar', 'Suarez']
ages = [38, 32, 36]

age_comb = []
for player in players:
    for age in ages:
        age_comb.append([player, age])
        
print(age_comb)




# List Comprehension
odd_numbers = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_numbers)


age_comb = [[player, age] for player in players for age in ages]
print(age_comb)


