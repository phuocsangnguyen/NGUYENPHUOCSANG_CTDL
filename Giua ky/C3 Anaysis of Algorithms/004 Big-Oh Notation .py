import time

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

# Tạo một danh sách đã sắp xếp có 1 triệu số nguyên từ 1 đến 1 triệu
sorted_list = list(range(1, 1000001))

# Tìm kiếm giá trị 500,000 trong danh sách
target = 500000

# Đo thời gian thực thi của tìm kiếm tuyến tính
start_time = time.time()
result_linear = linear_search(sorted_list, target)
end_time = time.time()
print(f"Kết quả tìm kiếm tuyến tính: {result_linear}")
print(f"Thời gian tìm kiếm tuyến tính: {end_time - start_time} giây")

# Đo thời gian thực thi của tìm kiếm nhị phân
start_time = time.time()
result_binary = binary_search(sorted_list, target)
end_time = time.time()
print(f"Kết quả tìm kiếm nhị phân: {result_binary}")
print(f"Thời gian tìm kiếm nhị phân: {end_time - start_time} giây")
