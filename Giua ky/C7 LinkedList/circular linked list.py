class _Node:  # tạo Node
    __slots__ = '_element','_next'  # Node chứa 2 thuộc tính _element và _next

    def __init__(self,element,next):  # phương thức khởi tạo cửa lớp _Node chứa 2 tham số là element và next trỏ tới giá trị tiếp theo
        self._element = element    # gán giá trị của  tham số element cho thuộc tính _element
        self._next = next          # gán giá trị của  tham số next cho thuộc tính _next

class CircularLinkedList:      # tạo class CircularLinkedList danh sách liên kết vòng
    def __init__(self): # phương thức khởi tạo của lớp CirLinkedList
        self._head = None # gán giá trị đầu là Null
        self._tail = None # tạo một biến tail để tham chiều của nút cuối cùng
        self._size = 0  # tạo một biến size để đếm số phần tử của danh sách liên kết vòng

    def __len__(self):  # hàm len để kiểm tra số phần tử của danh sách liên kết
        return self._size  # trả về độ dài số phần tử của danh sách liên kết

    def isempty(self):  # hàm kiểm tra danh sách liên kết có rỗng không
        return  self._size == 0   # trả vê giá trị True nếu danh sách rỗng hoặc False nếu có phần tử

    def addlast(self,e):  # hàm thêm phần tử e vào danh sách liên kết vòng
        newest=_Node(e,None) # gán biến newest có giá trị e, trỏ tới None
        if self.isempty(): # nếu danh sách liên kết đang rỗng thì
            newest._next=newest # gán giá trị trỏ kể tiếp của biến newest là địa chỉ của biến newest
            self._head=newest # gán giá trị đầu của danh sách liên kết là newest,cái này sẽ tạo thành 1 danh sách liên kết vòng trỏ giá trị cuối tời giá trị đầu của danh sách
        else: # nếu không rỗng thì
            newest._next=self._tail._next # newest sẽ trỏ vào nút đầu tiên hiện tại của danh sách liên kết( vì self._tail._next là trỏ tới giá trị đầu của danh sách)
            self._tail._next=newest # nút cuối cùng hiện tại sẽ trỏ đến nút newest thay vì giá trị đầu của dslk , làm nút newest trở thành nút cuối cùng của danh sách liên kết
        self._tail=newest #  trỏ cuối cùng của danh sách liên kết trỏ vào nut newest, newest trở thành phần tử  cuối cùng của danh sách liên kết
        self._size+=1 # tăng giá trị kích thước của danh sách liên kết

    def addfirst(self,e): # tạo hàm thêm e vào phần tử đầu của danh sách liên kết
        newest=_Node(e,None)  # nút newest chưa giá trị e và tham chiếu tới Null
        if self.isempty(): # nếu danh sách rỗng thì
            newest._next=newest #  gán  giá trị tham chiếu tiếp theo của nút newest là chính nó
            self._head=newest #  tham chiều đến nút đầu tiên là nút newest
        else: # nếu không rỗng thì
            self._tail._next=newest #  nút cuối cùng hiện tại trỏ tới nút newest
            newest._next=self._head # nút newest trỏ tới nút đầu tiên hiện tại của danh sách, làm cho nút đầu tiên thành nút thứ 2 của danh sách
        self._head=newest #  newest thành nút đầu tiên của danh sách
        self._size+=1 # tăng giá trị kích thước của danh sách

    def addany(self,e,position): # tạo hàm thêm phần tử e vào vị trí position
        newest=_Node(e,None) # nút newest chứa giá trị e, tham chiếu tới Null
        p=self._head # p trỏ tới giá trị đâu tiên của danh sách liên kết
        i=1
        while i<position-1: # chạy vòng lặp  i tới phần tử cần chèn
            p=p._next # trỏ p tham chiếu tới phần tử kế tiếp
            i=i+1 # tăng giá trị biến đếm
        newest._next=p._next # tham chiếu của nút newest trỏ tới tham chiếu của nút kế tiếp của p
        p._next=newest# tham chiếu của nút p trỏ tới nút newest, thành ra  (p -->newest--> p.next)
        self._size+=1 # tăng giá trị kích thước của danh sách liên kết vòng




    def removefirst(self):
        if self.isempty():
            print("Circular List is Empty") # in ra nếu rỗng
            return
        e= self._head._element # gán biến e là giá trị đầu tiền của danh sách liên kết
        self._tail_next = self._head._next # cập nhật tham chiếu của phần tử cuối cùng là phần tử kế tiếp của phần tử đầu tiên, tức là bỏ qua phần tử đầu tiên
        self._head= self._head._next
        self._size-=1 # giảm kích thước đi 1
        if self.isempty(): # kiểm tra lại nếu danh sách rỗng
            self._head=None # tham chiều phần tử đầu tiên = Null
            self._tail=None # tham chiều phần tử cuối cùng =Null
        return e

    def removelast(self): # tạo hàm xóa phần tử cuối cùng của danh sách lk tròn
        if self.isempty(): # kiểm tra nếu rỗng thì in ra rỗng
            print("Circular List is Empty ")
            return
        p=self._head # p trỏ giá trị đầu của danh sách liên kết
        i=1
        while i<len(self)-1: #dùng vòng lặp để chạy đến phần từ cuối trừ 1
            p=p._next # trỏ p tới phần tử kế tiếp
            i=i+1 # tăng biến đếm i
        e=p._next._element # e chứa giá trị của phần tử bị xóa
        p._next=self._head  # cập nhật trỏ kế tiếp của phần tử gần cuối là nút đầu tiên của danh sách liên kết, tức bỏ qua phần tử cuối
        self._size-=1
        return e

    def removeany(self,position):  # hàm xóa vị trí position
        p=self._head # trỏ p tới phần tử đầu  tiên của danh sách liên kết
        i=1
        while i<position-1: # chạy vòng lặp tới phần tử cạnh phần tử cần xóa
            p=p._next # trỏ p tới phần tử kế tiếp
            i=i+1# tăng biến đếm
        e=p._next._element # e là giá trị của phần tử cần xóa
        p._next=p._next._next # tham chiếu của phần tử cạnh phần tử kế phần tử cần xóa trỏ tới phần tử sau phần tử cần xóa, tức là bỏ qua phẩn tử cần xóa
        self._size-=1 # giảm giá trị kích thước danh sách liên kết
        return e # trả về giá trị đã xóa


    def display(self): # hàm để hiện ra phần tử được chèn vào
        p = self._head # p trỏ giá trị đầu của danh sách liên kết
        i=0 # gán i=0
        while i<len(self): # sử dụng vòng lặp để chạy tới phần tử cuối cùng
            print(p._element,end='-->') # in ra giá trị của p
            p = p._next # trỏ p tới phần tử kế tiếp
            i=i+1# tăng biến đếm
        print() # xuống dòng




C=CircularLinkedList()# khởi tạo danh sách liên kết vòng C
C.addlast(7) # thêm 7 vào cuối danh sách
C.addlast(4) # thêm 4  vào cuối danh sách
C.addlast(12) # thêm 12 vào cuối danh sách
C.display()# in danh sách

print("Size", len(C))# in ra size của dslk
C.addlast(8)  # thêm 8 vào cuối danh sách
C.addlast(3) # thêm  3 vào cuối danh sách
C.display() # in danh sách
print("Size", len(C))# in ra size của dslk
C.addfirst(25) # thêm  25 vào đầu  danh sách
C.display() # in danh sách
print("Size", len(C))# in ra size của dslk

C.addany(20,3) # thêm  20 vào vị trí thứ 3 trong danh sách
C.display() # in danh sách
print("Size", len(C))# in ra size của dslk

ele=C.removefirst()
C.display()
print("Size", len(C))# in ra size của dslk
print("removed element: ",ele)

elelast=C.removelast()
C.display()
print("Size", len(C))# in ra size của dslk
print("removed element: ",elelast)

eleany=C.removeany(2)
C.display()
print("Size", len(C))# in ra size của dslk
print("removed element: ",eleany)