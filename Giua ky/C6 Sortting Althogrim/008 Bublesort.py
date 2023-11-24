def bubblesort(A):  # hàm sắp xếp bubblesort
    n = len(A)      # n là độ dài của A
    for passes in range (n-1,0,-1):     # vòng lặp giảm dần tử n-1 xuống 0, mỗi lần -1
        for i in range (passes):    # vòng lặp chạy từ i đến passes(passes là phần tử kế cuối) (passes+1 là phần tử cuối )
            if A[i] > A[i+1]:    # so sánh 2 số cạnh nhau nếu số trước lớn hơn số sau thì đổi vị trí, để chuyển phần tử lớn nhất từ từ chuyển về cuối A
                temp =A[i]      # đổi vị trí A[i] với A[i+1]
                A[i] = A[i+1]   # đổi vị trí A[i] với A[i+1]
                A[i+1] = temp   # đổi vị trí A[i] với A[i+1]
                
A = [3,5,8,9,6,2]
print ('Original Array:' ,A)    # in ra dòng chưa sắp xếp
bubblesort(A)
print ('Sort Array:' ,A)    # in ra dòng đã sắp xếp
                
