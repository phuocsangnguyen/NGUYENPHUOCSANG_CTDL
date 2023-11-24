def radixsort(A): #định nghĩa một hàm có tên là radixsort(), nhận vào một mảng A.
    n = len(A)     #tính độ dài của mảng A.
    maxelement = max(A)  #tìm phần tử lớn nhất trong mảng A
    digits = len (str(maxelement))   #tính số chữ số của phần tử lớn nhất trong mảng A.
    l = []      #khởi tạo một danh sách l trống.
    bins = [l] * 10     #khởi tạo một danh sách bins chứa 10 danh sách trống.
    for i in range (digits):    #bắt đầu một vòng lặp for lặp digits lần
        for j in range (n):     #bắt đầu một vòng lặp for lặp n lần.
            e = int((A[j]) / pow(10,i)) % 10    #Dòng này tính chữ số thứ i của phần tử thứ j trong mảng A.
            if len(bins[e]) > 0:    #kiểm tra xem danh sách bins[e] có trống hay không.
                bins[e].append(A[j])    #Nếu danh sách bins[e] không trống, thì phần tử thứ j của mảng A sẽ được thêm vào danh sách bins[e].
            else:
                bins[e].append(A[j])    #Nếu danh sách bins[e] không trống, thì phần tử thứ j của mảng A sẽ được thêm vào danh sách bins[e].
                bins[e] = [A[j]]    
        k = 0
        for x in range(10): #khởi tạo một biến k bằng 0 và bắt đầu một vòng lặp for lặp 10 lần.
            if len(bins[x]) > 0:   #kiểm tra xem danh sách bins[x] có trống hay không.
                for y in range(len(bins[x])):   
                    A[k] = bins[x].pop(0)   #Nếu danh sách bins[x] không trống, thì tất cả các phần tử trong danh sách bins[x] sẽ được thêm vào mảng A theo thứ tự, bắt đầu từ vị trí k.
                    k = k+1      #Biến k sẽ được tăng lên 1 sau mỗi lần thêm một phần tử vào mảng A.
                    
A = [28,115,435,650,760,54]
print('Original Array:', A)
radixsort(A)
print('Sorted Array:' ,A)
    