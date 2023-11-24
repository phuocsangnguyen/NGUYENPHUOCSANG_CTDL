def mergesort(A,left,right):
    # Hàm mergesort nhận vào mảng A cùng với chỉ số bắt đầu (left) và chỉ số kết thúc (right) của phạm vi cần sắp xếp.
    if left<right: # Kiểm tra xem phạm vi cần sắp xếp có nhiều hơn một phần tử không (tức là left < right).
        mid=(left+right)//2 # Tìm giữa của phạm vi để chia mảng thành hai nửa.
        mergesort(A,left,mid)    # Gọi đệ quy để sắp xếp nửa bên trái của mảng.
        mergesort(A,mid+1,right) # Gọi đệ quy để sắp xếp nửa bên phải của mảng.
        merge(A,left,mid,right)  # Gộp hai nửa đã sắp xếp lại với nhau.
def merge(A,left,mid,right):
    # Hàm merge nhận vào mảng A và chỉ số bắt đầu (left), chỉ số giữa (mid), và chỉ số kết thúc (right) của phạm vi cần gộp.
    i=left # Khởi tạo các biến chỉ số.
    j=mid+1
    k=left
    B=[0]*(right+1) # Tạo một mảng tạm thời B để lưu kết quả gộp.
    while i<=mid and j<=right:  # Lặp qua cả hai nửa của mảng và so sánh phần tử.
        if A[i]<A[j]:  # So sánh phần tử từ nửa bên trái và nửa bên phải, chọn phần tử nhỏ hơn.
            B[k]=A[i] # Lưu phần tử nhỏ hơn vào mảng kết quả.
            i=i+1 # Di chuyển chỉ số i để xem phần tử tiếp theo trong nửa bên trái.
        else:
            B[k]=A[j] # Tương tự, lưu phần tử nhỏ hơn vào mảng kết quả và di chuyển chỉ số j hoặc k.
            j=j+1
        k=k+1
    while i<= mid : # Sao chép phần còn lại của nửa bên trái (nếu còn).
        B[k]=A[i]
        i=i+1
        k=k+1
    while j<=right:  # Sao chép phần còn lại của nửa bên phải (nếu còn).
        B[k]=A[j]
        j=j+1
        k=k+1
    for x in range(left,right+1): # Sao chép kết quả từ mảng tạm thời B vào mảng ban đầu A.
        A[x]=B[x]

A=[4,6,8,7,6,2]
print("Original Array", A)
mergesort(A,0,len(A)-1)
print("Sorted Array ",A) 