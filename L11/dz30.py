from typing import Union


def is_even(num: int) -> Union[str, bool]:
    if str(num)[-1] in "02468":
        return True
    return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'


