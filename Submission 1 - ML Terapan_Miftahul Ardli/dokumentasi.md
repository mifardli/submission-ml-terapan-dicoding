
<h1> Laporan Proyek Machine Learning - Miftahul Ardli </h1>
<hr>
<h2> Domain Proyek </h2>
<hr>
<p> Pertumbuhan ekonomi merupakan pertumbuhan yang signifikan berpengaruh terhadap suatu pertumbuhan negara dan masyarakat. Tidak ayal, pertumbuhan ekonomi disangkutpautkan dengan jumlah masyarakat yang tidak bekerja (penganggur). Setiap tahun, Perlunya pertumbuhan ekonomi di suatu negara dipantau sehingga diperlukan analisis prediktif untuk mengetahui apakah pertumbuhan ekonomi tersebut membaik atau memburuk. Tidak jarang, jumlah penganggur yang ada di masyarakat menentukan jumlah pendapatan domestik suatu negara tersebut yang dapat berpengaruh dalam kondisi perekonomian suatu negara <sup>[1]</sup>. Melihat urgensi tersebut, sistem model prediktif diperlukan untuk mengambil tindakan preventif untuk menghindari kemungkinan terburuk, yaitu resesi ekonomi. </p>

<h2> Business Understanding </h2>
<hr>
<p> Pembuatan model prediktif tersebut dapat diselesaikan dengan cara membuat model sistem prediktif yaitu model linear regresi, dimana model tersebut dapat memprediksi seberapa banyak jumlah masyarakat yang belum memiliki pekerjaan (penganggur) setiap tahunnya berdasarkan <i>features</i>, sehingga seluruh stakeholder dapat mengambil langkah preventif atau kuratif untuk mengatasi permasalahan tersebut. </p>
<p> Seperti yang kita ketahui, jumlah pendapatan domestik suatu negara dipengaruhi oleh jumlah kesejahteraan masyarakat, sehingga masalah terkait kesempatan kerja perlu menjadi perhatian bagi seluruh pihak.</p>

<h3> Problem Statements </h3>
<hr>
<p>Dalam pembuatan model prediktif ini, permasalahan yang akan diangkat berdasarkan data yang sudah tersedia tersebut ialah 
  <ul>
    <li>Fitur-fitur apa saja yang berpengaruh dalam jumlah peningkatan penganggur, serta </li>
    <li> Tingkat performa akurasi untuk beberapa algoritma model yang digunakan </li>
  </ul> 
Harapannya, setelah membuat model, permasalahan-permasalahan tersebut dapat terjawab.</p>
<p>Metodologi yang dipakai untuk jenis permasalahan tersebut ialah menggunakan prediksi regresi linear dengan variabel 'penganggur' (<i>unemployed</i>) sebagai hasil dari komputasi (output). </p>
<h3> Solution Statement </h3>
<hr>
<p> Model kemudian dibuat dengan melakukan pemrosesan data terlebih dahulu seperti normalisasi serta pembagian data menjadi training, dan test set, serta melakukan penerapan model tiga algoritma machine learning (K-Nearest Neighborhood, Random Forest, Boosting Algorithm) <sup>[2]</sup>. Pertimbangan menggunakan tiga model tersebut ialah dengan tujuan mengetahui model mana yang paling memberikan performansi paling optimal bagi model. </p>
<p> Matrik yang digunakan untuk mengetahui kualitas dari model yang dibuat ialah menggunakan metrik yang sudah banyak dikenal, yakni MSE (Mean Squared Error)<sup>[3]</sup>, dengan cara menghitung total perbedaan antara poin prediksi dengan poin hasil dikuadratkan kemudian dilakukan pembagian sesuai dengan jumlah data yang digunakan. </p>


<img src="https://user-images.githubusercontent.com/75966846/181481783-b786fb77-54f6-4a90-8367-aeddf6c1a49a.png">
<p>(<i>source</i> :<a href=https://www.coursera.org/learn/machine-learning/home/week/1">DeepLearning.AI</a>) </p>

<p>Dalam pembuatannya, model akan dibuat dengan menggunakan spesifikasi sebagai berikut :
<ul>
	<li>Bahasa Pemrograman Python</li>
	<li><i>Library</i> NumPy, Pandas, Matplotlib, dan Seaborn</li>
	<li> Google Colab</li>

<h2>Data Understanding</h2>
<hr>
<p> Dalam pembuatan model prediktif ini, digunakan dataset yang diambil dari dataset salah satu <i>library</i> yang tersedia dalam bahasa pemrograman R
(tidyverse), yaitu <i>Economics</i>. Data ini diambil dari Federal Reserve Bank of St. Louis, salah satu bank penyedia jasa data pertumbuhan ekonomi untuk negara-negara bagian Amerika Serikat. </p>

<image src="https://user-images.githubusercontent.com/75966846/181481554-1de8ce89-c776-4a2f-869e-e50372ed42dd.png">
  <p>(<i>source</i> :<a href="https://fred.stlouisfed.org/">Federal Reserve Economic Data RED  St. Louis Fed</a>)</p>

<p>Dataset yang disediakan tersebut mencakup beberapa variabel yang dianggap penting, beberapa variabel tersebut ialah data terkait populasi, jumlah pengangguran, dan konsumsi pribadi serta tahun dan bulan. Dataset ini dihasilkan dari data deret waktu (<i>Time  Series</i>) ekonomi AS yang tersedia dari Federal Reserve Bank of St. Louis.</p>
<p>Deskripsi terkait variabel dataset diuraikan sebagai berikut

<img src="https://user-images.githubusercontent.com/75966846/181481603-f78b936f-6d81-470c-9955-fae299a4cc19.png">
</p>
  <p>(<i>source</i>:<a href="https://www.rpubs.com/mperlow/552127">RPubs - Economics Data</a>)</p>
  <h2> Data Preparation</h2>
  <hr>
<p>Dataset tersebut kemudian dilakukan <i>preprocessing</i> data terlebih dahulu karena data tersebut masih dalam keadaan mentah (<i>raw</i>) sehingga perlu penyesuaian sedemikian rupa agar dataset tersebut dapat digunakan dengan baik oleh <i> Machine Learning Engineer</i>. Beberapa langkah <i>preprocessing</i> tersebut mencakup pengubahan tipe data agar dapat diimplementasikan perubahan yang diinginkan, penggantian index baris, penggantian kolom untuk kemudahan dalam pembuatan model, serta memastikan tidak adanya dataset yang bernilai <i>null</i>.</p>

<p>Setelah dilakukan proses <i>preprocessing</i> data, dataset tersebut dilakukan eksplorasi analisis data dengan tujuan lebih memahami dataset yang digunakan. Beberapa analisis yang dilakukan mencakup analisis statistika dasar serta analisis korelasi antar variabel. Dikarenakan dataset tidak memiliki variabel yang bersifat kategorik, sehingga hanya dilakukan untuk variabel numerik.</p>

  <img src="https://user-images.githubusercontent.com/75966846/181481647-b08cad36-a656-4b6e-8357-cfcf20dd7e56.png">
  
  (<i>Source</i> : Dokumentasi Pribadi)

Hasil matriks tersebut mendeskripsikan bahwa terdapat korelasi lemah antara variabel 'psavert' dengan variabel target, yaitu 'unemploy' serta memiliki korelasi cukup tinggi dengan 'uempmed', 'pop' dan 'pce'. Dari hasil ini, kita dapat mengabaikan variabel 'psavert', tentunya berdasarkan standar dari masing-masing bidang (kesehatan, ekonomi, dan lainnya, contohnya: korelasi yang jauh lebih rendah lebih dibutuhkan di bidang medis yang dianggap sangat berpengaruh dan krusial dibandingkan dengan bidang teknologi). Sehingga, variabel 'psavert' dapat dihilangkan dikarenakan memiliki nilai korelasi dibawah 0.5.

Dataset yang sudah dilakukan proses <i>preprocessing</i> serta dilakukan eksplorasi data analisis, dapat langsung dilakukan pembagian data berdasarkan training dan test set dengan tujuan memudahkan pembuatan model Machine Learning. Pembagian dataset tersebut dilakukan dengan mengutamakan data untuk training lebih besar, mengingat kebutuhan data sangat penting untuk model Machine Learning yang menggunakan algoritma Supervised Learning agar target dapat didapatkan dengan baik. Pembagian dataset dapat dilakukan dengan pembagian (8:2 atau (9:1) sesuai kumpulan data yang tersedia. Pembuatan model ini akan menggunakan perbandingan 9:1 untuk kumpulan data training dan test, secara berurutan.

<h2>Modelling</h2>
<hr>
<p>Seperti yang sudah diuraikan, proses pembuatan model ini akan menggunakan tiga model algoritma machine learning (K-Nearest Neighborhood, Random Forest, dan Boosting Algorithm). 
Ketiga model algoritma tersebut kemudian dilakukan perbandingan hasil untuk menentukan model yang paling memberikan akurasi cukup tinggi dengan menghitung nilai mse (<i>mean squared error</i>). </p>

<p>Tahapan yang dilakukan untuk setiap pembuatan model tersebut ialah dengan menggunakan fungsi method yang sudah disediakan melalui <i>library</i> Scikitlearn. Perlu diketahui, sebelum dilakukan tahap proses modelling, Anda perlu menerapkan proses normalisasi terhadap test data dengan tujuan agar test data berasal dari lingkungan yang seragam dengan data training yang digunakan untuk mode pelatihan.</p>
<h2>Evaluation</h2>
<hr>
Setelah dilakukan proses modelling dengan menentukan metrik yang digunakan untuk setiap algoritma serta melakukan <i>hyperparameter tuning</i> hingga menghasilkan mse yang minimum, Anda dapat melakukan evaluasi model dengan menggunakan parameter metrik yang sudah disebutkan di atas, yaitu metrik mse (<i>mean suared error</i>). Mse merupakan salah satu metrik evaluasi yang sering digunakan dalam perhitungan regresi linear. Metrik ini secara spesifik bekerja dengan menghitung hasil kuadrat jumlah selisih nilai prediksi dengan nilai hasil aktual kemudian dibagi dengan jumlah data, atau biasa dikenal sebagai <i> Cost Function </i> (Fungsi Biaya). 

<p>Hasil performansi dari ketiga algoritma tersebut menunjukkan perbedaan yang cukup signifikan bagi model. Performansi menunjukkan bahwa algoritma Random Forest memiliki nilai mse yang lebih kecil dibandingkan dengan kedua model lainnya, salah satunya, dengan nilai mse mencapai nilai 1750 untuk KNN yang merupakan model yang memiliki nilai error paling besar dibandingkan dengan Random Forest yang memiliki nilai error paling kecil dibandingkan ketiga model.</p>

  <img src = "https://user-images.githubusercontent.com/75966846/181481694-7fdda997-e270-480e-bb26-e5fc0f5b0344.png">
  
  (<i>source</i> : Dokumentasi Pribadi)

<p> Kemudian, dilakukan <i>plotting</i> untuk hasil perhitungan mse tersebut dengan tujuan agar lebih mudah dalam memahami hasil mse yang dihaslkan oleh metrik tersebut.

  <img src="https://user-images.githubusercontent.com/75966846/181481720-887cce8e-7300-4f1f-91b1-7b353fce2d65.png">

  (<i>source</i> : Dokumentasi Pribadi)

Setelah penghitungan nilai mse, model dilakukan prediksi nilai dengan tujuan mengetahui prediksi yang akan dibuat.
<img src="https://user-images.githubusercontent.com/75966846/181481904-7b563327-aa44-4443-9b85-9a9ce070e1ad.png">

  (<i>source</i> : Dokumentasi Pribadi)

Berdasarkan hasil tersebut, model algoritma Random Forest pun dipilih sebagai algoritma yang digunakan untuk tujuan dari pengembangan model machine learning tersebut. Hal ini dikarenakan algoritma Random Forest merupakan sekumpulan algoritma yang saling bekerja sama (<i>ensemble model </i>) yang menggunakan konsep paralel (<i>bagging</i>) dibandingkan dengan konsep Boosting model yang menggunakan konsep secara sekuensial<sup>[4]</sup>. Namun, meski algoritma Random Forest berjalan sangat baik di sebagian permasalahan machine learning, beberapa algoritma yang belum dicoba seperti XGBoost, *deep learning* pada kumpulan data yang lebih besar, dan beberapa algoritma *supervised learning* lainnya sering unggul dari segi performa. Hal ini sangat tergantung pada banyak kasus seperti jumlah dataset serta permasalahan yang akan diselesaikan. </p>

  
  <h2> Kesimpulan </h2>
  <hr>
<p> Dalam pembuatan model linear regresi menggunakan dataset Federal Reserved Economic Data (FRED), variabel yang berpengaruh bagi target adalah variabel 'uempmed’, ‘pop’, dan ‘pce’ berdasarkan matriks korelasi. Ketiga variabel tersebut adalah variabel 'Nilai median tidak bekerja', 'Populasi', dan 'Pengeluaran konsumsi pribadi'.</p>
<p> Model dengan akurasi paling tinggi dimiliki oleh model dengan algoritma Random Forest dikarenakan proses <i>bagging</i> (paralel) yang dimilikinya menjadi salah satu keunggulan tersendiri dibandingkan dengan gabungan model lainnya.</p>

  <h2>Daftar Pustaka</h2>
<hr>

>[1]
Iulia CRISTINA Iuga, “Analysis of correlation between the unemployment rate and gross domestic product in the European union,” _ResearchGate_, 2013. https://www.researchgate.net/publication/268980711_Analysis_of_correlation_between_the_unemployment_rate_and_gross_domestic_product_in_the_European_union (accessed Jul. 28, 2022).


> [2]
Andrew, Ng.  *Machine Learning Specialization: Supervised Machine Learning, Regression and Classification*. DeepLearning.AI. 2022. https://www.coursera.org/learn/machine-learning/home/welcome

> [3}
>Dicoding Indonesia. *Machine Learning Terapan*. Dicoding Indonesia. 2022.
>https://www.dicoding.com/academies/319/corridor

>[4}
L. Chen, “Basic Ensemble Learning (Random Forest, AdaBoost, Gradient Boosting)- Step by Step Explained,”  _Medium_, Jan. 02, 2019. https://towardsdatascience.com/basic-ensemble-learning-random-forest-adaboost-gradient-boosting-step-by-step-explained-95d49d1e2725 (accessed Jul. 28, 2022).

‌
