def powers1(num):
    return [num, num*num]


for i in range(11):
    nums = powers1(i)
    print str(nums[0]) + ": square=" + str(nums[1])



##########

def powers2(num):
    return num, num*num

for i in range(11):
    num, square = powers2(i)
    print str(num) + ": square=" + str(square)
