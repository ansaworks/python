print("Today's date?")
today = input()
print("Breakfast calories?")
breakfast = int(input())
print("Lunch calories?")
lunch = int(input())
print("Dinner calories?")
dinner = int(input())
print("Snack calories?")
snack = int(input())
sum_calories = breakfast + lunch + dinner + snack
print("Calorie content for " + today + ": " + str(sum_calories))
