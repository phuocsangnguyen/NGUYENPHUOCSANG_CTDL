def insertionsort(A):       # Định nghĩa hàm sắp xếp chèn với đầu vào là một danh sách A
    n = len(A)              # Lấy độ dài của danh sách A
    for i in range(1,n):    # Duyệt qua từng phần tử của danh sách, bắt đầu từ phần tử thứ hai 
        cvalue = A[i]       # Lưu giá trị hiện tại cần được chèn vào phần đã sắp xếp của danh sách
    position = i            # Lưu vị trí hiện tại của giá trị cvalue trong danh sách
    while position > 0 and A[ position -1 ] > cvalue: # Nếu vị trí hiện tại lớn hơn 0 và giá trị tại vị trí trước đó lớn hơn giá trị cvalue
            A[position] = A[ position -1 ]       # Di chuyển giá trị lớn hơn về sau một vị trí
            position = position - 1             # Giảm vị trí hiện tại đi 1
            A[position] = cvalue            # Chèn giá trị cvalue vào vị trí phù hợp
        
A = [4,5,9,8,6,2]               # Khởi tạo danh sách A cần sắp xếp
print('Original Array:', A)     # In ra danh sách ban đầu
insertionsort(A)                # Gọi hàm sắp xếp chèn với đầu vào là danh sách A
print('Sorted Array:', A)       # In ra danh sách sau khi đã sắp xếp