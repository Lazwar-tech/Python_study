# r_list = [1, 2, 3, 4, 5, 6, 7, 9]
r_list = [1, 1, 2, 1]
# r_list = [6, 3, 7]

import random

for i in range(random.randint(3, 10)):
    random.choice(r_list)
s_list = [r_list[0], r_list[2], r_list[-2]]
print(s_list)

