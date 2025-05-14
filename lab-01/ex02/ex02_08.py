# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # KiểM tra xem số thập phan có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
# Nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")