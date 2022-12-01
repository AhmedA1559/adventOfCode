def sum_up_calories(calories):
    total = 0
    for c in calories:
        total += c
    return total

with open('calories.txt') as f:
    elves_calories = []
    calorie_buffer = []
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            elves_calories.append(sum_up_calories(calorie_buffer))
            calorie_buffer = []
            continue
        calorie_buffer.append(int(line))
    elves_calories.append(sum_up_calories(calorie_buffer))

    max_three = []
    for _ in range(3):
        max_three.append(max(elves_calories))
        elves_calories.remove(max(elves_calories))
    print(sum(max_three))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
