def best_case_linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
        elif element > target:
            break
    return -1

# Tạo một danh sách đã sắp xếp có các số nguyên từ 1 đến 10
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Giá trị mục tiêu cần tìm trong danh sách
target = 3

# Thực hiện tìm kiếm trong trường hợp tốt nhất
result_best_case = best_case_linear_search(sorted_list, target)

if result_best_case != -1:
    print(f"Kết quả tìm kiếm trong trường hợp tốt nhất: Giá trị {target} được tìm thấy tại vị trí {result_best_case}.")
else:
    print(f"Kết quả tìm kiếm trong trường hợp tốt nhất: Giá trị {target} không tồn tại trong danh sách.")
