from functools import reduce

nums = [1, 2, 3, 4, 5]

nums_sum = reduce(lambda a, b: a + b, nums)             # 15
# it calculates ((((1+2)+3)+4)+5)
nums_product = reduce(lambda a, b: a * b, nums)         # 120

print(nums_sum)
print(nums_product)