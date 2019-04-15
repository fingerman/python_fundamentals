def summe_tuple(*nums):
    summe = sum(nums)
    return summe


def summe_list(*nums):
    for i in nums:
        return i


def summe_dict(**kwargs):
    sum1 = sum(kwargs.values())
    return sum1


# print(summe_tuple(1, 2, 3))
# print(summe_dict(a=1, b=2, c=3))
print(summe_list(['a', 'dsadsa', '3']))
