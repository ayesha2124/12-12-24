sal = float(input("Enter your salary: "))
bill1 = float(input("Enter the first shopping bill: "))
bill2 = float(input("Enter the second shopping bill: "))
bill3 = float(input("Enter the third shopping bill: "))
total = bill1 + bill2 + bill3
percentage = (total / sal) * 100
print(f"Total shopping amount: ${total}")
print(f"Percentage of salary spent on shopping: {percentage:.2f}%")

