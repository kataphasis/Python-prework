user_name="patrick"
def hello_name(user_name):
    user_name = input("patrick")
    return "hello_" + user_name
print(hello_name(user_name))
#i honestly don't know what i'm doing wrong to not make this print the whole thing, i tried print() in the function and it did nothing, shouldn't return also print the string and not just patrick?

def first_odds():
    numbers = []
    for i in range(1, 100, 2):
        numbers.append(i)
    print(numbers)
print(first_odds())


def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
z_list = [100, 200, 300, 1, 54, 1347]
print(max_num_in_list(z_list))

def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(2000))

#i had to look the exact code of this last one up, very tricky#
def is_consecutive(b_list):
    return sorted(b_list) == list(range(min(b_list), max(b_list)+1))
c_list=[1, 4, 2, 3, 6, 5]
print(is_consecutive(c_list))