## OnePlus Kernel Open Source

[![OnePlus Repository](https://img.shields.io/badge/OnePlus-Repository-red)](https://github.com/Xiaomichael/kernel_manifest)

## Support devices

> [!TIP]
> **CURRENTLY ONLY SUPPORTS KERNEL 6.1 AND BELOW**

## User Guide

### MÔ TẢ TẬP TIN CẤU HÌNH

以**Oneplus 12**为例：
- không có hậu tố：Android 15
- `_u` hậu tố：Android 14
- `_t` hậu tố：Android 13

![Ví dụ về tập tin cấu hình](https://github.com/user-attachments/assets/88f6940b-4b2c-462f-b8fa-3d9dd2f2faec)

### lựa chọn Branches

1. Nhấp vào `Branches` để chuyển đổi các nhánh bộ xử lý
2. Chọn cấu hình phù hợp với thiết bị của bạn

![Ví dụ lựa chọn Branches](https://github.com/user-attachments/assets/58f31536-b88e-4613-9865-3e0574868928)

### Cách kiểm tra mã bộ xử lý

![Cách kiểm tra mã bộ xử lý](https://github.com/user-attachments/assets/fc217103-24ef-45fa-a7e1-f13cfd64f771)
Nó được viết bên dưới Branches tương ứng. Nếu nó xuất hiện `using make build` Đừng lo lắng về điều đó

## Chuyển đổi đề xuất

- **kpm**：Nên tắt để giảm mức tiêu thụ điện năng
- **lz4kd**：
  - Kernel dòng 6.1: Nên tắt nó đi để có được `lz4 + zstd` tốt hơn
  - Các phiên bản kernel khác: Nên giữ nguyên trạng thái bật

## Ví dụ về cấu hình Runtime

![{BF5F0169-D752-481A-BA95-FCDD8483A359}](https://github.com/user-attachments/assets/8f875661-3955-46c4-b65c-06f40afbc122)
