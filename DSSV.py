class Node:
    def __init__(self, mssv, ho, ten, diem1, diem2):
        self.mssv = mssv
        self.ho = ho
        self.ten = ten
        self.diem1 = float(diem1)
        self.diem2 = float(diem2)
        self.next = None
        self.prev = None

class DanhSachSinhVien:
    def __init__(self):
        self.head = None

    def themSinhVien(self, mssv, ho, ten, diem1, diem2):
        new_node = Node(mssv, ho, ten, diem1, diem2)
        if self.head is None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.mssv == mssv:
                print("Sinh viên đã tồn tại trong danh sách")
                return
            curr_node = curr_node.next
        
        if curr_node.mssv == mssv:
            print("Sinh viên đã tồn tại trong danh sách")
            return
        curr_node.next = new_node
        new_node.prev = curr_node

    def xoaSinhVien(self, mssv):
        curr_node = self.head

        if curr_node is not None:
            if curr_node.mssv == mssv:
                self.head = curr_node.next
                curr_node.next.prev = None
                curr_node = None
                return

        while curr_node is not None:
            if curr_node.mssv == mssv:
                if curr_node.next is not None:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                else:
                    curr_node.prev.next = None
                curr_node = None
                return
            curr_node = curr_node.next

        print("Không tìm thấy sinh viên có mã số", mssv)

    def timKiemSinhVien(self, mssv):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.mssv == mssv:
                diem_trung_binh = (curr_node.diem1 + curr_node.diem2) / 2
                print("MSSV:", curr_node.mssv)
                print("Họ và tên:", curr_node.ho, curr_node.ten)
                print("Điểm môn 1:", curr_node.diem1)
                print("Điểm môn 2:", curr_node.diem2)
                print("Điểm trung bình:", diem_trung_binh)
                return
            curr_node = curr_node.next
        print("Không tìm thấy sinh viên có mã số", mssv)

    def inDanhSachSinhVien(self):
        curr_node = self.head
        while curr_node is not None:
            diem_trung_binh = (curr_node.diem1 + curr_node.diem2) / 2
            print("MSSV:", curr_node.mssv)
            print("Họ và tên:", curr_node.ho, curr_node.ten)
            print("Điểm môn 1:", curr_node.diem1)
            print("Điểm môn 2:", curr_node.diem2)
            print("Điểm trung bình:",diem_trung_binh)
            curr_node=curr_node.next

   
