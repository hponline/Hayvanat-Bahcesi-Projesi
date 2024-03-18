# Hayvanat Bahcesi Projesi
 
**Hayvanat Bahçesi Projesi**
<h3>500'e 500'lük bir alanda yaşayan 30 koyun (15 erkek,15 dişi), 10 inek (5 erkek,5 dişi),
10 tavuk,10 kurt (5 dişi,5 erkek) 10 horoz, 8 aslan (4 erkek, 4 dişi) ve 1 avcı
bulunmaktadır.
 <br>
Hayvanlardan;
koyun 2 birim,
kurt 3 birim,
inek 2 birim,
tavuk 1 birim,
horoz 1 birim,
aslan 4 birim,
avcı 1 birim rasgele şekilde hareket etmektedir ancak alanın dışına çıkamamaktadır.
 <br>
kurt kendisine 4 birim yakınındaki koyun, tavuk, horoz'u avlayabiliyor.
 <br>
aslan kendisine 5 birim yakınlıktaki inek, koyun'u avlayabiliyor.
 <br>
avcı da kendisine 8 birim yakınlıktaki hayvanlardan herhangi birisini avlayabiliyor.
 <br>
aynı cins farklı cinsiyetteki hayvanlar birbirine 3 birim yakınlaştığı zaman random
cinsiyetli ve aynı cins bir hayvan meydana gelmektedir.
 <br>
1000 birim hareket sonunda hayvanların sayısının bulunduğu bir console application
yazılması beklenmektedir.</h3>

*****
**Dökümantasyon:**

**Proje Açıklaması:** Bu proje, bir hayvanat bahçesindeki hayvanların hareketlerini, avlanma davranışlarını ve üreme süreçlerini simüle eden bir Python programını içermektedir.

**Algoritma Yaklaşımı:** Projede, hayvanların rastgele hareket etmeleri için Monte Carlo yöntemi kullanılmıştır. Avlanma davranışı içinse her hayvan türüne özgü mesafe hesaplamaları yapılmış ve belirli bir mesafede bulunan avlarını tespit edebilmektedirler.

**Kodlama Pratikleri:** Kodlama sürecinde, modülerlik ve okunabilirlik ön planda tutulmuştur. Sınıflar ve fonksiyonlar ayrı dosyalarda düzenlenmiş ve gerektiğinde çağrılmıştır. Kodun düzeni ve yorum satırları sayesinde kodlama pratikleri göz önünde bulundurulmuştur.

**Problem Çözüm Yaklaşımı:** Projede, başlangıçta belirtilen hayvanların türleri ve davranışlarına uygun olarak bir simülasyon oluşturulmuştur. Avlanma, hareket ve üreme(yapılamadı) gibi olaylar her adımda kontrol edilmiş ve gerektiğinde işlemler gerçekleştirilmiştir.

