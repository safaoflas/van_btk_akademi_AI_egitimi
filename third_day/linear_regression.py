import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression #Linear Regresyon algoirtmasını sklearn üzerinden çağırıyoruz.
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:\\Users\\safaoflas\\Downloads\\housing.csv")
print(df)

#veri setini tanıyalım

print(df.info())
print(df.describe())

X = df.iloc[:,0:3] # burda veri setinde bulunan feature'ları alıyorum. "RM, LSTAT, PTRATIO"
Y = df.iloc[:,3]

new_x = np.array(X)
new_y = np.array(Y)


X_train, X_test, Y_train, Y_test = train_test_split(new_x,new_y,test_size=1/3, random_state=42)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_tahmin = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_tahmin)# oratlama kare hata hesaplama 
rmse = np.sqrt(mse)# karekök ortalama kare hata hesaplama 
r2 = r2_score(Y_test, Y_tahmin)# r2 score hesaplama

yeni_veri = [[7.25, 4.125, 23.0]]  # Örnek yeni veri noktası
tahmin = model.predict(yeni_veri)

print("Yeni tahmin değeri = ", tahmin[0])



