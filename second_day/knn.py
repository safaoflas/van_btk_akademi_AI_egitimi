# from kelimesinin türkçe karşılığı -den -dan anlamına gelir 3. satır'da kullandığımız yapıda aslında şunu diyoruz sisteme:
# Bana sklearn kütüphanesin(den/from yapısı) datasets kısmından bana iris datasetini import et yani çalıştığım ortama o veri setini getir diyoruz.   
from sklearn.datasets import load_iris 

# 6. satırda iris diye bir değişken oluşturuyoruz ve diyoruz ki iris veri setini kalıtım yoluyla iris veri setine iris değişkeni ile erişebiliyoruz. 
iris = load_iris()

# 9. satırda feature_names ile X değişkenlerimizin isimleri yer almaktadır.(Örn. Sepal length, petal width gibi)
print (iris.feature_names)

# 12.satırda target_names türkçe manasıyla hedef ismi demek yani bizim y çıktılarımız oluyor bu da demek oluyor ki iris verisinin sınıf isimlerini bu özellik ile öğrenebiliriz.
print (iris.target_names)

# 15. satırda yer alan iris.target özelliği iris veri setimizdeki sınıf sayısını index sıralamaya göre sunabiliyor.
print (iris.target)

# 18. satırda yer alan iris.data iris veri setindeki verilerin kabaca gösterimini yapıyor.
print (iris.data)

# 21. satırda yer alan özellik ile x girdilerimizin iris üzerinde bulunan datadan alacağını belirtiyoruz. 
X = iris.data

# 24. satırda y çıktılarımızın iris veri seti üzerinde bulunan targetlardan alacağını belirtiyoruz. 
Y = iris.target

# 28. satırda sklearn kütüphanesin(den/ from yapısı ) model seçimi kısmından train_test_split(eğitim_test_ayırma) özelliğini import ediyorum yani bulunduğum ortama aktar diyoruz.
# train_test_split() özelliği üzerinde çalışmış olduğumuz verisetimiz manuel olarak eğitim verisi ve test verisi diye ayrılmamışsa bu özellik otomatik olarak belirlemiş olduğumuz parametrelere göre veri setini eğitim ve test için ayırıyor.
from sklearn.model_selection import train_test_split

# 33. satırda X_train ve X_test diyerek aslında şunu söylemiş oluyoruz:
# benim X girdilerim var evet ama bu girdilerimin hepsini eğitimde kullanmak istemiyorum bir kısmını eğitim için kullanalım sonrasında:
# kalan veriler ile eğitmiş olduğum modeli hiç göstermediğim (X_test içerisinde bulunan modeller daha öncesinde modele verilmez.) veriler ile modelin doğruluğunu test edeyim demiş oluyoruz. 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

# Devamında 37 ve 38.satırlarda sadece bir fikrimiz olsun diye eğitim ve test verisine kaç adet veri ayırdığını öğreniyoruz.
# NOT! : 37 ve 38.satırda yapmış olduğumuz bilgi edinme zorunlu bir durum değildir istenilirse kullanılmaz.
print("Eğitim veri seti boyutu=",len(X_train))
print("Test veri seti boyutu=",len(X_test))



"""
Yukarıda verilen işlemler veriyi anlamak ve veriyi analiz etmek için kullanılır.
Terimsel olarak Veri Önişleme ve veri işleme adımları olarak bilinmektedir. 
Model oluşturma kısmı 50.satır ile 65.satırlar arasında yer almakatadır.
"""

# 50. satırda iris veri çiçeğinin sınıflandırma problemini çözmek için K-Nearest Neighbors yani K- En Yakın Komşu algoritmasını bulunduğumuz ortama aktaracağız.
# Sklearn kütüphanesinden komşuluk algoritmalarından K-komşuluk sınıflandırıcısını bulunduğum ortama aktar diyoruz. 
from sklearn.neighbors import KNeighborsClassifier

# 55. satırda model = KNeighborsClassifier() diyip kalıtım yapmış oluyoruz.
"""Derste vermiş olduğumuz örnek üzerinden anlatacak olursak
model adlı değişken C.Ronaldo'nun oğlu C.Ronaldo ise bulunduğumuz durum itibariyle KNeighborsClassifier () oluyor """ 
model =  KNeighborsClassifier ()

# 60. satırda model.fit diyerek modelimizi X ve Y eğitim verilerimiz ile eğitmeye başlıyoruz.
"""Verdiğimiz örnek üzerinden devam edecek olursak 
Ronaldonun oğlu belli başlı eğitimler alıyor ve aldığı eğitimler doğrultusunda kendini eğitiyor."""
model.fit(X_train,Y_train)

# 65. satırda modelimizden tahmin değerlerini alıp Y_tahmin değişkenine atıyoruz.
"""Ronaldonun oğlu real madrid takımına girmek istiyor ve oyuncu seçmelerinde Ronaldonun oğluna bazı testler uygulanıyor.
Ve ronaldonun oğlunun yapmış olduğu skorlar Ancelottiye gidiyor. Bu örnek için Y_tahmin değerleri Ancelottiye giden skor değerleri."""
Y_tahmin = model.predict(X_test)

#72.satırda sklearn kütüphanesinden metrics yani ölçümler kısmından hata matrisini bulunduğumuz ortama aktarmasını istiyoruz.
"""Örnek üzerinden devam edecek olursak Ancelotti ronaldonun oğlunun takıma girmeye hak kazanıp kazanmadığını şu şekilde anlıyor:
   normalde testler üzerinde alınması gereken skorlar ile ronaldonun oğlunun almış oluduğu skorlar arasındaki farklara bakarak karar veriyor 
   Bu karar verme süreci 73. satır ve 85.satırda yer alan kodları anlatmaktadır.  
"""
from sklearn.metrics import confusion_matrix
# python üzerinde hata matrisini çağırmak için "confusion_matrix" terimi kullanılır 76.satırda tanımlanan hata_matrisi sadece bir değişkendir.
# hata matrisi değişkenimizi oluşturuyoruz ve modelin hatalarını;
# gerçek çıktı değerleri ve modelin yapmış oluduğu tahmini çıktı değerleri arasındaki farka göre belirliyoruz. 
hata_matrisi = confusion_matrix(Y_test, Y_tahmin)
print(hata_matrisi)


#81. satırda Sklearn kütüphanesinden ölçümler kısmından doğruluk puanı özelliğini bulunduğumuz ortam aktarmasını istiyoruz.
#accuracy_score özelliği ile modelimizin yüzdelik gösterimle doğruluk oranını öğrenmiş oluruz
from sklearn.metrics import accuracy_score
# sonuc değişkenimizi oluşturuyoruz ve modelin yüzdelik doğruluğunu;
# gerçek çıktı değerleri ve modelin yapmış oluduğu tahmini çıktı değerleri arasındaki farka göre belirliyoruz.
sonuc = accuracy_score(Y_test, Y_tahmin)
print(sonuc)


#Şimdi bütün model süreçleri bitti artık elde ettiğimiz sonuçları yani matrisimizi süsleyeceğiz daha renkli daha cafcaflı hale getireceğiz.
# Bu yapıcağımız işlemin terimsel ifadesi Veri görselleştirmedir.
# Veri görselleştirme işlemi için seaborn, pandas, matplotlib kütüphanelerini bulunduğumuz ortam aktarıyoruz.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# index ve columns listelerinde iris veri setinin sınıflarının isimlerini yazıyoruz.  
# index ve columns yapısı matamatikteki lineer cebir yapısından gelmektedir.
index = ['setosa','versicolor','virginica'] 
columns = ['setosa','versicolor','virginica'] 

#102. satırda yer alan kod, matrisin üzerine index ve columns listelerini ekleyeceğiz. 
#Bu birleştirmenin sonucnda oluşan yeni veri çervesini yani matrix'i hata_goster adlı değişkende tutucaktır.
hata_goster = pd.DataFrame(hata_matrisi,columns,index)                      

#106. satırda yer alan kodda hata_goster değişkeni üzerinde bulunan matrisi matris görümünden çıkarıp şekil yani figür görümünde göstermek için figür oluşturuyoruz. 
plt.figure(figsize=(10,6))  

# 110. satırda hata goster değişkeninde bulunan matrisi oluşturulan figür doğrultusunda ısı haritası formatına dönüştürüyoruz.
# annot=True seçeneği, ısı haritasına her bir hücrenin değerini de ekler. 
# Bu sayede, haritadaki her bir noktanın neyi temsil ettiğini kolayca anlayabilirsiniz.
sns.heatmap(hata_goster, annot=True)