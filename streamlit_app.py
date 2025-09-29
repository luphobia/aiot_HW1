import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title("Simple Linear Regression with Streamlit")

st.sidebar.header("Parameters for Data Generation")

n_samples = st.sidebar.slider("Number of samples (n)", 100, 5000, 1000)
slope_a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.0)
intercept_b = st.sidebar.slider("Intercept (b)", -10.0, 10.0, 3.0)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 1.0)

# 1. 準備資料 (y = ax + b + 雜訊)
np.random.seed(42)
X = 2 * np.random.rand(n_samples, 1)   # 自變數 (n_samples 筆, 單一特徵)
y = slope_a * X + intercept_b + np.random.randn(n_samples, 1) * np.sqrt(noise_variance)  # 因變數

st.subheader("Generated Data")
st.write(f"Number of samples: {n_samples}")
st.write(f"True slope (a): {slope_a}")
st.write(f"True intercept (b): {intercept_b}")
st.write(f"Noise variance: {noise_variance}")

# 2. 建立模型
model = LinearRegression()
model.fit(X, y)

st.subheader("Model Parameters")
st.write(f"Intercept (intercept): {model.intercept_[0]:.3f}")
st.write(f"Coefficient (slope): {model.coef_[0][0]:.3f}")

# 3. 預測
y_pred = model.predict(X)

# 4. 評估
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
st.subheader("Model Evaluation")
st.write(f"Mean Squared Error (MSE): {mse:.3f}")
st.write(f"R-squared: {r2:.3f}")

# 5. 視覺化
fig, ax = plt.subplots()
ax.scatter(X, y, label="Data points")
ax.plot(X, y_pred, color="red", label="Regression line")

# Identify and label top 5 outliers
residuals = y - y_pred
outlier_indices = np.argsort(np.abs(residuals).flatten())[::-1][:5]

for i, idx in enumerate(outlier_indices):
    ax.annotate(f'Outlier {i+1}', (X[idx][0], y[idx][0]),
                textcoords="offset points", xytext=(0,10),
                ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.5))

ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
