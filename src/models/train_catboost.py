import pandas as pd
import numpy as np
from catboost import CatBoostRegressor, Pool
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Load data
DATA_PATH = "f:/Project/DataSciences/data/processed/feature_dataset.csv"
MODEL_PATH = "f:/Project/DataSciences/models/catboost_model.pkl"

df = pd.read_csv(DATA_PATH)
df = df.sort_values('date')

# 2. Prepare Features & Target
features = [col for col in df.columns if col not in ['date', 'target_delta', 'price_next_day']]
X = df[features]
y = df['target_delta']

# Split (80% Train, 20% Test)
split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

print(f"Training CatBoost on {len(X_train)} samples...")

# 3. Train CatBoost
# Ưu điểm: Tự động xử lý overfitting và tối ưu hóa cho dữ liệu chuỗi thời gian
model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    loss_function='MAE',
    verbose=100,
    random_seed=42
)

model.fit(X_train, y_train, eval_set=(X_test, y_test))

# 4. Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\nCatBoost Evaluation:")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# 5. Save Model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"\nCatBoost Model saved to {MODEL_PATH}")
