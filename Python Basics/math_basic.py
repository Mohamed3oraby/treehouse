from statistics import median
from statistics import mode
from statistics import mean

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
min_grade = min(test_grades)
max_grade = max(test_grades)
test_grades.sort()
print(test_grades)
print("The minimum grade is: {} and the maximum grade is {}".format(min_grade, max_grade))


passed = 0
for grade in test_grades:
    if grade >= 70:
        passed += 1

total_grades = len(test_grades)
percentage_passed = round(passed / total_grades * 100)

essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]
essay_grades.sort()
print(essay_grades)

median_grade = median(test_grades)
median_essay = median(essay_grades)

test_mode = mode(test_grades)
essay_mode = mode(essay_grades)

test_average = mean(test_grades)
essay_average = mean(essay_grades)

print(f"The median test grade is: {median_grade}")
print(f"The median essay grade is: {median_essay}")
print(f"The most often seen grade is: {test_mode}")
print(f"The most often seen essay grade is: {essay_mode}")
print(f"The average test grade is: {test_average}")
print(f"The average essay grade is: {essay_average}")
print(f"The number of students who passed: {passed}")
print(f"The number of students who did not pass: {total_grades - passed}")
print(f"The percentage of students who passed: {percentage_passed}%")
print(f"The percentage of students who did not pass: {100 - percentage_passed}%")