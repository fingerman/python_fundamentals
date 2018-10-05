
name = input()
age = int(input())
town = input()
salary = float(input())
agerange_check = {
    range(1, 18): "teen",
    range(19, 70): "adult",
    range(70, 99999): "elder"
}

salaryrange_check = {
    range(1, 500): "low",
    range(500, 2000): "medium",
    range(2001, 99999): "high"
}


print("Name: " + name)
print("Age: " + str(age))
print("Town: " + town)
print("Salary: $" + "{0:.2f}".format(salary))
for key in agerange_check:
    if age in key:
        print("Age range: " + agerange_check[key])
for key in salaryrange_check:
    if salary in key:
        print("Salary range: " + salaryrange_check[key])
        break



