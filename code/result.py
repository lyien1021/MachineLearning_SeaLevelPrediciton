import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 

#讀取資料 
file_src = "C:/Users/decar/Downloads/MachineLearning_SeaLevelPrediciton-main/MachineLearning_SeaLevelPrediciton-main/data/" //更改路徑
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
station = station.drop(columns=['Year', 'Month']) 
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
