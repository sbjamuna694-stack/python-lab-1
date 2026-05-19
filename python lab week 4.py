#%%
#collectins
print("===list example===")
fruits=["apple", "strawberry", "banana"]
print("original list:", fruits)

fruits.append("orange")
#remove element
if"banana" in fruits:
    fruits.remove("banana")
    #access by index
    print("first friut:",fruits[0])


#tuple
print("\n   tuple example")
coordinates=(10,20.3,10.5)
print("tuple:",coordinates)
print("first coordinate:",coordinates[-1])

#tuple unpacking
x,y,z=coordinates
print(f"unpacked:x={x},y={y},z={z}")


#create a list of 5 numbers and print all elements
numbers=[10,20,30,40]
for num in numbers:
    print(num)

#print first and last element of a list[10,20,30,40,50]
numbers=[10,20,30,40,50]
print("first element in numbers: ",numbers[0])
print("last element in numbers: ",numbers[-1])

#add numbers 100 to the list[1,2,3,4]
num=[1,2,3,4]
num.append(100)
print(num)

#remove element 3 from the list[1,2,3,4,5]
num=[1,2,3,4,5]
num.remove(3)
print(num)

#find the sum of all elements in[5,10,15,20]
num=[5,10,15,20]
total=sum(num)
print("sum of all elements:",total)

#find the maximum and minimum in [8,3,9,1,6]
num=[8,3,9,1,6]
maximum=max(num)
minimum=min(num)
print("maximum of all elements:",maximum)
print("minimum of all elements:",minimum)

