#working on elements
motorcycles = ['haonda', 'yamaha', 'suzuki']
print(motorcycles)

#To change an element
motorcycles[0] = 'ducati'
print(motorcycles)

#To add, use append
motorcycles.append ('ducati')
print(motorcycles)

#To add, use insert
motorcycles.insert(0,'zu')
print(motorcycles)

#To change
motorcycles[1] = 'honda'
print(motorcycles)

#To delete
del motorcycles[0]
print(motorcycles)

#To pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)  

#To pop an item from any position
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#To remove an item by value
motorcycles.remove('suzuki')
print(motorcycles)

too_expensive ='yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#To sort in alphabetical order
cars = ['lexus', 'camry', 'benz', 'ferrari']
cars.sort()
print(cars)

#To sort in reverse order
cars.sort(reverse=True)
print(cars)

#Sorting in temporarily order with sorted()function
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#To print a list in reverse order
cars.reverse()
print(cars)

#To find the length of a list
cars = ['lexus', 'camry', 'benz', 'ferrari']
len(cars)
print(len(cars)) 

print(cars[-1])