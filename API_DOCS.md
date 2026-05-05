# 🔌 Tài Liệu Kỹ Thuật API (API Documentation)

Hệ thống cung cấp RESTful API để tích hợp dự báo vào các ứng dụng bên thứ ba.

## 1. Thông tin chung
- **Base URL**: `http://localhost:8000`
- **Content-Type**: `application/json`

## 2. Các Endpoints

### 🟢 Lấy danh sách mẫu dữ liệu lịch sử
- **Endpoint**: `/samples`
- **Method**: `GET`
- **Mô tả**: Trả về 100 ngày dữ liệu gần nhất để phục vụ mục đích giả lập.

### 🔵 Thực hiện dự báo
- **Endpoint**: `/predict`
- **Method**: `POST`
- **Request Body**:
```json
{
  "price_lag_0": 23000,
  "brent_lag_0": 85.5,
  "brent_lag_7": 82.0,
  "brent_mean_30": 83.2,
  "regime": 0,
  "brent_diff_1": 0.5,
  "brent_diff_7": 3.5,
  "days_since_last_change": 5,
  "model_name": "random_forest",
  "horizon": 3
}
```
- **Response Body**:
```json
{
  "model_used": "random_forest",
  "horizon": 3,
  "forecast": [
    { "day": 1, "predicted_delta": 15.2, "predicted_price": 23015.2 },
    { "day": 2, "predicted_delta": 5.1, "predicted_price": 23020.3 }
  ]
}
```

## 3. Mã lỗi thường gặp
- **400 Bad Request**: Model name không tồn tại hoặc dữ liệu đầu vào sai định dạng.
- **422 Unprocessable Entity**: Thiếu các trường dữ liệu bắt buộc.
- **500 Internal Server Error**: Lỗi logic trong quá trình tính toán của AI.
