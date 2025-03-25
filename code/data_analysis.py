import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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



merged_keelung = merged_keelung.drop(columns=['station'])
all_keelung = merged_keelung.iloc[84:96]

all_keelung = all_keelung.drop(columns=['MeanTidalRange','MaxAstronomicalTidalRange'])

for column in all_keelung.columns:
    plt.plot(all_keelung.index, all_keelung[column],label=column)
    all_keelung[column] = all_keelung[column].astype(float)
plt.xlabel('Time')
plt.ylabel('Water Level(m)')
# 設定y軸範圍
plt.yticks(np.arange(-1.5, 1.5, 0.2))
# plt.plot(all_Zhuwei.index, all_Zhuwei['HighestHighWaterLevel'], label=column, marker='o')
plt.title('keelung station')
plt.legend(['Highest High Water Level', 'Highest Astronomical Tide','MeanHighWaterLevel','MeanLowWaterLevel','LowestAstronomicalTide','LowestLowWaterLevel'])
plt.show()

#####竹圍站#####

#設立時間軸
station_Zhuwei = pd.DataFrame({'station': 'Zhuwei'}, index=idx)
###調換時間順序###
station_Zhuwei['Month'] = idx
station_Zhuwei['Year'] = pd.DatetimeIndex(station_Zhuwei['Month']).year
station_Zhuwei['Month'] = pd.DatetimeIndex(station_Zhuwei['Month']).month
# 先按照年份倒序排列，再按照月份正序排列
station_Zhuwei = station_Zhuwei.sort_values(by=['Year', 'Month'], ascending=[False, True])
# 將年份和月份拼接回去
station_Zhuwei['datetime'] = pd.to_datetime(station_Zhuwei['Year'].astype(str) + '-' + station_Zhuwei['Month'].astype(str), format='%Y-%m')
# 刪除Year和Month欄位
station_Zhuwei = station_Zhuwei.drop(columns=['Year', 'Month'])
station_Zhuwei = station_Zhuwei.reset_index(drop=True)

#選取測站的資料
Zhuwei = df.iloc[430:514,53:62]
Zhuwei = Zhuwei.reset_index(drop=True)


# 横向合併兩個表格
merged_Zhuwei = pd.concat([station_Zhuwei, Zhuwei], axis=1)
merged_Zhuwei = merged_Zhuwei.set_index(['datetime']).sort_index(ascending=True)


#處理非數值資料
merged_Zhuwei.replace(['-'], np.nan, inplace=True)
merged_Zhuwei['MeanTidalRange'] = pd.to_numeric(merged_Zhuwei['MeanTidalRange'], errors='coerce')

#draw
plt.plot(merged_Zhuwei.index, merged_Zhuwei['MeanTidalRange'])
plt.xlabel('Time')
plt.ylabel('Mean Tidal Range(m)')
plt.title('Zhuwei station')
plt.show()


merged_Zhuwei = merged_Zhuwei.drop(columns=['station'])
all_Zhuwei = merged_Zhuwei.iloc[72:84]

all_Zhuwei = all_Zhuwei.drop(columns=['MeanTidalRange','MaxAstronomicalTidalRange'])

for column in all_Zhuwei.columns:
    plt.plot(all_Zhuwei.index, all_Zhuwei[column],label=column)
    all_Zhuwei[column] = all_Zhuwei[column].astype(float)
plt.xlabel('Time')
plt.ylabel('Water Level(m)')
# 設定y軸範圍
plt.yticks(np.arange(-2.4, 2.6, 0.3))
# plt.plot(all_Zhuwei.index, all_Zhuwei['HighestHighWaterLevel'], label=column, marker='o')
plt.title('Zhuwei station')
plt.legend(['Highest High Water Level', 'Highest Astronomical Tide','MeanHighWaterLevel','MeanLowWaterLevel','LowestAstronomicalTide','LowestLowWaterLevel'])
plt.show()





