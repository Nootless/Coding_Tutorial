def sum_list(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum

def length_list(list):
    length = 0
    for x in list:
        length = length + 1
    return length

def class_average(list_of_scores):
    sum_class = sum_list(list_of_scores)
    length_list = len(list_of_scores)
    print(f'The Class average = {sum_class / length_list}')
    return sum_class / length_list

values = [90, 85, 27, 70, 66, 94, 88]
class_avg = class_average(values)