name = "Kendra Repo"

# ****** ONE ******
# Orginal code found in "The Accumulator Patter with Lists"
# nums = [3, 5, 8]
# accum = []
# for w in nums:
#    x = w**2
#    accum.append(x)
# print accum
# ****** New Code ******
nums = [3, 5, 8]
print map((lambda value: value**2), nums)

# ****** TWO ******
# Orginal code found in "Lists and for loops"
# numbers = [10, 20, 30, 40, 50]
# print numbers
# for i in range(len(numbers)):
#    numbers[i] = numbers[i]**2
# print numbers
# ****** New Code ******
numbers = [10, 20, 30, 40, 50]
print numbers
print map((lambda value: value**2), numbers)

# ****** THREE ******
# Orginal code found in "Practice Problems: Material Prior to Functions"
# def sum_a_list(lt):
#    tot = 0
#    for i in lt:
#        tot = tot + i
#    return tot
# print sum_a_list([1,4,7,5])
# ****** New Code ******
a_list = [1,4,7,5]
print reduce(lambda x, y: x + y, a_list)

# ****** FOUR ******
# Orginal code found in "10/4 Problem Set"
# items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# acc_num = 0
# for element in items:
#   if "w" in element:
#     acc_num = acc_num + 1
# ****** New Code ******
items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_lst = [element for element in items if "w" in element]
acc_num = reduce(lambda x, y: x+1, acc_lst,0)
print acc_num

# ****** FIVE ******
# Orginal code found in "The Accumulator Pattern with lists"
# alist = [4,2,8,6,5]
# blist = [ ]
# for item in alist:
#    blist.append(item+5)
# print blist
# ****** New Code ******
alist = [4,2,8,6,5]
blist = [num+5 for num in alist]
print blist