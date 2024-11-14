import cv2
import numpy as np
# Les bildet
image = cv2.imread('soppel.jpg')
#blå
blue_lower = np.array([0, 20, 100])
blue_upper = np.array([255, 255, 255])
# Lag masker for hver farge
blue_mask = cv2.inRange(image, blue_lower, blue_upper)
# Tell antall piksler for hver farge
blue_pixels = np.sum(blue_mask == 255)
# Total antall piksler i bildet
total_pixels = image.size // 3  # Delt på 3 for å få antall piksler (ikke fargekanaler)
# Beregn andel for hver type avfall
blue_percentage = (blue_pixels / total_pixels) * 100
total_percentage = (total_pixels-blue_pixels)/total_pixels*100
# Resultater
print(f'Andel blå: {blue_percentage:.2f}%')
print(f'Andel søppel: {total_percentage:.2f}%')

