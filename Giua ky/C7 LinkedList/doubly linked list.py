class _Node:  # tạo Node
    __slots__='_element','_next','_prev'  # Node chứa 3 thuộc tính _element,_next, _prev

    def __init__(self,element,next,prev): # phương thức khởi  tạo lớp Node chứa element,next,prev
        self._element=element # gán giá trị của  tham số element cho thuộc tính _element
        self._next=next    # gán giá trị của  tham số next cho thuộc tính _next
        self._prev=prev  # gán giá trị của  tham số prev cho thuộc tính _prev


class DoublyLinkedList:  # tạo class DoublyLinkedList danh sách liên kết đôi
    def __init__(self):    # phương thức khởi tạo các thuộc tính ban đầu cho đối tượng DoublyLinkedList
        self._head=None # trỏ giá trị đầu dslk là Null
        self._tail=None # trỏ giá trị cuối của dslk là Null
        self._size=0      # khởi tạo số phần tử ban đầu = 0

    def __len__(self):  # hàm trả về kích thước của dslk
        return self._size

    def isempty(self):      # hàm kiểm tra dslk có rỗng không
        return self._size == 0


    def addlast(self,e):      # hàm truyền phần tử e vào cuối danh sách liên kết
        newest=_Node(e,None,None) # nút newest chứa giá trị e, trỏ đầu và cuối tới Null
        if self.isempty(): # kiểm tra xem dslk có rỗng không
            self._head=newest # nếu rỗng thì trỏ giá trị đầu  tới phần tử thêm vào
            self._tail=newest # nếu rỗng  thì trỏ giá trị cuối tới phần tử thêm vào
        else: # nếu không rỗng
            self._tail._next=newest # trỏ phần tử kế tiếp của phần tử cuối cùng hiện tại là nút newest
            newest._prev=self._tail # trỏ phần trước của newest là phần tử cuối cùng hiện tại
            self._tail=newest # biến nút newest trở thành phần tử cuối cùng của danh sách liên kết
        self._size+=1 # tăng kích thước của danh sách liên kết


    def addfirst(self,e):# hàm thêm phần tử vào đầu danh sách
        newest=_Node(e,None,None)  # nút newest chứa giá trị e, trỏ đầu và cuối tới Null
        if self.isempty():# kiểm tra xem dslk có rỗng không
            self._head=newest# nếu rỗng thì trỏ giá trị đầu  tới phần tử thêm vào
            self._tail=newest# nếu rỗng  thì trỏ giá trị cuối tới phần tử thêm vào
        else:# nếu không rỗng
            newest._next=self._head # phân tử kế tiếp của nút newest là phần tử đầu hiện tại, để đẩy phần tử đầu lên vị trí 2
            self._head._prev=newest # gán trỏ trước của phần từ đầu là nút newest
            self._head=newest # nút newest thành nút đầu của dslk
        self._size+=1# tăng kích thước dslk

    def display(self): # hiện thị danh sách liên kết theo chiều xuôi tử dầu tới cuối
        p=self._head # p trỏ tới phần tử đầu của dslk
        while p: # chừng nào còn trỏ tới có giá trị
            print(p._element,end="-->") # in ra giá trị của nút đó
            p=p._next # duyệt tới phần tử kế tiếp
        print()

    def addany(self,e,position): # hàm thêm vào vị trí position
        newest=_Node(e,None,None) # nút newest chứa giá trị e, trỏ đầu và cuối tới Null
        p=self._head #p trỏ tới phần tử đầu tiên
        i=1
        while i<position-1: # duyệt tới phần tử cần chèn trừ 1
            p=p._next # duyệt tới phần tử kế tiếp
            i=i+1 #tăng biến đếm
        newest._next=p._next # trỏ kế tiếp của nút newest tại nút cần chèn, đầy nút đó lui vị trí tiếp theo
        p._next._prev=newest # đặt lại trỏ trước tại nút cần chèn là nút newest để hoàn thành nối nút newest với nút ngay tại chỗ chèn vào
        p._next=newest # trỏ  của nút trước cần chèn nối với nút newest
        newest._prev=p # trỏ trước của nút newest nối với nút trước nút cần chèn để nối nút trước nó với nút newest
        self._size+=1 # tăng kích  thước dslk


    def removefirst(self):  # hàm xóa vị trí đầu
        if self.isempty(): # kiểm tra nếu rỗng thì in ra rỗng
            print("Circular List is Empty ")# in ra rỗng
            return
        e=self._head._element # gán e là giá trị của nút đầu
        self._head=self._head._next # biến nút thứ 2 thành trỏ của phần tử đầu của danh sách liên kết
        self._head._prev=None # nối trỏ đầu của phần tử thứ 2 lúc đầu( phần tử đầu của dslk hiện tại) với Null
        self._size-=1# giảm kích thước  dslk
        if self.isempty():# kiểm tra lại nếu sau khi xóa dslk rỗng thì gán giá trị cuoi
            self._tail=None
        return e

    def removelast(self): # xòa vị trí cuối
        if self.isempty(): # kiểm tra nếu rỗng thì in ra rỗng
            print("Circular List is Empty ")# in ra rỗng
            return
        e=self._tail._element # gán e là giá trị cuối của nút cuối
        self._tail=self._tail._prev # gán trỏ giá trị cuối hiện tại của danh sách là nút trước nó
        self._tail._next=None # gán trỏ tới của giá trị cuối hiện sau khi xóa nút cuối là Null
        self._size-=1 # giảm kích thước dslk
        return e # trả về giá trị đã xóa


    def removeany(self,position): # hàm xóa tại vị trí bất kỳ
        p=self._head # p trỏ tới nút đầu của dslk
        i=1
        while i<position-1: # vòng lặp tới phần tử position -1
            p=p._next # duyệt trỏ p tới địa chỉ phần tử kể tiếp
            i=i+1# tăng biến đếm
        e=p._next._element # gán e là giá trị của nút tại vị trí position
        p._next=p._next._next # gán trỏ tới của vị trí (position-1) là vị trị của (position+1)
        p._next._prev = p # gán trỏ trước của nút (postion+1) là vị trí nút (position-1)
        self._size -=1 # giảm kích thước dslk
        return  e # trả về giá trị  bị xóa

    def displayrev(self): # hiển thị danh sách liên kết theo chiều ngược lại tử cuối về đầu
        p=self._tail # p trỏ tới phần tử cuối
        while p: # chừng nào còn trỏ tới có giá trị
            print(p._element,end="-->")# in ra giá trị của nút đó
            p=p._prev  # duyệt tới phần tử trước nó
        print()

L=DoublyLinkedList()# khởi tạo danh sách liên kết đôi L
L.addlast(7) # thêm 7 vào cuối danh sách
L.addlast(4)# thêm 4 vào cuối danh sách
L.addlast(12)# thêm vào cuối danh sách
L.display() # hiển thi danh sách chiều xuôi
print('Size',len(L))# kích thước dslk
L.displayrev()# hiện thị danh sách chiều ngược
L.addlast(8)# thêm 8 vào cuối danh sách
L.addlast(3)# thêm 3 vào cuối danh sách
L.display() #  hiển thi danh sách chiều xuôi
print('Size',len(L))# kích thước dslk

L.addfirst(25) # thêm 25 vào đầu danh sách
L.display()

L.addany(25,3)
L.display()

L.removefirst()
L.display()

L.removelast()
L.display()
L.addlast(25)
L.display()

ele=L.removeany(3)
L.display()
print(ele)