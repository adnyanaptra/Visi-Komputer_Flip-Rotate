# -*- coding: utf-8 -*-
"""Tugas Viskom Hough Transform.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AYbVuC4IhdTybB3Pph8NO8UPV2JdKTay

**Impor Library**
"""

import sys
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

"""**Deteksi Garis**"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar dan mengonversi ke citra grayscale
image = cv2.imread('/content/istilah-dalam-marka-jalan.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mendeteksi tepi menggunakan Canny edge detection
edges = cv2.Canny(gray, 230, 255, apertureSize=3)

# Melakukan transformasi Hough pada citra tepi
lines = cv2.HoughLinesP(edges, 1, np.pi/500, 15, minLineLength=1, maxLineGap=10)

# Membuat subplot
plt.figure(figsize=(8, 6))

# Menampilkan citra tepi
plt.subplot(1, 2, 1)
plt.imshow(edges, cmap='gray')
plt.title('Citra Tepi')
plt.axis('off')

# Menampilkan hasil Hough Line Transform
plt.subplot(1, 2, 2)
output_image = image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 1)
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title('Hasil Hough Line Transform')
plt.axis('off')

plt.tight_layout()
plt.show()

"""**Deteksi Garis Lurus**"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Read image
image = cv2.imread('/content/scrnli_8_15_2023_3-35-03 PM.png')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Apply HoughLinesP method to
# to directly obtain line end points
lines_list = []
lines = cv2.HoughLinesP(
    edges, # Input edge image
    1, # Distance resolution in pixels
    np.pi/180, # Angle resolution in radians
    threshold=100, # Min number of votes for valid line
    minLineLength=5, # Min allowed length of line
    maxLineGap=10 # Max allowed gap between line for joining them
)
# Iterate over points
for points in lines:
  # Extracted points nested in the list
  x1, y1, x2, y2 = points[0]
  # Draw the lines joining the points On the original image
  cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
  # Maintain a simple lookup list for points
  lines_list.append([(x1, y1), (x2, y2)])


# Display images using matplotlib
plt.figure(figsize=(10, 10))
# Display the edge-detected image (canny edges)
plt.subplot(1, 2, 1)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.xticks([]), plt.yticks([])
# Display the image with Hough Transform lines

plt.subplot(1, 2, 2)
im_with_lines = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
for line in lines_list:
  cv2.line(im_with_lines, line[0], line[1], (0, 255, 0), 2)

plt.imshow(im_with_lines)
plt.title('Grayscale Image with Hough Transform Lines')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()

"""**Deteksi Garis dan menampilkan panjang garis**"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
img = cv2.imread('/content/photo_2024-11-06_09-42-13.jpg')

# Mendapatkan resolusi gambar
height, width, channels = img.shape
print("Resolusi gambar:")
print("Lebar:", width, "piksel")
print("Tinggi:", height, "piksel")
print()

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menambahkan blur Gaussian
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Deteksi tepi menggunakan Canny
edges = cv2.Canny(blurred, 50, 270)

# Transformasi Hough untuk mendeteksi garis
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=130, minLineLength=340, maxLineGap=12)

# Gambar garis yang terdeteksi pada citra asli
if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            # Hitung panjang garis menggunakan formula jarak Euclidean
            line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            # Tampilkan panjang garis berdasarkan jumlah pixel pada gambar
            cv2.putText(img, f'{line_length:.0f} px', (int((x1 + x2) / 2), int((y1 + y2) / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}, Panjang garis: {line_length} piksel")

# Menampilkan citra menggunakan matplotlib
plt.figure(figsize=(12, 12))

# Menampilkan gambar grayscale
plt.subplot(2, 2, 1)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')

# Menampilkan gambar dengan Gaussian Blur
plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(blurred, cmap='gray')

# Menampilkan hasil deteksi tepi
plt.subplot(2, 2, 3)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

# Menampilkan hasil deteksi garis
plt.subplot(2, 2, 4)
plt.title('Line Detection')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
img = cv2.imread('/content/photo_2024-11-06_09-42-13.jpg')
output = img.copy()  # Salin gambar untuk menampilkan hasil akhir

# Mendapatkan resolusi gambar
height, width, channels = img.shape
print("Resolusi gambar:")
print("Lebar:", width, "piksel")
print("Tinggi:", height, "piksel")
print()

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menambahkan blur Gaussian
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Deteksi tepi menggunakan Canny
edges = cv2.Canny(blurred, 50, 270)

# Transformasi Hough untuk mendeteksi garis
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=130, minLineLength=340, maxLineGap=12)

# Gambar garis yang terdeteksi pada citra asli
if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 3)
            # Hitung panjang garis menggunakan formula jarak Euclidean
            line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            # Tampilkan panjang garis berdasarkan jumlah pixel pada gambar
            cv2.putText(output, f'{line_length:.0f} px', (int((x1 + x2) / 2), int((y1 + y2) / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}, Panjang garis: {line_length} piksel")

# Menghitung diagonal layar laptop
# Tentukan titik kiri atas dan kanan bawah dari layar laptop (misalnya)
top_left = (70, 60)  # Koordinat contoh, sesuaikan dengan posisi layar pada gambar
bottom_right = (690, 399)  # Koordinat contoh, sesuaikan dengan posisi layar pada gambar

# Menggambar garis diagonal pada layar
cv2.line(output, top_left, bottom_right, (255, 0, 0), 2)

# Menghitung panjang diagonal layar
diagonal_length_screen = ((bottom_right[0] - top_left[0]) ** 2 + (bottom_right[1] - top_left[1]) ** 2) ** 0.5
print(f"Jarak diagonal layar laptop: {diagonal_length_screen:.2f} piksel")

# Tampilkan panjang diagonal layar pada gambar
cv2.putText(output, f'Diagonal Screen: {diagonal_length_screen:.0f} px',
            (top_left[0] + 10, top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Menampilkan citra menggunakan matplotlib
plt.figure(figsize=(12, 12))

# Menampilkan gambar grayscale
plt.subplot(2, 2, 1)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')

# Menampilkan gambar dengan Gaussian Blur
plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(blurred, cmap='gray')

# Menampilkan hasil deteksi tepi
plt.subplot(2, 2, 3)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

# Menampilkan hasil deteksi garis dan garis diagonal layar
plt.subplot(2, 2, 4)
plt.title('Line & Diagonal Detection')
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

plt.show()

"""**Deteksi lingkaran dan menampilkan diameter lingkaran**"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

# Baca gambar
image = cv2.imread('/content/a238294f7c978cdde239fcd6bb927521.jpg')
output = image.copy()

# Mendapatkan resolusi gambar
height, width, channels = image.shape
print("Resolusi gambar:")
print("Lebar:", width, "piksel")
print("Tinggi:", height, "piksel")
print("\n")

# Tampilkan gambar asli
print("Gambar asli")
cv2_imshow(image)
print("\n")

# Mengonversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print("Gambar grayscale")
#cv2_imshow(gray)
#print("\n")

# Deteksi tepi menggunakan Canny
edges = cv2.Canny(gray, 230, 255, apertureSize=3)
#print("Gambar Edges")
#cv2_imshow(edges)
#print("\n")

# Mengaplikasikan Gaussian Blur
gray = cv2.GaussianBlur(gray, (5, 5), 2)
#print("Gambar blur")
#cv2_imshow(gray)
#print("\n")

# Mendeteksi lingkaran dengan HoughCircles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=90, param2=44, minRadius=19, maxRadius=100)

# Memastikan setidaknya satu lingkaran telah terdeteksi
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]

        # Hitung diameter
        diameter = radius * 2
        print(f"Diameter lingkaran: {diameter} piksel")

        # Menggambar lingkaran pada citra
        cv2.circle(output, center, radius, (255, 0, 0), 2)

        # Menggambar titik pusat lingkaran
        cv2.circle(output, center, 1, (0, 255, 0), 3)

        # Menambahkan teks diameter di dekat lingkaran
        text = f"{diameter} px"
        text_position = (i[0] - radius, i[1] - radius - 10)  # Posisi teks di atas lingkaran
        cv2.putText(output, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Cek apakah ada lingkaran yang terdeteksi
if circles is not None:
    circleCount = len(circles[0])
    print("Jumlah lingkaran: {n}".format(n=circleCount))
else:
    print("Tidak ada lingkaran yang terdeteksi.")

# Menampilkan citra menggunakan matplotlib
plt.figure(figsize=(12, 12))

# Menampilkan gambar grayscale
plt.subplot(2, 2, 1)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')

# Menampilkan gambar dengan Gaussian Blur
plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(gray, cmap='gray')

# Menampilkan hasil deteksi tepi
plt.subplot(2, 2, 3)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

# Menampilkan hasil deteksi garis
plt.subplot(2, 2, 4)
plt.title('Circle Detection')
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

plt.show()


# Menampilkan citra dengan lingkaran dan diameter
#cv2_imshow(output)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
from math import sqrt

# Baca gambar
image = cv2.imread('/content/a238294f7c978cdde239fcd6bb927521.jpg')
output = image.copy()

# Mendapatkan resolusi gambar
height, width, channels = image.shape
print("Resolusi gambar:")
print("Lebar:", width, "piksel")
print("Tinggi:", height, "piksel")
print("\n")

# Tampilkan gambar asli
print("Gambar asli")
cv2_imshow(image)
print("\n")

# Mengonversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deteksi tepi menggunakan Canny
edges = cv2.Canny(gray, 230, 255, apertureSize=3)

# Mengaplikasikan Gaussian Blur
gray = cv2.GaussianBlur(gray, (5, 5), 2)

# Mendeteksi lingkaran dengan HoughCircles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=90, param2=44, minRadius=19, maxRadius=100)

# Memastikan setidaknya satu lingkaran telah terdeteksi
if circles is not None:
    circles = np.uint16(np.around(circles))

    # Inisialisasi variabel untuk lingkaran paling kiri dan paling kanan
    leftmost_circle = None
    rightmost_circle = None

    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]

        # Hitung diameter
        diameter = radius * 2
        print(f"Diameter lingkaran: {diameter} piksel")

        # Menggambar lingkaran pada citra
        cv2.circle(output, center, radius, (255, 0, 0), 2)

        # Menggambar titik pusat lingkaran
        cv2.circle(output, center, 1, (0, 255, 0), 3)

        # Menambahkan teks diameter di dekat lingkaran
        text = f"{diameter} px"
        text_position = (i[0] - radius, i[1] - radius - 10)  # Posisi teks di atas lingkaran
        cv2.putText(output, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Menyimpan lingkaran paling kiri dan paling kanan
        if leftmost_circle is None or i[0] - radius < leftmost_circle[0] - leftmost_circle[2]:
            leftmost_circle = (i[0], i[1], radius)
        if rightmost_circle is None or i[0] + radius > rightmost_circle[0] + rightmost_circle[2]:
            rightmost_circle = (i[0], i[1], radius)

    # Menghitung jarak antar lingkaran terluar (kiri dan kanan)
    if leftmost_circle and rightmost_circle:
        x1, y1, r1 = leftmost_circle
        x2, y2, r2 = rightmost_circle
        distance = int(sqrt((x2 - x1)**2 + (y2 - y1)**2)) #rumus euclidian distance

        # Menggambar garis antara kedua lingkaran dan menampilkan jaraknya
        cv2.line(output, (x1 - r1, y1), (x2 + r2, y2), (0, 255, 0), 2)
        distance_text = f"Distance: {distance} px"
        midpoint = ((x1 - r1 + x2 + r2) // 2, (y1 + y2) // 2)
        cv2.putText(output, distance_text, midpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        print(f"Jarak antara lingkaran terluar kiri dan kanan: {distance} piksel")

# Cek apakah ada lingkaran yang terdeteksi
if circles is not None:
    circleCount = len(circles[0])
    print("Jumlah lingkaran: {n}".format(n=circleCount))
else:
    print("Tidak ada lingkaran yang terdeteksi.")

# Menampilkan citra menggunakan matplotlib
plt.figure(figsize=(12, 12))

# Menampilkan gambar grayscale
plt.subplot(2, 2, 1)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')

# Menampilkan gambar dengan Gaussian Blur
plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(gray, cmap='gray')

# Menampilkan hasil deteksi tepi
plt.subplot(2, 2, 3)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

# Menampilkan hasil deteksi garis
plt.subplot(2, 2, 4)
plt.title('Circle Detection')
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

plt.show()