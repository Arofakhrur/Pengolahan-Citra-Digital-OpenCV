import numpy as np
import cv2 as cv

# Variabel global untuk menggambar
drawing = False  # True jika tombol mouse ditekan
ix, iy = -1, -1  # Koordinat awal saat mouse ditekan
brush_radius = 5  # Jari-jari kuas awal

# Fungsi untuk menggambar lingkaran saat mouse bergerak
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, brush_radius

    if event == cv.EVENT_LBUTTONDOWN:  # Jika tombol kiri mouse ditekan
        drawing = True  # Mulai menggambar
        ix, iy = x, y  # Simpan posisi awal

    elif event == cv.EVENT_MOUSEMOVE:  # Jika mouse bergerak
        if drawing:  # Jika menggambar aktif
            cv.circle(img, (x, y), brush_radius, (b, g, r), -1)  # Gambar lingkaran

    elif event == cv.EVENT_LBUTTONUP:  # Jika tombol kiri mouse dilepaskan
        drawing = False  # Selesai menggambar
        cv.circle(img, (x, y), brush_radius, (b, g, r), -1)  # Gambar lingkaran di posisi akhir

# Fungsi dummy untuk trackbars
def nothing(x):
    pass

# Membuat gambar putih, jendela, dan mengaitkan fungsi callback ke jendela
img = np.ones((512, 512, 3), np.uint8) * 255  # Inisialisasi gambar dengan warna putih
cv.namedWindow('Paint')
cv.setMouseCallback('Paint', draw_circle)

# Membuat trackbars untuk warna RGB
cv.createTrackbar('R', 'Paint', 0, 255, nothing)
cv.createTrackbar('G', 'Paint', 0, 255, nothing)
cv.createTrackbar('B', 'Paint', 0, 255, nothing)

# Membuat trackbar untuk jari-jari kuas
cv.createTrackbar('Brush Size', 'Paint', brush_radius, 50, nothing)

while True:
    cv.imshow('Paint', img)  # Tampilkan gambar di jendela 'Paint'

    # Mendapatkan nilai dari trackbars untuk warna RGB
    r = cv.getTrackbarPos('R', 'Paint')
    g = cv.getTrackbarPos('G', 'Paint')
    b = cv.getTrackbarPos('B', 'Paint')

    # Mendapatkan nilai dari trackbar untuk jari-jari kuas
    brush_radius = cv.getTrackbarPos('Brush Size', 'Paint')

    # Jika tombol 'Esc' ditekan, keluar dari loop
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()  # Tutup semua jendela
