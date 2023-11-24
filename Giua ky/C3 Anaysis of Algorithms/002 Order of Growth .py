# Tìm kiếm tuyến tính (Linear Search)
def linear_search(arr, target):
    for i, element in enumerate(arr):  # Duyệt qua từng phần tử của mảng và lấy cả giá trị và chỉ số của phần tử
        if element == target:  # So sánh giá trị của phần tử hiện tại với giá trị mục tiêu
            return i  # Nếu tìm thấy, trả về chỉ số của phần tử chứa giá trị mục tiêu
    return -1  # Trả về -1 nếu không tìm thấy giá trị mục tiêu trong mảng

# Tìm kiếm nhị phân (Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Đặt left và right để chỉ định phạm vi tìm kiếm trong mảng
    while left <= right:  # Bắt đầu vòng lặp while, tiếp tục cho đến khi left lớn hơn right
        mid = (left + right) // 2  # Tìm vị trí giữa của phạm vi tìm kiếm
        if arr[mid] == target:  # So sánh giá trị giữa với giá trị mục tiêu
            return mid  # Nếu tìm thấy, trả về chỉ số của giá trị mục tiêu trong mảng
        elif arr[mid] < target:  # Nếu giá trị giữa nhỏ hơn giá trị mục tiêu, điều này có nghĩa rằng giá trị mục tiêu nằm bên phải của giá trị giữa
            left = mid + 1  # Đặt left để tiếp tục tìm kiếm bên phải của giá trị giữa
        else:  # Nếu giá trị giữa lớn hơn giá trị mục tiêu, điều này có nghĩa rằng giá trị mục tiêu nằm bên trái của giá trị giữa
            right = mid - 1  # Đặt right để tiếp tục tìm kiếm bên trái của giá trị giữa
    return -1  # Trả về -1 nếu không tìm thấy giá trị mục tiêu trong mảng

# Một danh sách đã sắp xếp
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Giá trị mục tiêu
target = 11

# Sử dụng tìm kiếm tuyến tính
result_linear = linear_search(sorted_list, target)
if result_linear != -1:
    print(f"Tìm thấy giá trị {target} tại vị trí {result_linear} (Tìm kiếm tuyến tính).")
else:
    print(f"Không tìm thấy giá trị {target} trong danh sách (Tìm kiếm tuyến tính).")

# Sử dụng tìm kiếm nhị phân
result_binary = binary_search(sorted_list, target)
if result_binary != -1:
    print(f"Tìm thấy giá trị {target} tại vị trí {result_binary} (Tìm kiếm nhị phân).")
else:
    print(f"Không tìm thấy giá trị {target} trong danh sách (Tìm kiếm nhị phân).")
