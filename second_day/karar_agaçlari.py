from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
Y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30)
# Knn algoritmasından farklı olarak bu sefer karar ağaçlarını çağırıyoruz.
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)
Y_tahmin = model.predict(X_test)
from sklearn.metrics import confusion_matrix
hata_matrisi = confusion_matrix(Y_test, Y_tahmin)
print(hata_matrisi)
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
index = ['setosa','versicolor','virginica'] 
columns = ['setosa','versicolor','virginica'] 
hata_goster = pd.DataFrame(hata_matrisi,columns,index)                      
plt.figure(figsize=(10,6))  
sns.heatmap(hata_goster, annot=True)