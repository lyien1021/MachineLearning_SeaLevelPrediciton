import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/環境時空與資料視覺化/final project/"
file_name = "keelung_data.xlsx"
df = pd.read_excel(file_src + file_name)

#建立x矩陣
X = np.array([df['海平面氣壓(hPa)'],df['最大陣風(m/s)'],df['流量']])
X = X.T.tolist()

y = np.array([df['highesthighwaterlevel']])
y = y.T.tolist()
# 資料標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 拆分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 定義神經網路模型
model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', random_state=42)

# 訓練模型
model.fit(X_train, y_train)

# 在測試集上評估模型
score = model.score(X_test, y_test)
print(score)

# 使用模型進行新的預測
new_data = np.array([[34.4],[1010],[13.5]])  # 填入新的數據
new_data = new_data.T.tolist()  
new_data_scaled = scaler.transform(new_data)
predictions = model.predict(new_data_scaled)
print(predictions)

####調整參數####
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [0.1, 0.01, 0.001],
}

# 創建交叉驗證對象
cross_validation = GridSearchCV(SVR(), param_grid, cv=5)

# 調整參數
cross_validation.fit(X_train, y_train)

# 最佳參數組合
best_params = cross_validation.best_params_
print("最佳參數組合:", best_params)

# 評估模型
best_model = SVR(**best_params)
best_model.fit(X_train, y_train)
accuracy = best_model.score(X_test, y_test)
print("模型精準度:", accuracy)