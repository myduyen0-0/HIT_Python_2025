# TruongMyDuyen_Buoi1
## Bai1:
-Python là ngôn ngữ thông dịch.
+ Mã nguồn được thực thi trực tiếp mà không cần qua bước biên dịch thành mã máy hoàn chỉnh như C/C++.
+ Khi chạy một chương trình Python, trình thông dịch sẽ chuyển mã nguồn thành mã bytecode, sau đó thực thi nó trong Python Virtual Machine (PVM).
+ Việc sử dụng thông dịch giúp Python dễ phát triển, gỡ lỗi và tương tác nhanh với người lập trình hơn.
## Bai2:
1. Các kiểu dữ liệu trong Python
- int: số nguyên (a = 10)
- float: số thực (pi = 3.14)
- str: chuỗi (name = "Python")
- bool: kiểu logic (flag = True)
- list: danh sách (lst = [1, 2, 3])
- tuple: bộ giá trị bất biến (t = (1, 2, 3))
- dict: từ điển (d = {"name": "Alice", "age": 20})
- set: tập hợp (s = {1, 2, 3})
2. Các toán tử trong Python
- Toán tử số học: +,-,*,/,//,%,**
- Toán tử so sánh: ==,!=,>,<,>=,<=
- Toán tử logic: and,or,not
- Toán tử gán: =,+=,-=,*=,/=,%=
- Toán tử membership: in,not in
- Toán tử identity: is,is not
 3. Mệnh đề điều kiện và vòng lặp
-Câu lệnh điều kiện:
+ if condition: thực hiện nếu điều kiện đúng
+ elif another_condition: thực hiện nếu điều kiện khác đúng
+ else: thực hiện nếu tất cả điều kiện sai
-Vòng lặp:
+ Vòng lặp for:
for i in range(5):
    print(i)
+ Vòng lặp while:
count = 0
while count < 5:
    print(count)
    count += 1
4. Kiểu dữ liệu True, False (kiểu Boolean)
- True và False là hai giá trị boolean trong Python.
- Dùng để kiểm tra điều kiện trong các cấu trúc điều khiển như if, while,...
- Một số giá trị mặc định sẽ được coi là False trong biểu thức điều kiện như: 
+ 0, 0.0
+ (chuỗi rỗng)
+ [], {}, set() (các container rỗng)
+ None
Ví dụ:
if not []:
    print("Danh sách rỗng được xem là False")
