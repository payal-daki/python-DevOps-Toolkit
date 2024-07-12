#creating a set 
my_set = {1, 2, 3, 4, 5}
print (my_set)

#adding and removing the value
my_set.add(6)  # Adding an element
print(my_set)

my_set.remove(3)  # Removing an element
print(my_set)


#set operation
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
print (union_set)
intersection_set = set1.intersection(set2)  # Intersection of sets
print(intersection_set)
difference_set = set1.difference(set2)  # Difference of sets
print(difference_set)


#subset and superset
is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
print(is_subset)
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2
print(is_superset)
