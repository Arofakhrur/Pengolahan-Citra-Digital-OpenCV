import numpy as np
import cv2 as cv

# Variabel global untuk mengontrol proses menggambar
drawing = False  # True jika tombol mouse ditekan
mode = True  # True: mode menggambar persegi panjang; False: mode menggambar lingkaran
ix, iy = -1, -1  # Koordinat awal saat mouse ditekan

# Fungsi callback untuk event mouse
def draw_shapes(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # Event klik ganda tombol kiri untuk menggambar lingkaran besar
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)  # Lingkaran besar berwarna biru

    # Event menekan tombol kiri untuk memulai menggambar
    elif event == cv.EVENT_LBUTTONDOWN:
        drawing = True  # Mulai menggambar
        ix, iy = x, y  # Simpan koordinat awal mouse

    # Event mouse bergerak saat tombol kiri ditekan untuk menggambar
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:  # Mode menggambar persegi panjang
                img_copy = img.copy()  # Buat salinan gambar untuk menghindari tumpang tindih saat menggambar
                cv.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), -1)  # Persegi panjang berwarna hijau
                cv.imshow('image', img_copy)
            else:  # Mode menggambar lingkaran kecil
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)  # Lingkaran kecil berwarna merah

    # Event melepaskan tombol kiri untuk menyelesaikan menggambar
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False  # Selesai menggambar
        if mode:  # Gambar persegi panjang terakhir
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)  # Persegi panjang hijau terakhir
        else:  # Gambar lingkaran kecil
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)  # Lingkaran kecil merah terakhir

# Membuat gambar hitam, jendela, dan mengaitkan fungsi callback ke jendela
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_shapes)

while True:
    cv.imshow('image', img)  # Tampilkan gambar di jendela
    k = cv.waitKey(1) & 0xFF  # Tunggu input dari keyboard
    if k == ord('m'):  # Tekan 'm' untuk mengganti mode antara persegi panjang dan lingkaran
        mode = not mode
    elif k == 27:  # Tekan 'Esc' untuk keluar
        break

cv.destroyAllWindows()  # Tutup semua jendela
