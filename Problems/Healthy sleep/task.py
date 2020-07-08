input_hours_min = int(input())
input_hours_max = int(input())
input_hours_sleep = int(input())


def is_sleep_enough(hours_min, hours_max, hours_sleep):
    if hours_sleep < hours_min:
        return "Deficiency"
    if hours_min <= hours_sleep <= hours_max:
        return "Normal"
    return "Excess"


print(is_sleep_enough(input_hours_min, input_hours_max, input_hours_sleep))
