# the speciality of a set is that the elements inside a set are unique that is they do not show repeated elements
my_set={1,2,4,5,6,3,5}
print(my_set)
my_set.add(100)
my_set.add(3)
print(my_set)
print(1 in my_set)

# removing repeated elements  from a list
my_list=[1,2,3,4,5,6,5,4,3,2,1,]
print(my_list)
print(set(my_list))



new_set={4,5,7,8,9,43,3}
print(new_set)
print(my_set.difference(new_set))
print(my_set.discard(5))
print(my_set)
# print(my_set.difference_update(new_set))
print(my_set)
print(my_set.intersection(new_set))
print(my_set.isdisjoint(new_set))
print(my_set.union(new_set))
print(my_set.issubset(new_set))
print(new_set.issuperset(my_set))


