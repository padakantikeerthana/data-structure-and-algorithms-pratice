arr=[10,20,30,40]

print("Original list:", arr)

#append
arr.append(50)
print("after append:",arr)

#insert
arr.insert(2,25)
print("after insert:",arr)

#remove
arr.remove(20)
print("after remove:",arr)

#pop
arr.pop(3)
print("after pop:",arr)

#index
print("Index of 30:", arr.index(30))

#count
arr.append(10)
print("count of 10:",arr.count(10))

#sort
arr.sort()
print("after sort:",arr)

#reverse
arr.reverse()
print("after reverse:",arr)

#update
arr[1]=12
print("after update:",arr)

#clear
temp=arr.copy()
temp.clear()
print("after clear:",temp)

#searching (linear search)
arr =[10,20,30,40,50]
key=30
for i in range(len(arr)): 
    if arr[i]==key:
        print("element found at index:",i)
        break

#2d array
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(len(matrix)):
    row_sum =0
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]

    print("Row", i, "sum:", row_sum)
    
print("2D Array:")
for row in matrix:
    print(row)
