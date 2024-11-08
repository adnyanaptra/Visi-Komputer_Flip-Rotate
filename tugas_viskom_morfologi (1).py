# -*- coding: utf-8 -*-
"""Tugas Viskom Morfologi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mRWl9qTXT8UZtgQB91O7eXQx3x5z3Rcc

**Morfologi Dilasi**
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar input dalam mode warna
img = cv2.imread('/content/photo_2024-11-05_09-52-12.jpg', cv2.IMREAD_COLOR)

# Membuat elemen struktural kernel (misalnya matriks persegi 5x5)
kernel = np.ones((3, 3), np.uint8)

# Melakukan operasi dilasi
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Menampilkan hasil gambar asli dan gambar setelah dilasi
plt.subplot(1, 2, 1)
plt.title('Original Image')
# Konversi dari BGR ke RGB agar tampil dengan benar di matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Dilated Image')
# Konversi dari BGR ke RGB untuk hasil gambar dilasi
plt.imshow(cv2.cvtColor(dilated_img, cv2.COLOR_BGR2RGB))

plt.show()

"""**Morfologi Erosi**

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar input (warna)
img = cv2.imread('/content/photo_2024-11-05_10-09-43.jpg', cv2.IMREAD_COLOR)

# Membuat elemen struktural kernel (misalnya matriks persegi 5x5)
kernel = np.ones((3, 3), np.uint8)

# Melakukan operasi erosi
eroded_img = cv2.erode(img, kernel, iterations=1)

# Menampilkan gambar asli dan gambar hasil erosi
plt.subplot(1, 2, 1)
plt.title('Original Image')
# Konversi dari BGR ke RGB agar ditampilkan dengan benar di matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Eroded Image')
# Konversi dari BGR ke RGB untuk gambar hasil erosi
plt.imshow(cv2.cvtColor(eroded_img, cv2.COLOR_BGR2RGB))

plt.show()

"""**Morfologi Opening**"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar input (grayscale)
img = cv2.imread('/content/35021156933271131014.png', 0)

# Membuat elemen struktural kernel (misalnya matriks persegi 5x5)
kernel = np.ones((5, 5), np.uint8)

# Melakukan operasi opening (erosi diikuti dengan dilasi)
opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Menampilkan gambar asli dan gambar hasil opening
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Opening Image')
plt.imshow(opening_img, cmap='gray')

plt.show()

"""**Morfologi Closing**"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar berwarna (tidak grayscale)
img = cv2.imread('/content/6372f06cd49fb.jpg')

# Membuat elemen struktural kernel (misalnya matriks persegi 5x5)
kernel = np.ones((8, 8), np.uint8)

# Melakukan operasi closing (dilasi diikuti dengan erosi)
closing_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Menampilkan gambar asli dan gambar hasil closing
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Closing Image')
plt.imshow(cv2.cvtColor(closing_img, cv2.COLOR_BGR2RGB))

plt.show()

"""**Morfologi Hit Or Miss**"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar dan mengubahnya ke grayscale
img = cv2.imread('/content/images (4).jpg', 0)

# Mengonversi gambar grayscale menjadi gambar biner (thresholding)
# Semua pixel yang lebih dari 127 menjadi 1 (putih), dan sisanya menjadi 0 (hitam)
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Membuat elemen struktural untuk Hit-or-Miss
# Elemen ini adalah kernel yang akan mencocokkan pola
# Kernel ini dapat dimodifikasi sesuai pola yang ingin dicari
kernel = np.array([[0, 1, 0],
                   [1, -1, 1],
                   [0, 1, 0]], dtype=np.int8)

# Melakukan operasi Hit-or-Miss
hit_or_miss_img = cv2.morphologyEx(binary_img, cv2.MORPH_HITMISS, kernel)

# Menampilkan gambar asli biner dan hasil hit-or-miss
plt.subplot(1, 2, 1)
plt.title('Binary Image')
plt.imshow(binary_img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Hit-or-Miss Result')
plt.imshow(hit_or_miss_img, cmap='gray')

plt.show()

"""**Morfologi Skeletonization**"""

import cv2
import numpy as np
from skimage.morphology import skeletonize
from matplotlib import pyplot as plt

# Membaca gambar dan mengubahnya ke grayscale
img = cv2.imread('/content/5-motif-batik-yang-mudah-digambar.webp', 0)

# Mengonversi gambar grayscale menjadi gambar biner (thresholding)
# Semua pixel yang lebih dari 127 menjadi 1 (putih), dan sisanya menjadi 0 (hitam)
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Membalik gambar biner (karena skimage skeletonize menganggap latar belakang 0 dan objek 1)
binary_img = cv2.bitwise_not(binary_img)

# Normalisasi nilai pixel ke rentang 0 dan 1 untuk skimage
binary_img = binary_img // 255

# Melakukan skeletonization
skeleton = skeletonize(binary_img)

# Mengonversi kembali ke rentang 0-255 untuk ditampilkan
skeleton = (skeleton * 255).astype(np.uint8)

# Menampilkan gambar asli biner dan hasil skeletonization
plt.subplot(1, 2, 1)
plt.title('Binary Image')
plt.imshow(binary_img * 255, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Skeletonized Image')
plt.imshow(skeleton, cmap='gray')

plt.show()