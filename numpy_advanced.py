import numpy as np

# Re-creating our base 2D matrix of shape (3, 4)
# (Using elements 1 to 12 as intended in the previous step)
matrix_2d = np.arange(1, 13).reshape(3, 4)

print("--- Base 2D Matrix (Shape: 3, 4) ---")
print(matrix_2d)
print("\n" + "="*50 + "\n")

# 1. Elevating to a 3D Array (Shape: 2, 3, 4)
# We stack two copies of matrix_2d along a new leading axis (Axis 0)
array_3d = np.stack([matrix_2d, matrix_2d * 10], axis=0)

print("--- 1. Elevated 3D Array (Shape: 2, 3, 4) ---")
print("Page 0 (First 3x4 Matrix):")
print(array_3d[0])
print("\nPage 1 (Second 3x4 Matrix - Multiplied by 10):")
print(array_3d[1])
print("\n" + "="*50 + "\n")


# 2. Advanced Broadcasting: 1D Array to 3D Array
# Broadcasting a 1D vector of shape (4,) across the last axis of a (2, 3, 4) array.
# The vector [100, 200, 300, 400] is automatically stretched to fit shapes (3, 4) and (2, 3, 4).
vector_1d = np.array([100, 200, 300, 400])
broadcast_1d_result = array_3d + vector_1d

print("--- 2. Broadcasting (4,) Vector onto (2, 3, 4) Array ---")
print("Vector is added to every single row across both pages.")
print("Result Page 0:")
print(broadcast_1d_result[0])
print("\n" + "="*50 + "\n")


# 3. Complex Multi-Dimensional Broadcasting: (2, 1, 1) onto (2, 3, 4)
# Suppose we want to add a unique flat modifier to each individual 'page' of our 3D space.
# We create a 3D scale vector of shape (2, 1, 1). 
# Axis 0 matches (2), while Axes 1 and 2 are stretched automatically from 1 to match (3, 4).
page_modifiers = np.array([[[1000]], [[2000]]]) # Shape: (2, 1, 1)
broadcast_3d_result = array_3d + page_modifiers

print("--- 3. Advanced Broadcasting (2, 1, 1) Vector onto (2, 3, 4) Array ---")
print(f"Page Modifiers Shape: {page_modifiers.shape}")
print("Adds 1000 to all elements in Page 0, and 2000 to all elements in Page 1.")
print("Result Page 0:")
print(broadcast_3d_result[0])
print("\nResult Page 1:")
print(broadcast_3d_result[1])
