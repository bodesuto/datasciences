# 📘 Hướng Dẫn Vận Hành Dự Án Fuel Price AI

Tài liệu này hướng dẫn bạn cách khởi chạy toàn bộ hệ thống từ bước thiết lập môi trường đến bước vận hành Dashboard. Vui lòng thực hiện theo đúng trình tự các bước dưới đây.

---

## 🛠️ Bước 1: Chuẩn bị Môi trường (Prerequisites)

Đảm bảo máy tính của bạn đã cài đặt:
1.  **Python 3.10+**: [Tải về tại đây](https://www.python.org/downloads/)
2.  **Node.js 18+**: [Tải về tại đây](https://nodejs.org/)
3.  **Git**: [Tải về tại đây](https://git-scm.com/)

---

## 📦 Bước 2: Thiết lập Mã nguồn & Thư viện

### 2.1. Clone dự án và tạo môi trường ảo (Python)
```powershell
# Di chuyển vào thư mục dự án
cd f:/Project/DataSciences

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo (Windows)
.\venv\Scripts\activate

# Cài đặt các thư viện Backend
pip install -r requirements.txt
```

### 2.2. Thiết lập Frontend
```powershell
cd frontend
npm install
```

---

## ⚙️ Bước 3: Chạy Pipeline Dữ liệu & Huấn luyện AI

Nếu bạn muốn chạy lại toàn bộ quy trình từ dữ liệu thô đến khi ra file mô hình:

1.  **Làm sạch dữ liệu**:
    `python src/processing/data_cleaning.py`
    *(Kết quả: Tạo ra file data/processed/cleaned_data.csv)*

2.  **Tạo đặc trưng (Features)**:
    `python src/features/feature_engineering.py`
    *(Kết quả: Tạo ra file data/processed/feature_dataset.csv)*

3.  **So sánh & Thử nghiệm mô hình**:
    `python src/models/compare_models.py`
    *(Dùng để xem báo cáo so sánh các thuật toán)*

4.  **Huấn luyện các mô hình chính thức (Để phục vụ API)**:
    *   **CatBoost (SOTA)**: `python src/models/train_catboost.py`
    *   **XGBoost**: `python src/models/train_xgboost.py`
    *   **Ensemble**: `python src/models/train_ensemble.py`
    *   **Random Forest**: `python src/models/train_final_model.py`

5.  **Phân tích sự tương quan (XAI)**:
    *   Chạy `python src/analysis/feature_importance.py` để xuất biểu đồ ảnh hưởng của các Input.

*Lưu ý: Sau khi chạy xong mục 4, bạn sẽ thấy các file `.pkl` xuất hiện trong thư mục `models/`. Đây là điều kiện bắt buộc để API khởi chạy không bị lỗi.*

---

## 🚀 Bước 4: Khởi chạy Hệ thống (Sẵn sàng sử dụng)

Hệ thống yêu cầu cả Backend và Frontend chạy song song.

### 4.1. Khởi chạy Backend API (Cửa sổ Terminal 1)
```powershell
# Đảm bảo đang ở thư mục gốc và venv đã được kích hoạt
python src/api/main.py
```
*Hệ thống sẽ báo: `Uvicorn running on http://0.0.0.0:8000`*

### 4.2. Khởi chạy Frontend Dashboard (Cửa sổ Terminal 2)
```powershell
cd frontend
npm run dev
```
*Truy cập giao diện tại: `http://localhost:5173`*

---

## 🐳 Bước 5: Khởi chạy bằng Docker (Cách chuyên nghiệp nhất)

Nếu bạn đã cài đặt Docker, bạn có thể khởi chạy toàn bộ chỉ với 1 lệnh duy nhất:
```powershell
# Tại thư mục gốc (nơi có file docker-compose.yml)
docker-compose up --build
```
*Lúc này Web chạy tại cổng `80` và API chạy tại cổng `8000`.*

---

## ❓ Giải quyết sự cố thường gặp (Troubleshooting)

1.  **Lỗi Port 8000 đã được sử dụng**:
    *   Kiểm tra xem có cửa sổ terminal nào đang chạy API không và tắt nó đi (Ctrl+C).
2.  **Lỗi trắng màn hình ở Frontend**:
    *   Hãy đảm bảo bạn đã chạy `npm install` thành công.
    *   Kiểm tra Console (F12) để xem lỗi thư viện.
3.  **Lỗi không tìm thấy Model (.pkl)**:
    *   Đảm bảo bạn đã chạy Bước 3 để tạo ra các file mô hình trong thư mục `models/`.

---
*Chúc bạn vận hành dự án thành công!*
