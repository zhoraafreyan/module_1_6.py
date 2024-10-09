#2
my_dict = {'гога': 1988, 'пётр': 2000, 'феликс': 1977}
print(my_dict)
print(my_dict['феликс'])
print(my_dict.get('катя', 'без ошибки'))
my_dict.update({'вера': 2011,
               'надежда': 2010})
a = my_dict.pop('гога')
print(a)
print(my_dict)
#3
my_set = {1, 1, 1, 1, 10.11, 'руки', 'руки'}
print(my_set)
my_set.update({23, 12+5,
               (1,3,5,7)})
my_set.discard(1)
print(my_set)