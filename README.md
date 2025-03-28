# 利用Machine Learning製作預測海平面上升模型
- Introduction  
分析地點：基隆港  
分析年份：2015~2022  
- Data Analysis
  - Highest High water level in Keelung station  
    ![image](https://github.com/lyien1021/Image/blob/24257a8199bd81a7fd25f1454d03e7ddb3fe0fa8/keelung_highest%20high%20water%20level_2015~2022.png)
  - Heat map of variables  
      - Wind velocity  
      - Sea level pressure  
      - River flow  
         ![image](https://github.com/lyien1021/Image/blob/a0c92d0b133f03da9a99e176574029018dbeef6e/HEAT%20MAP.png)  
  - Relationship between HHWL and wind velocity  
      ![image](https://github.com/lyien1021/Image/blob/4b9c624849ad6175fbcfebdda530ac623f96e039/WindVelocity_HHWL.png)  
  - Relationship between HHWL and sea pressure  
    ![image](https://github.com/lyien1021/Image/blob/afcb99aa115c3c0b497b426aed8da464c6bb4bbc/SeaPressure_HHWL.png)  
  - Relationship between HHWL and flow  
    ![image](https://github.com/lyien1021/Image/blob/afcb99aa115c3c0b497b426aed8da464c6bb4bbc/Flow_HHWL.png)  
- Methods & Result  
  - Linear Regression  
      - Training: 80%  
      - Testing: 20%  
![image](https://github.com/lyien1021/Image/blob/afcb99aa115c3c0b497b426aed8da464c6bb4bbc/Regression_result.png)  
  - Result(Fill in missing value)  
    ![image](https://github.com/lyien1021/Image/blob/afcb99aa115c3c0b497b426aed8da464c6bb4bbc/Prediction.png)  
