# Định nghĩa hàm sum_of_array nhận một mảng arr làm đối số
def sum_of_array(arr):
    # Tạo một biến cố định total để lưu trữ tổng các phần tử
    total = 0  # O(1) - Constant Space Complexity

    # Duyệt qua từng phần tử trong mảng arr
    for num in arr:
        # Cộng giá trị của phần tử vào tổng
        total += num  # O(1) - Constant Space Complexity

    # Trả về tổng
    return total  # O(1) - Constant Space Complexity

# Tạo một mảng với 1 triệu phần tử
arr = list(range(1, 1000001))  # O(n) - Linear Space Complexity, n là kích thước của mảng

# Gọi hàm sum_of_array để tính tổng mảng và lưu vào biến result
result = sum_of_array(arr)  # O(1) - Constant Space Complexity

# In ra tổng của mảng
print(f"Tổng của mảng là: {result}")  # O(1) - Constant Space Complexity
