# Your name: Rayan Mostofa
# Your student id: 4970 7916
# Your email: mostofar@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Just me
# If you worked with generative AI also add a statement for how you used it.  

# The goal of this homework is to practice basic debugging and get familar with
# Python 3 basics.  It includes work with functions, strings, for-each loop,
# for loop, range, and conditionals

# Fix errors in the function below. It should return a count of the number
# of values between a (inclusive) and b (inclusive).  
#
# For example count_between(1, 3, [1, 2, 3, 4, 5]) should return 3
# and count_between(1, 3, [1, 2, 4, 5]) should return 2.
def count_between(a, b, nums):
    count = 0
    for num in nums:
        if num >= a and num <= b:
            count += 1
    return count

# Testing the count_between function
def test_count_between():
    print("Testing count_between")
    res = count_between(1, 3, [1, 2, 3, 4, 5])
    print("Expected: 3, Actual: ", res)
    res = count_between(1, 3, [1, 2, 4, 5])
    print("Expected: 2, Actual: ", res)
    res = count_between(4, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("Expected: 4, Actual: ", res)
    res = count_between(1, 3, [4, 5, 6])
    print("Expected: 0, Actual: ", res)
    res = count_between(1, 3, [1, 2, 3])
    print("Expected: 3, Actual: ", res)

# Fix errors in the function below.  It should return a total of the values from 1
# to the specified end (inclusive) when counting by 2's.
#
# For example total_by_twos(3) should return 4 (1 + 3). 
def total_by_twos(end):
    total = 0
    for x in range(1, end+1 , 2):
        total += x
    return total

# Testing the total_by_threes function
def test_total_by_twos():
    print("Testing total_by_twos")
    res = total_by_twos(3)
    print("Expected: 4, Actual: ", res)
    res = total_by_twos(0)
    print("Expected: 0, Actual: ", res)
    res = total_by_twos(1)
    print("Expected: 1, Actual: ", res)
    res = total_by_twos(5)
    print("Expected: 9, Actual: ", res)
    res = total_by_twos(2)
    print("Expected: 1, Actual: ", res)

# Return true if all the values in num_list are all even and false otherwise.  
# 
# For example check_all_even([2, 4, 5]) should return False and check_all_even([2, 4]) should
# return True.
def check_all_even(num_list):
    for num in num_list:
        if num % 2 == 1:
            return False
    return True

# Testing the check_all_even function
def test_check_all_even():
    print("Testing check_all_even")
    res = check_all_even([2, 4, 5])
    print("Expected: False, Actual: ", res)
    res = check_all_even([2, 4])
    print("Expected: True, Actual: ", res)
    res = check_all_even([-2, -3, -8])
    print("Expected: False, Actual: ", res)
    res = check_all_even([-100, 30, 4])
    print("Expected: True, Actual: ", res)
    res = check_all_even([3, 8])
    print("Expected: False, Actual: ", res)


# Fix the function below to return the index of the minimum value in the list nums
# or -1 if there aren't any values in the list.  If the minimum value appears more than
# once in the list you should return the index of the last one.  
# 
# For example get_index_min([20, 100, 10, 10]) should return 3.
def get_index_min(nums):        #finished

    # init the min and min_index
    min = 99999999
    min_index = 0
    counter = 0
    
    if len(nums) == 0:
        return -1
    
    # loop through the list
    for index in nums:

        # get the current value
        current = index

        # if new min
        if current <= min:

            # reset min and min index
            min = current
            min_index = counter
            
        counter += 1

    return min_index

# Testing the get_index_min function
def test_get_index_min():
    print("Testing get_index_min")
    res = get_index_min([-2, 3, -5])
    print("Expected: 2, Actual: ", res)
    res = get_index_min([1])
    print("Expected: 0, Actual: ", res)
    res = get_index_min([14, 20, 4, 14])
    print("Expected: 2, Actual: ", res)
    res = get_index_min([])
    print("Expected: -1, Actual: ", res)
    res = get_index_min([20, 100, 20, 100])
    print("Expected: 2, Actual: ", res)

# Fix the function below to:
# return 0 if score > 75 
# return 1 if score > 50 and <= 75
# return 2 if score > 25 and <= 50
# else return 3
#
# For example: get_group(75) should return 0.
def get_group(score):           #finished
    if score > 75:
        return 0
    elif 75 >= score and score > 50:
        return  1
    elif 50 >= score and score > 25:
        return  2
    else:
        return 3
    

# Test the get_group function
def test_get_group():
    print("Testing get_group")
    res = get_group(75)
    print("Expected: 1, Actual: ", res)
    res = get_group(100)
    print("Expected: 0, Actual: ", res)
    res = get_group(40)
    print("Expected: 2, Actual: ", res)
    res = get_group(18)
    print("Expected: 3, Actual: ", res)
    res = get_group(200)
    print("Expected: 0, Actual: ", res)

# Fix errors in the function below.  It should return a password (string)
# created from the first letter of each word in the passed string
# followed by a '!abc' and then the last digit of the passed year.
#
# For example create_pass("Hello world", 2021) should return "Hw!abc1"
def create_pass(the_str, year):         #finished
    words = the_str.split()
    password = ""
    for word in words:
        password += word[0]
    
    year_str = str(year)
    password = password + "!abc'" + year_str[-1]
    return password

# Testing the create_pass function
def test_create_pass():
    print("Testing create_pass")
    res = create_pass("Hello world", 2021)
    print("Expected: Hw!abc1, Actual: ", res)
    res = create_pass("Some one stop me", 2020)
    print("Expected: Sosm!abc0, Actual: ", res)
    res = create_pass("Walk", 2019)
    print("Expected: W!abc9, Actual: ", res)
    res = create_pass("Walk for Hope", 2019)
    print("Expected: WfH!abc9, Actual: ", res)
    res = create_pass("aa bb cc", 2021)
    print("Expected: abc!abc1, Actual: ", res)

# Extra credit - up to 5 points
# Fix the function below to take a list of numbers, nums, and return a new list 
# where the numbers are replaced with a string if they 
# meet the following critera:
# If the number is divisible by both 2 and 3 use "both"
# If the number is only divisible by 2 use "two"
# If the number is only divisible by 3 use "three"
# Otherwise use the number
# 
# For example divs([1, 3, 9]) should return [1, "three", "three"]
def divs(nums):         #finished
    new_nums = []
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            new_nums.append("both")
        elif num % 2 == 0:
            new_nums.append("two")
        elif num % 3 == 0:
            new_nums.append("three")
        else:
             new_nums.append(num)
    return new_nums

# Testing the divs function
def test_divs():
    print("Testing divs")
    res = divs([1, 3, 9])
    print("Expected: [1, 'three', 'three'], Actual: " + str(res))
    res = divs([1, 2])
    print("Expected: [1, 'two'], Actual: " + str(res))
    res = divs([5, 7])
    print("Expected: [5, 7], Actual: " + str(res))
    res = divs([4, 12])
    print("Expected: ['two', 'both'], Actual: " + str(res))
    res = divs([9, 24, 1])
    print("Expected: ['three', 'both', 1], Actual: " + str(res))

# declare the main method
def main():
    test_count_between()
    print()
    test_total_by_twos()
    print()
    test_check_all_even()
    print()
    test_get_index_min()
    print()
    test_get_group()
    print()
    test_create_pass()
    print()
    test_divs() # remove the # to test the extra credit

# call the main method
main()
