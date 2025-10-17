from time import sleep

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def gpa_calculator():
    gpa_values = input(f"Enter your GPA's being sure to: \n Separating them with commas \n No Duplicate Commas \n No letters \n Input Here:  ")
    gpa_values = gpa_values.split(',')
    for num in gpa_values:
            if num == num in letters:
                print("Letters are not allowed")
                gpa_calculator()
            if num in gpa_values == ['']:
                 print("You put 2 commas")
                 gpa_calculator()
    gpa_values = [float(num.strip()) for num in gpa_values]
    for num in gpa_values:
        if num >=5 or num <=0:
                print("Number inputted not in correct GPA range")
                gpa_calculator()
    gpa_sum = float(sum(gpa_values))
    gpa_count = int(len(gpa_values))
    gpa = gpa_sum / gpa_count
    gpa_rounded = round(gpa,2)
    gpa_sorted = sorted(gpa_values)
    print(f"Your average GPA given your values is: {gpa_rounded}")

    goal_gpa = input("What is your goal GPA? ").strip()
    lowest_value = min(gpa_sorted)
    gpa_sorted.remove(lowest_value)
    gpa_sorted.append(4.0)
    gpa_sum = float(sum(gpa_sorted))
    gpa_count = int(len(gpa_sorted))
    new_gpa = gpa_sum / gpa_count
    new_gpa_rounded = round(new_gpa,2)
    if new_gpa >= float(goal_gpa):
        print(f"Congratulations! By replacing your lowest GPA with a 4.0, you have reached your goal GPA of {goal_gpa}. Your new GPA is {new_gpa_rounded}.")
    else:
        print(f"Unfortunately, even by replacing your lowest GPA with a 4.0, you have not reached your goal GPA of {goal_gpa}. Your new GPA is {new_gpa}.")


gpa_calculator()