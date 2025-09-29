# simple_linear_regression.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 準備資料 (y = 2x + 3 + 雜訊)
np.random.seed(42)
X = 2 * np.random.rand(100, 1)   # 自變數 (100 筆, 單一特徵)
y = 2 * X + 3 + np.random.randn(100, 1)  # 因變數

# 2. 建立模型
model = LinearRegression()
model.fit(X, y)

# 3. 模型參數
print("截距 (intercept):", model.intercept_)
print("係數 (slope):", model.coef_)

# 4. 預測
y_pred = model.predict(X)

# 5. 評估
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE: {mse:.3f}")
print(f"R-squared: {r2:.3f}")

# 6. 視覺化
plt.scatter(X, y, label="Data points")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()