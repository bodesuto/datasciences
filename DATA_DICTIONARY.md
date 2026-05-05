# 📖 Từ Điển Dữ Liệu & Định Nghĩa Đặc Trưng (Data Dictionary)

Tài liệu này giải thích ý nghĩa các biến số được sử dụng trong mô hình dự báo giá xăng dầu.

## 1. Các biến mục tiêu (Targets)
- **`target_delta`**: Sự chênh lệch giá xăng giữa ngày mai và hôm nay ($P_{t+1} - P_t$). Đây là biến mà AI trực tiếp dự báo.

## 2. Các biến đầu vào (Features)

### ⛽ Nhóm biến Giá xăng (Fuel Features)
- **`price_lag_0`**: Giá xăng RON 95 niêm yết tại thời điểm hiện tại (VND).
- **`days_since_last_change`**: Số ngày kể từ lần điều chỉnh giá gần nhất. (Biến này cực kỳ quan trọng để bắt chu kỳ điều chỉnh của Nhà nước).

### 🛢️ Nhóm biến Dầu quốc tế (Global Market Features)
- **`brent_lag_0`**: Giá dầu Brent thế giới ngày hôm nay (USD/barrel).
- **`brent_lag_7`**: Giá dầu Brent cách đây 7 ngày (Điểm rơi tương quan mạnh nhất).
- **`brent_mean_30`**: Giá dầu Brent trung bình trong 30 ngày qua (Thể hiện xu hướng dài hạn).
- **`brent_diff_1`**: Biến động giá dầu Brent so với ngày hôm qua.
- **`brent_diff_7`**: Biến động giá dầu Brent so với tuần trước.

### 📊 Nhóm biến Trạng thái (Categorical Features)
- **`regime`**: Chế độ thị trường (0: Ổn định, 1: Biến động mạnh). Được phân loại tự động bằng thuật toán học máy.

## 3. Đơn vị đo lường
- **Tiền tệ**: VNĐ (cho xăng), USD (cho dầu Brent).
- **Thời gian**: Theo ngày (Daily).
