set1 = {'a','b','c','d','e'}
set2 = {'c','d','e','f','g'}


set1.update(['f','g','h','i','j'])
set1.remove('a')
set1.intersection_update(set2)
print(set1)