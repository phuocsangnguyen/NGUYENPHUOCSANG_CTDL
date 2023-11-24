# O(1) - Constant Time Complexity

# Định nghĩa hàm print_first_element nhận một mảng arr làm đối số
def print_first_element(arr):
    # In ra phần tử đầu tiên của mảng
    print(arr[0])

# Tạo một mảng có giá trị từ 1 đến 5
arr = [1, 2, 3, 4, 5]
# Gọi hàm print_first_element để in ra phần tử đầu tiên của mảng
print_first_element(arr)
# In ra kết quả
print("Phần tử đầu tiên của mảng là:", arr[0])


# O(n) - Linear Time Complexity

# Định nghĩa hàm linear_search nhận một mảng arr và một giá trị target làm đối số
def linear_search(arr, target):
    # Duyệt qua từng phần tử trong mảng
    for element in arr:
        # Kiểm tra nếu phần tử hiện tại bằng giá trị target
        if element == target:
            # Trả về True nếu tìm thấy target
            return True
    # Trả về False nếu không tìm thấy target trong mảng
    return False

# Tạo một mảng
arr = [1, 2, 3, 4, 5]
# Giá trị mục tiêu để tìm kiếm trong mảng
target = 3
# Gọi hàm linear_search để kiểm tra xem target có tồn tại trong mảng hay không
result = linear_search(arr, target)
# In ra kết quả
if result:
    print(f"{target} tồn tại trong mảng.")
else:
    print(f"{target} không tồn tại trong mảng.")


# O(n^2) - Quadratic Time Complexity

# Định nghĩa hàm bubble_sort nhận một mảng arr làm đối số
def bubble_sort(arr):
    n = len(arr)  # Độ dài của mảng
    for i in range(n):  # Vòng lặp bên ngoài: lặp qua từng phần tử của mảng
        for j in range(0, n-i-1):  # Vòng lặp bên trong: lặp qua các phần tử chưa được sắp xếp
            if arr[j] > arr[j+1]:  # So sánh hai phần tử liền kề
                # Nếu phần tử hiện tại lớn hơn phần tử kế tiếp, hoán đổi chúng
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Tạo một mảng chưa sắp xếp
arr = [5, 2, 9, 3, 1]
# Sử dụng thuật toán Bubble Sort để sắp xếp mảng arr (thay đổi mảng gốc)
bubble_sort(arr)
# In ra mảng sau khi sắp xếp
print("Mảng sau khi sắp xếp:", arr)


# O(log n) - Logarithmic Time Complexity

# Định nghĩa hàm binary_search nhận một mảng arr và một giá trị target làm đối số
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Đặt biến left và right để chỉ định phạm vi tìm kiếm trong mảng.
    while left <= right:  # Bắt đầu vòng lặp while, tiếp tục cho đến khi left lớn hơn right.
        mid = (left + right) // 2  # Tìm vị trí giữa của phạm vi tìm kiếm.
        if arr[mid] == target:  # So sánh phần tử giữa với giá trị mục tiêu.
            return mid  # Trả về vị trí của giá trị mục tiêu nếu tìm thấy.
        elif arr[mid] < target:  # Nếu giá trị giữa nhỏ hơn giá trị mục tiêu, điều này có nghĩa rằng giá trị mục tiêu nằm ở bên phải của giá trị giữa.
            left = mid + 1  # Đặt left để tiếp tục tìm kiếm bên phải của giá trị giữa.
        else:  # Nếu giá trị giữa lớn hơn giá trị mục tiêu, điều này có nghĩa rằng giá trị mục tiêu nằm ở bên trái của giá trị giữa.
            right = mid - 1  # Đặt right để tiếp tục tìm kiếm bên trái của giá trị giữa.
    return -1  # Trả về -1 nếu không tìm thấy giá trị mục tiêu trong mảng.


# Tạo một mảng đã được sắp xếp
arr = [1, 2, 3, 4, 5]
# Giá trị mục tiêu để tìm kiếm trong mảng
target = 3
# Gọi hàm binary_search để tìm vị trí của target trong mảng (hoặc -1 nếu không tìm thấy)
result = binary_search(arr, target)
# In ra kết quả
if result != -1:
    print(f"{target} được tìm thấy tại vị trí {result}.")
else:
    print(f"{target} không được tìm thấy trong mảng.")
