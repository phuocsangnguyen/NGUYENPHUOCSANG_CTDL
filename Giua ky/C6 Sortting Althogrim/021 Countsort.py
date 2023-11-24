def countsort(A):  # Định nghĩa hàm sắp xếp đếm với đầu vào là một danh sách A
    n = len (A)  # Lấy độ dài của danh sách A
    maxsize = max(A)  # Tìm giá trị lớn nhất trong danh sách A
    carray = [0] * (maxsize + 1)  # Khởi tạo một danh sách carray với kích thước bằng maxsize + 1, tất cả các phần tử đều bằng 0
    for i in range(n):  # Duyệt qua từng phần tử của danh sách A
        carray [A[i]] = carray[A[i]] + 1  # Tăng giá trị tại vị trí tương ứng trong carray lên 1
    i = 0
    j = 0
    while i < maxsize + 1 :  # Duyệt qua từng phần tử của carray
        if carray[i] > 0 :  # Nếu giá trị tại vị trí hiện tại lớn hơn 0
            A[j] = i   # Gán giá trị đó vào danh sách A
            j = j + 1
            carray[i] = carray[i] - 1   # Giảm giá trị tại vị trí hiện tại trong carray đi 1
        else:
            i = i + 1   # Nếu không, tăng i lên 1 


A = [2,5,7,8,7,2,3,5,5]
print('Original Array:', A)
countsort(A)
print('Sorted Array:',A)