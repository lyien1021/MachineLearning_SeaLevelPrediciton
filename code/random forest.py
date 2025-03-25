import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#讀取資料
file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/環境時空與資料視覺化/midterm project/data/"
file_name = "Taiwan sea level.xlsx"
df = pd.read_excel(file_src + file_name)

#更改列名稱
df = df.rename({'ns1:MeanTideLevel8': 'MeanTideLevel'},axis=1)
df = df.rename({'ns1:HighestHighWaterLevel5': 'HighestHighWaterLevel'},axis=1)
df = df.rename({'ns1:HighestAstronomicalTide6': 'HighestAstronomicalTide'},axis=1)
df = df.rename({'ns1:MeanHighWaterLevel7': 'MeanHighWaterLevel'},axis=1)
df = df.rename({'ns1:MeanLowWaterLevel9': 'MeanLowWaterLevel'},axis=1)
df = df.rename({'ns1:LowestAstronomicalTide10': 'LowestAstronomicalTide'},axis=1)
df = df.rename({'ns1:LowestLowWaterLevel11': 'LowestLowWaterLevel'},axis=1)
df = df.rename({'ns1:MeanTidalRange12': 'MeanTidalRange'},axis=1)
df = df.rename({'ns1:MaxAstronomicalTidalRange13': 'MaxAstronomicalTidalRange'},axis=1)
df = df.rename({'ns1:MeanHighWaterOfSpringTide14': 'MeanHighWaterOfSpringTide'},axis=1)
df = df.rename({'ns1:MeanLowWaterOfSpringTide15': 'MeanLowWaterOfSpringTide'},axis=1)
df = df.rename({'ns1:DataMonth': 'Month'},axis=1)
df = df.rename({'ns1:StationName': 'Station'},axis=1)

#####淡海站#####
#設立時間軸
idx = pd.date_range('2015-01', '2023-01', freq='M')
station = pd.DataFrame({'station': 'keelung'}, index=idx)

###調換時間順序###
station['Month'] = idx
station['Year'] = pd.DatetimeIndex(station['Month']).year
station['Month'] = pd.DatetimeIndex(station['Month']).month
# 先按照年份倒序排列，再按照月份正序排列
station = station.sort_values(by=['Year', 'Month'], ascending=[False, True])
# 將年份和月份拼接回去
station['datetime'] = pd.to_datetime(station['Year'].astype(str) + '-' + station['Month'].astype(str), format='%Y-%m')
# 刪除Year和Month欄位
station = station.drop(columns=['Year', 'Month','station'])
station = station.reset_index(drop=True)

#選取測站的資料
keelung = df.iloc[7091:7186,53:62]
keelung = keelung.reset_index(drop=True)


# 横向合併兩個表格
merged_keelung = pd.concat([station, keelung], axis=1)
merged_keelung = merged_keelung.set_index(['datetime']).sort_index(ascending=True)


#處理非數值資料
merged_keelung.replace(['-'], np.nan, inplace=True)
merged_keelung['HighestHighWaterLevel'] = pd.to_numeric(merged_keelung['HighestHighWaterLevel'], errors='coerce')

#draw
plt.plot(merged_keelung.index, merged_keelung['HighestHighWaterLevel'])
plt.xlabel('Time')
plt.ylabel('Highest High Water Level(m)')
plt.title('keelung station')
plt.show()


###########final###########
print('資料維度:',merged_keelung.shape)
merged_keelung.describe(include='all')

#標籤
labels = np.array(merged_keelung['HighestHighWaterLevel'])
#名字單獨儲存
keelung_list = list(merged_keelung.columns)
# 轉換成合適的格式
merged_keelung = np.array(merged_keelung)

#資料集切分
train_keelung, test_keelung, train_labels, test_labels = train_test_split(merged_keelung, labels, test_size=0.25, random_state=42)
print('訓練集特徵：', train_keelung.shape)
print('訓練集標籤', train_labels.shape)
print('測試集特徵：', test_keelung.shape)
print('測試集標籤：', test_labels.shape)

#隨機森林
#建模
rf = RandomForestRegressor(n_estimators=2000, random_state=42)
#處理nan值
train_keelung = train_keelung.astype(float)
nan_train_keelung = np.isnan(train_keelung).any(axis=1)
filtered_array = train_keelung[~nan_train_keelung]
train_labels = train_labels.astype(float)
nan_train_labels = np.isnan(train_labels)
filtered_array2 = train_labels[~nan_train_labels]

test_keelung = test_keelung.astype(float)
nan_test_keelung = np.isnan(test_keelung).any(axis=1)
filtered_array3 = test_keelung[~nan_test_keelung]
test_labels = test_labels.astype(float)
nan_test_labels = np.isnan(test_labels)
filtered_array4 = test_labels[~nan_test_labels]

print('訓練集特徵：', filtered_array.shape)
print('訓練集標籤', filtered_array2.shape)
print('測試集特徵：', filtered_array3.shape)
print('測試集標籤：', filtered_array4.shape)

#訓練
rf.fit(filtered_array, filtered_array2)
#預測結果
predictions = rf.predict(filtered_array3)
#計算誤差
errors = abs(predictions - filtered_array4)

#MAPE
mape = 100*(errors/filtered_array4)
print('MAPE:',np.mean(mape))

# 計算精度指標
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# accuracy = accuracy_score(filtered_array3, predictions)
# precision = precision_score(filtered_array3, predictions)
# recall = recall_score(test_labels, predictions)
# f1 = f1_score(test_labels, predictions)
# auc_roc = roc_auc_score(test_labels, predictions)
# confusion = confusion_matrix(test_labels, predictions)

# print("Accuracy:", accuracy)
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1 Score:", f1)
# print("AUC-ROC:", auc_roc)
# print("Confusion Matrix:\n", confusion)