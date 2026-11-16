import numpy as np

sales = np.array([1000,2000,3000,4000,5000])
total = np.sum(sales)

print(total)


# create an array filled with zeros
numbers = np.zeros(5)
print(numbers)
# Create an array filled with ones
numbers = np.ones(6)
print(numbers)

# Create range of numbers
numbers = np.arange(1,5)
print(numbers)


# Array Dimentions (1D, 2D, 3D)

sales = np.array([[1,2],[11,21]])
print(sales)
print(sales.ndim)
print(sales.shape)


# 3D Dimentions
sales = np.array([
    [
        [1,2],[3,4]
    ],
    [
        [5,6],[7,8]
    ]
])

print(sales)
print(sales.ndim)
print(sales.shape)




# Array Indexing and slicing
numbers = np.array([1,2,3,4,5,6])
print(numbers[1])

print(numbers[-1])