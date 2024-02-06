import numpy as np

msg = "Roll a dice"
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array(42)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(msg)
print(np.__version__)
print(np.random.randint(1,9))
print(type(arr))
print(arr4)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)