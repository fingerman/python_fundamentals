list_a = {1, 2, 3, 4, 5}
filter_obj = filter(lambda x: x % 2 == 0, list_a)   # filter object <filter at 0x4e45890>
even_num = list(filter_obj)                          # Converts the filer obj to a list
print(even_num)
# Output: [2, 4]

my_nums = [0, 32, 0, 43, 4, 6, 0]
nonzeroes = list(filter(lambda x: x!=0, my_nums))
print(nonzeroes)

angaben = [['NA', 12, 5, 78], [2, 13, 5, 7], [2, 'NA', 5, 78], [2, 14, 5, 39], [3, 13, 'NA', 7]]

def new_func(lst):
    for i in lst:
        if i  == 'NA':
            pass
        else:
            return i


angaben_neu = list(filter(new_func(angaben), angaben))
print(angaben_neu)