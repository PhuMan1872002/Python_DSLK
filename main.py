import os
import msvcrt
import time
from DSSV import *
student_list=DanhSachSinhVien()
student_list.__init__()

while True:
  print("1) Nhập dữ liệu sinh viên từ file text")
  print("2) In danh sách sinh viên")
  print("3) Tìm kiếm in thông tin theo MSSV")
  print("4/Thêm sinh viên vào danh sách không được trùng MSSV")
  print("5/Xóa sinh viên theo MSSV")
  print("6/Thoát")
  choice = input("Enter Choice: ")
  
  choice = choice.strip()
   
  
  if (choice == "1"):
    with open("Data.txt") as f:
        for line in f:
            data = line.strip().split('-')
            student_list.themSinhVien(data[0], data[1], data[2],data[3],data[4])
    time.sleep(1)
    os.system('cls')
  elif (choice == "2"):
        student_list.inDanhSachSinhVien()
        time.sleep(1)
        os.system('cls')
  elif (choice == "3"):
        MSSV=input("Nhập mssv: ")
        student_list.timKiemSinhVien(MSSV)
        time.sleep(1)
        os.system('cls')
  elif (choice == "4"):
        print("Mời nhập thông tin sinh viên cần thêm: ")
        MSSV=input("Nhập mssv: ")
        Ho=input("Nhập họ: ")
        Ten=input("Nhập tên: ")
        Diem1=input("Nhập điểm môn 1: ")
        Diem2=input("Nhập điểm môn 2: ")
        student_list.themSinhVien(MSSV,Ho,Ten,Diem1,Diem2)
        time.sleep(1)
        os.system('cls')
  elif (choice=="5"):
    MSSV=input("Mời nhập MSSV của sinh viên cần xóa khỏi danh sách: ")
    student_list.xoaSinhVien(MSSV)
    time.sleep(1)
    os.system('cls')
  else:
    break


