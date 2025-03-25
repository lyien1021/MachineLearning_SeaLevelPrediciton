import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import r2_score 

file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/環境時空與資料視覺化/final project/"
file_name = "keelung_data.xlsx"
df = pd.read_excel(file_src + file_name)


#建立x矩陣
X = np.array([df['海平面氣壓(hPa)'],df['最大陣風(m/s)'],df['流量']])
X = X.T.tolist()


y = np.array([df['highesthighwaterlevel']])
y = y.T.tolist()


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# 創建線性回歸模型
model = LinearRegression()

# 使用交叉驗證計算模型的評估指標，例如均方誤差（MSE）
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')

from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

# 將得分轉換為正值
mse_scores = -scores
mae_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')

# 計算均方根誤差 (RMSE)
rmse_scores = np.sqrt(mse_scores)

# 計算 R2
r2_scores = cross_val_score(model, X, y, cv=5, scoring='r2')

# 輸出結果
# print("Mean Squared Error:", mean_mse)
print("Mean Absolute Error (MAE):", mae_scores.mean())
print("R2 Score:", r2_scores.mean())
print("Root Mean Squared Error (RMSE):", rmse_scores.mean())

