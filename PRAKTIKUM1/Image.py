import cv2 as cv #mengimpor modul openCV untuk pemrosesan gambar
import sys #Mengimpor modul sys untuk menangani operasi sistem, seperti keluar dari gambar

#fungsi imread membaca gambar dari direktori
img = cv.imread(cv.samples.findFile(r"C:\Users\Arofakhrur\Downloads\image (1).jpg"))

#fungsi untuk menentukan apakah format gambar didukung, atau sebaliknya
if img is None:
    sys.exit("format gambar tidak di dukung!")

#fungsi imshow menampilkan gambar ke layar dengan GUI dengan pesan "Display window"    
cv.imshow("Display window", img)

#menyimpan nilai dari tombol yang di tekan (s) ke variabel 'K'
k = cv.waitKey(0)

# tombol 's' berguna untuk menyimpan gambar dan mengganti format penamaannya menjadi "hasil.jpg" 
if k == ord("s"):
    cv.imwrite("hasil.jpg", img)
