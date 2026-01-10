print('Welcome to the GPA calculator')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end')

# Map from letter grade to point value
points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0
}

num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print(f"Unknown grade '{grade}' being ignored")
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:
    print(f'Your GPA is {total_points/num_courses:.3f}')
else:
    print('No valid grades were entered.')
