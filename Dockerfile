# Sử dụng Python 3.11 làm nền tảng
FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Mở cổng 8000 cho FastAPI
EXPOSE 8000

# Lệnh khởi chạy API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
