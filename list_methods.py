basket=[1,2,3,4,5]
print(len(basket))
# adding
basket.append(6)
print(basket)
# insert
basket.insert(2,'insert')
print(basket)
# extend
basket.extend([100,1001])
print(basket)

# poping - removing
basket.pop()
print(basket)

basket.remove('insert')
print(basket)

# reverse
basket.reverse()
print(basket)

basket.sort()
print(basket)


# returns indec of the element
print(basket.index(2))

# to check if 'd' is in the list print(basket.index('d',0,4))

# to check if variable is in the list
print('x' in basket)
print(2 in basket)

# count
print(basket.count(4))


# sorteed built in function that doesnt modify the list

print(sorted(basket))