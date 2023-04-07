# Algoritma-Analiz-Odevi1.2
 Algoritma-Analiz-Odevi-2.Kisim

D* Algoritması

D* (D Star) algoritması, bir ağırlıklı graf üzerinde en kısa yolu bulmak için kullanılan bir graf algoritmasıdır. 
Ancak, D* algoritması, grafın dinamik olarak değişebileceği durumlarda kullanılmak üzere tasarlanmıştır. 
Bu nedenle, düğümlerdeki maliyetlerin ve tahmini maliyet değerlerinin sürekli olarak güncellenmesi gerekir.

D* algoritması, her düğümün "g" maliyet değeri ve başlangıç düğümünden her düğüme olan tahmini maliyet değeri veya "h" değeri üzerinde çalışır. 
Başlangıçta, her bir düğümün "rhs" (right-hand side) değeri, başlangıç düğümünden o düğüme giden tahmini en kısa yolun maliyeti olarak ayarlanır.

Algoritma, her bir adımda, başlangıç düğümünden hedef düğüme giden en kısa yolu hesaplamaya çalışır. 
Hedef düğümün "rhs" değeri, başlangıçta tahmini maliyet değerine ayarlanır ve daha sonra, hedef düğüme komşu olan tüm düğümler üzerinde bir döngü oluşturulur.

Bu düğümlerin "g" ve "h" değerleri kullanılarak, bu düğümlere giden en kısa yolun maliyeti hesaplanır. 
Hesaplanan maliyet değerleri, düğümlerin "rhs" değerleriyle karşılaştırılır ve daha iyi bir maliyet değeri elde edilirse, "rhs" değeri güncellenir.

D* algoritması, graf değişikliklerine uygun olarak güncellenebilir. 
Örneğin, bir düğümün maliyeti veya tahmini maliyet değeri değişirse, D* algoritması bu değişikliklere göre yeni bir en kısa yol hesaplayabilir. 
Bu nedenle, D* algoritması, özellikle robot navigasyonu veya otonom araçlar gibi dinamik ortamlarda kullanılan bir algoritmadır. en kısa yol hesaplayabilir.

Çalışma Zamanı

D* algoritmasının en iyi, en kötü ve ortalama çalışma zamanı, grafin boyutu, başlangıç ve hedef düğümleri arasındaki uzaklık, 
düğümlerdeki bilgi sayısı ve grafin dinamik olarak değiştiği durumlarda yapılan değişikliklere bağlıdır.

En iyi durumda, D* algoritması, hedef düğüme çok yakın olan durumlarda en kısa yolu hızlı bir şekilde bulabilir. 
Bu durumda, algoritmanın çalışma zamanı O(1) veya O(logn) olabilir.

Ortalama durumda, D* algoritması, başlangıç ve hedef düğümleri arasındaki uzaklık ve grafin büyüklüğüne bağlı olarak çalışma zamanı O(nlogn) veya O(n^2) olabilir.

En kötü durumda, D* algoritması, grafın boyutunun büyüklüğüne ve başlangıç ile hedef düğümleri arasındaki uzaklığa bağlı olarak çalışma zamanı O(n^2) olabilir.
Özellikle, D* algoritması, her adımda tüm düğümleri kontrol ederek çalışır. Bu nedenle, grafın boyutu büyüdükçe, algoritmanın çalışma zamanı da artacaktır.

D* algoritması, grafin dinamik olarak değiştiği durumlarda yapılan değişikliklere bağlı olarak da çalışma zamanı değişebilir. 
Ancak, D* algoritması, değişiklik yapılan düğümleri yeniden planlar ve günceller, bu da algoritmanın daha az sayıda düğümü yeniden hesaplaması gerektiği anlamına gelir 
ve algoritmanın çalışma zamanını iyileştirir.

-------------------------------------------

Horspool Algoritması (Arama algoritması)

Horspool algoritması, bir metin içinde verilen bir deseni (pattern) bulmak için kullanılan bir string eşleştirme algoritmasıdır. 
Bu algoritma, daha önce bir dizi ön işlemleme adımı gerçekleştirir ve bu sayede desen eşleştirmesini hızlandırır.

Desenin son karakteri için bir tablo oluşturulur. Bu tablo, desendeki bir karakterin metindeki son konumunu belirler. 
Eğer desendeki bir karakter metinde hiç bulunmuyorsa, kaydırma işlemi için desenin uzunluğu kullanılır.

Desen eşleştirme işlemi sağdan sola doğru gerçekleştirilir ve desendeki son karaktere bakarak bir kaydırma (shift) yapılır. 
Eğer desendeki son karakter metindeki bir karakterle eşleşmiyorsa, kaydırma işlemi yapılır ve desendeki son karakter metindeki sonraki karakterle eşleştirilir. 
Bu işlem, desenin tamamı metinde bulunana kadar devam eder.

Horspool algoritması, basit ve hızlı bir string eşleştirme yöntemi olmasının yanı sıra, ayrıca bellek kullanımı açısından da verimlidir. 
Bu nedenle, özellikle küçük desenler için sıklıkla kullanılmaktadır. Ancak büyük desenlerde diğer algoritmalara göre daha yavaş çalışabilir.

Çalışma Zamanı

Horspool algoritmasının en kötü, en iyi ve ortalama çalışma zamanı, aranacak metnin uzunluğuna ve aranacak kalıbın uzunluğuna bağlıdır.

En kötü durumda, Horspool algoritması, aranan kalıbın metinde olmadığı durumda tüm metni kontrol etmek zorunda kalır ve bu durumda çalışma zamanı O(nm) olur,
 n metnin uzunluğunu, m ise kalıbın uzunluğunu temsil eder.

En iyi durumda, Horspool algoritması, aranan kalıp metnin başında bulunursa en kısa sürede eşleşme sağlayabilir. Bu durumda çalışma zamanı O(m) olacaktır.

Ortalama durumda, Horspool algoritması, metnin uzunluğuna ve aranan kalıbın uzunluğuna bağlı olarak çalışma zamanı O(n) ve O(nm) arasında değişebilir.

Horspool algoritması, bir pre-processing işlemi gerçekleştirerek arama süresini iyileştirir. 
Bu işlemde, aranacak kalıptaki karakterlerin sağdan sola doğru sıralanması ve bir önbelleğe atanması işlemi yapılır. 
Bu sayede, arama işlemi sırasında daha hızlı bir şekilde eşleşmeler sağlanabilir. Bu önbelleğin oluşturulması için gereken zaman ise kalıbın uzunluğuna bağlıdır 
ve O(m) zaman karmaşıklığına sahiptir.

alice_in_wonderland.txt dosyasında upon, sigh, Dormouse, jury-box ve swim kelimelerinin bulunduğu sıralar şöyledir:
upon : 2168
sigh : 5273
Dormouse : 71955
jury-box : 123560
swim : 19113
