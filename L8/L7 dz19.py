import random


def common_elements():
    list1 = [i for i in range(1, 100) if i % 3 == 0]
    list2 = [i for i in range(1, 100) if i % 5 == 0]
    random.shuffle(list1)
    random.shuffle(list2)
    list1 = random.sample(list1, min(30, len(list1)))
    list2 = random.sample(list2, min(30, len(list2)))
    result = set(list1) & set(list2)
    return result


print(common_elements())