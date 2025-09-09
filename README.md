## OnePlus Kernel Open Source

[![OnePlus Repository](https://img.shields.io/badge/OnePlus-Repository-red)](https://github.com/maihcx/kernel_manifest)

## Support devices

> [!TIP]
> **HIỆN TẠI CHỈ HỖ TRỢ KERNEL 6.1 TRỞ XUỐNG**

## User Guide

### MÔ TẢ TẬP TIN CẤU HÌNH

Lấy **Oneplus 12** làm ví dụ:
- không có hậu tố：Android 15
- `_u` hậu tố：Android 14
- `_t` hậu tố：Android 13

![Ví dụ về tập tin cấu hình](https://github.com/user-attachments/assets/7d30d34f-95ff-418d-a7ad-205566814df2)

### lựa chọn Branches

1. Nhấp vào `Branches` để chuyển đổi các nhánh bộ xử lý
2. Chọn cấu hình phù hợp với thiết bị của bạn

![Ví dụ lựa chọn Branches](https://github.com/user-attachments/assets/7c04928e-430a-4c2b-aabb-8c8a83a1d387)

### Cách kiểm tra mã bộ xử lý

![Cách kiểm tra mã bộ xử lý](https://github.com/user-attachments/assets/82ea9c63-da2d-40fe-a076-27711099d0e3)

Nó được viết bên dưới Branches tương ứng. Nếu nó xuất hiện `using make build` Đừng lo lắng về điều đó

## Chuyển đổi đề xuất

- **kpm**：Nên tắt để giảm mức tiêu thụ điện năng
- **lz4kd**：
  - Kernel dòng 6.1: Nên tắt nó đi để có được `lz4 + zstd` tốt hơn
  - Các phiên bản kernel khác: Nên giữ nguyên trạng thái bật

## Ví dụ về cấu hình Runtime

![{BF5F0169-D752-481A-BA95-FCDD8483A359}](https://github.com/user-attachments/assets/a0b95be2-e3cb-4591-b853-83398acf0153)
