# Tìm kiếm tuyến tính (Linear Search)
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Tìm kiếm nhị phân (Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Một danh sách có 1 triệu số nguyên đã sắp xếp từ 1 đến 1.000.000
sorted_list = list(range(1, 1000001))

# Tìm kiếm giá trị 500.000 trong danh sách
target = 500000

# Sử dụng tìm kiếm tuyến tính
result_linear = linear_search(sorted_list, target)

# Sử dụng tìm kiếm nhị phân
result_binary = binary_search(sorted_list, target)

print(f"Kết quả tìm kiếm tuyến tính: Phần tử {target} được tìm thấy tại vị trí {result_linear} trong danh sách.")
print(f"Kết quả tìm kiếm nhị phân: Phần tử {target} được tìm thấy tại vị trí {result_binary} trong danh sách.")
