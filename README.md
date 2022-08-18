# Phyton-Patika.dev-Projesi
Patika.dev Temel Phyton derslerinin proje ödevidir

# SORULAR VE CEVAPLAR
**1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de** **oluşabilir. Örnek olarak:**

**input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]**

**output: [1,'a','cat',2,3,'dog',4,5]**

**ÇÖZÜM 1**

Flatten adında düzleştirici bir fonksiyon oluşturarak verilen içinde list bulundurulan bir list'i listlerden arındırdık. Fonksiyonumuz ilk önce ögeleri tek tek ayırıp list olup olmadığını sorguluyor. Eğer list tipinde ise bu işlemi tipi list olmayana kadar tekrarlıyor. Eğer list değil veya fonksiyon sayesinde düzleştirilmişse kendi oluşturduğumuz yeni listenin içine ekliyor. En sonunda ise fonksiyon olarak oluşturduğumuz yeni listeyi return ediyor.

#

**2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine** **döndürün. Örnek olarak:**

**input: [[1, 2], [3, 4], [5, 6, 7]]**

**output: [[[7, 6, 5], [4, 3], [2, 1]]**

**ÇÖZÜM 1**

Reverse adını verdiğimiz fonksiyon ilk önce fonksiyonun içindeki ögeleri tersine dödürüyor. Sonrasında ögelere tek tek bakıyor ve eğer list bulursa list'i de kendi içinde ters çeviriyor.
