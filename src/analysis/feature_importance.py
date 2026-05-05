import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap
import os

# 1. Load dữ liệu và mô hình
DATA_PATH = "f:/Project/DataSciences/data/processed/feature_dataset.csv"
MODEL_PATH = "f:/Project/DataSciences/models/final_rf_model.pkl"

if not os.path.exists(MODEL_PATH):
    print("Vui lòng huấn luyện mô hình trước!")
    exit()

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

# Chuẩn bị dữ liệu (loại bỏ cột target và date)
features = [col for col in df.columns if col not in ['date', 'target_delta', 'price_next_day']]
X = df[features]

print(f"Đang phân tích sự tương quan cho {len(features)} đặc trưng...")

# 2. Sử dụng SHAP để giải thích mô hình
# SHAP tính toán giá trị đóng góp của từng biến vào kết quả dự báo cuối cùng
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# 3. Vẽ biểu đồ Summary Plot
# Biểu đồ này cho thấy: Biến nào quan trọng nhất và nó đẩy giá lên hay xuống
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X, show=False)
plt.title("SHAP Feature Importance (Sự tương quan của các Input)")
plt.tight_layout()

# Lưu biểu đồ
output_path = "f:/Project/DataSciences/logs/feature_impact_analysis.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
print(f"Biểu đồ phân tích tương quan đã được lưu tại: {output_path}")

# 4. In ra bảng xếp hạng tầm quan trọng
import numpy as np
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': np.abs(shap_values).mean(0)
}).sort_values(by='Importance', ascending=False)

print("\n--- BẢNG XẾP HẠNG TẦM QUAN TRỌNG CỦA INPUT ---")
print(importance_df)
