def quicksort(A, low, high):    
    if low < high:  # Nếu chỉ số `low` nhỏ hơn `high`, tức là dãy cần sắp xếp có nhiều hơn một phần tử.
        pi = partition(A, low, high)
        # Gọi hàm partition để chọn phần tử chốt (pivot) và đặt nó vào đúng vị trí. `pi` là chỉ số của pivot sau khi sắp xếp.  
        quicksort(A, low, pi-1) # Sắp xếp nửa bên trái của pivot bằng cách gọi đệ quy với phạm vi từ `low` đến `pi-1`.
        quicksort(A,pi+1,high)  # Sắp xếp nửa bên phải của pivot bằng cách gọi đệ quy với phạm vi từ `pi+1` đến `high`.

def partition(A, low, high):     #chọn pivot là phần tử đầu tiên của A
    pivot = A[low]  # Chọn phần tử chốt là phần tử đầu tiên trong phạm vi (ở chỉ số `low`).
    i = low + 1 # Điểm bắt đầu của i là chỉ số sau pivot
    j = high    # Điểm bắt đầu của  j là chỉ số cuối cùng trong phạm vi.
    while True:
        while i <= j and A[i] <= pivot: # Dòng này tìm một phần tử bên trái của pivot mà lớn hơn pivot.
            i = i + 1
        while i <= j and A[j] > pivot:# Dòng này tìm một phần tử bên phải của pivot mà nhỏ hơn hoặc bằng pivot.
            j = j - 1
        if i <= j:              # Nếu i không vượt qua j, đồng nghĩa với việc tìm thấy một cặp phần tử cần hoán đổi.
            A[i], A[j] = A[j], A[i] # Hoán đổi chỗ hai phần tử
        else:   # nếu i lớn hơn j thì thoát vòng lặp
            break
    A[low], A[j] = A[j], A[low] # Hoán đổi chỗ phần tử chốt (pivot) với phần tử ở vị trí `j` (vị trí sau khi sắp xếp).
    return j    # Trả về vị trí của pivot sau khi sắp xếp.

A = [1,5,8,9,6,2]
print('Original Array:', A)
quicksort(A, 0, len(A)-1)
print('Sorted Array:', A)
# In ra mảng đã sắp xếp.