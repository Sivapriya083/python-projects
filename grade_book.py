gradebook = {}

no_entries = int(input("Enter the number of entries:"))

for i in range(no_entries):
    name = input('Enter the names : ')
    score = int(input('Enter the scores: '))
    gradebook[name] = score
print(f'dictionary after adding multiple entries: {gradebook}')

#print high low and avg marks


Highest_value = max(gradebook.values())
Lowest_value = min(gradebook.values())
Average_value = sum(gradebook.values()) / len(gradebook)

print('The highest value is : ', Highest_value)
print('the lowest score is:', Lowest_value)
print('the avg score is :', Average_value)


#print the nameof the student with  highest mark

highest_student = max(gradebook, key=gradebook.get)
highest_score = gradebook[highest_student]

print('Highest mark got by:', highest_student, 'and the highest score is:', highest_score)


#print the name of the student with  lowest mark

lowest_student = min(gradebook, key=gradebook.get)
lowest_score = gradebook[lowest_student]

print('lowest mark got by:', lowest_student, 'and the lowest score is:', lowest_score)


#print the sorted dict

sorted_grades = dict(sorted(gradebook.items(), key = lambda item:item[1]))
print('sorted in ascending order:', sorted_grades)

sorted_grades = dict(sorted(gradebook.items(), key = lambda item:item[1],reverse = True))
print('sorted in descending order:', sorted_grades)

sorted_by_name = dict(sorted(gradebook.items(), key = lambda item:item[0]))
print('sorted by names:', sorted_by_name)

sorted_by_name  = dict(sorted(gradebook.items(), key = lambda item:item[0],reverse = True))
print('sorted by names:', sorted_by_name)


#print the remove a  student
remove = input('enter a name to remove: ')
gradebook.pop(remove,None)

print("updated scores:", gradebook)









