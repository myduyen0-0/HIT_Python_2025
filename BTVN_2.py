#bai1:
def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ!"

thang=int(input("Nhap thang: "))
nam=int(input("Nhap nam: "))
ketqua=songay(thang,nam)
    
print(f"So ngay trong thang {thang} nam {nam} la: {ketqua}")
#bai2:
def tinh_thue(luong):
    if luong >= 15000000:
         thue = luong * 0.3
    elif luong >= 7000000:
         thue = luong * 0.2
    else:
         thue = luong * 0.1
    return thue

def tinh_luong_rong(luong):
    thue = tinh_thue(luong)
    return luong - thue, thue
luong = int(input("Nhập lương nhân viên: "))
luong_rong, thue = tinh_luong_rong(luong)
print(f"Thuế: {int(thue)} Thu nhập: {int(luong_rong)}")
#bai3:
def dem_chu_so(n):
    return len(str(n))

def tong_chu_so(n):
    return sum(int(ch) for ch in str(n))

n = int(input("Nhập số nguyên n: "))
so_chu_so = dem_chu_so(n)
tong = tong_chu_so(n)
print(f"Số chữ số: {so_chu_so} Tổng chữ số: {tong}")

#bai4:
def so_chai_bia(n_xu):
    gia_bia = 28
    chai_ban_dau = n_xu // gia_bia
    so_chai = chai_ban_dau
    vo_chai = chai_ban_dau

    while vo_chai >= 3:
        doi_duoc = vo_chai // 3
        so_chai += doi_duoc
        vo_chai = vo_chai % 3 + doi_duoc

    return so_chai

n_xu = int(input("Nhập số xu: "))
so_chai = so_chai_bia(n_xu)
print(f"Số chai bia có thể mua được là: {so_chai}")
