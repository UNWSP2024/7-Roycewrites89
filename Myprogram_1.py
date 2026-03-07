#Royce Daniel, 2/6/2026, "Rainthinker MK 2"
total_rainfall = 0.0
total_months = 0

for month in range(1, 13):
    rainfall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rainfall[1]=float(input(f"Enter rainfall for month {month} (in inches): "))
    total_rainfall += rainfall[1]
    total_months += 1
    rainfall.sort()
average = total_rainfall / 12

print("The average rainfall for the year was", average)
print("The total rainfall for the year was", total_rainfall)
print("The highest rainfall for the year was", max(rainfall))
print("The lowest rainfall for the year was", min(rainfall) )