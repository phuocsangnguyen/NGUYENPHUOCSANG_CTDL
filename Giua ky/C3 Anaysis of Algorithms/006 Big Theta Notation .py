# Định nghĩa hàm linear_search nhận một danh sách arr và một giá trị target làm đối số
def linear_search(arr, target):
    # Duyệt qua từng phần tử trong danh sách sử dụng vòng lặp for
    for i, element in enumerate(arr):
        # Kiểm tra nếu phần tử hiện tại bằng với giá trị mục tiêu
        if element == target:
            # Trả về vị trí của giá trị mục tiêu nếu tìm thấy
            return i
    # Trả về -1 nếu không tìm thấy giá trị mục tiêu trong danh sách
    return -1

# Tạo một danh sách có n phần tử, trong trường hợp này, n = 1000
n = 1000
sample_list = list(range(1, n + 1))

# Giá trị mục tiêu cần tìm trong danh sách, trong trường hợp này, target = 500
target = 500

# Thực hiện tìm kiếm trong trường hợp trung bình
result_average_case = linear_search(sample_list, target)

# Kiểm tra kết quả tìm kiếm và in thông báo tương ứng
if result_average_case != -1:
    print(f"Kết quả tìm kiếm trong trường hợp trung bình: Giá trị {target} được tìm thấy tại vị trí {result_average_case}.")
else:
    print(f"Kết quả tìm kiếm trong trường hợp trung bình: Giá trị {target} không tồn tại trong danh sách.")
