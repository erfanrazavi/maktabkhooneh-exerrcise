age_list = []

while True:
    age = int(input(''))
    if age == -1:
        break
    elif 10 <= age <= 90:
        age_list.append(age)
    else:
        print("Please enter a valid age between 10 and 90.")

if age_list:
    max_age = max(age_list)
    print(max_age)
else:
    print("No valid ages were entered.")