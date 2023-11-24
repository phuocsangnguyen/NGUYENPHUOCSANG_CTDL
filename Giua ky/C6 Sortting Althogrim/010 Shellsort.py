def shellsort(A):                           #định nghĩa một hàm có tên là shellsort() với tham số đầu vào là một mảng A.
    n = len(A)                              #tính độ dài của mảng A và lưu trữ nó trong biến n.
    gap = n//2                               #tính toán khoảng cách ban đầu giữa các phần tử được so sánh, bằng với nửa độ dài của mảng A.
    while gap > 0:                          #bắt đầu một vòng lặp while lặp chừng nào khoảng cách gap còn lớn hơn 0.
        i = gap                             #khởi tạo một biến i bằng với khoảng cách gap.
        while i < n:                        #bắt đầu một vòng lặp while lặp chừng nào biến i còn nhỏ hơn độ dài của mảng A.
            temp = A[i]                     #lưu trữ giá trị của phần tử tại vị trí i của mảng A trong một biến tạm thời temp.
            j = i - gap                     #khởi tạo một biến j bằng với vị trí i trừ đi khoảng cách gap
            while j >= 0 and A[j] > temp:   # bắt đầu một vòng lặp while lặp chừng nào biến j còn lớn hơn hoặc bằng 0 và phần tử tại vị trí j của mảng A còn lớn hơn biến temp.
                A[j+gap] = A[j]             #di chuyển phần tử tại vị trí j của mảng A sang vị trí j + gap.
                j = j - gap                 #giảm giá trị của biến j đi khoảng cách gap.
            A[j + gap] = temp               #lưu trữ giá trị của biến temp vào vị trí j + gap của mảng A.
            i = i+1                         #tăng giá trị của biến i lên 1.
        gap = gap // 2                      #giảm giá trị của khoảng cách gap đi một nửa.

A = [3,5,8,9,6,2]
print('Original Array:', A)
shellsort(A)
print('sorted array: ' , A)