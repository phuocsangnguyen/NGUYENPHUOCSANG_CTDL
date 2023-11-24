def selectionsort(A):    # hàm sắp xếp kiểu selectionsort
   n= len(A) # gán n là chiều dài của A
   for i in range(n-1): #  chạy vòng lặp i tới n-1
        position=i # gán position là giá trị vị trí của giá trị nhỏ nhất
        for j in range(i+1,n): # chạy vòng lặp j từ i+1 tới n
            if A[j] < A[position]:# kiểm tra nếu A[j] <A[position](là phần tử nhỏ nhất đã duyệt đến) thì position sẽ gán với j(là giá trị nhỏ nhất mới duyệt đến)
                position =j # position sẽ gán với j(là giá trị nhỏ nhất mới duyệt đến)
            temp=A[i]          # đổi giá trị A[i] với giá trị nhỏ vừa duyệt đến là A[position]
            A[i]=A[position]   # đổi giá trị A[i] với giá trị nhỏ vừa duyệt đến là A[position]
            A[position]=temp   # đổi giá trị A[i] với giá trị nhỏ vừa duyệt đến là A[position]
        
A = [ 5,2,7,6,9,8]  # Khởi tạo danh sách A cần sắp xếp
print ('Original Array: ',A)    # In ra danh sách ban đầu
selectionsort(A)            # Gọi hàm sắp xếp chèn với đầu vào là danh sách A
print('Sort Array: ',A)      # In ra danh sách sau khi đã sắp xếp