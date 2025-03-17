import cv2
from PIL import Image
import numpy as np


def process(image):
    pil_image = Image.open(image)
    np_image = np.array(pil_image)
    p = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)

    # Aplica un gaussian blurr
    p_blurr  = cv2.GaussianBlur(p, (15, 15), 0)

    # Dilata la imagen para hacer los trazos mas gruesos y uniformes
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    img_dilatada = cv2.dilate(p_blurr, kernel, iterations=1)

    # Convierte la iamgen a blanco y negro (detecta bordes)
    res = cv2.adaptiveThreshold(img_dilatada, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 6)

    return res