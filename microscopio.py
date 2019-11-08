#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:36:17 2019

@author: usuario
"""

import numpy as np
import cv2

img = cv2.imread("teste3.jpg")


# Converter para escala de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavização
gauss = cv2.GaussianBlur(cinza, (1,1), 0)


# Detectar bordas
canny = cv2.Canny(gauss, 50, 150)

# Buscamos os contornos
(_,contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos o numero de objetos na tela
print("Foram encontrados {} objetos".format(len(contornos)))

cv2.drawContours(img,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", img)
cv2.imwrite("resultado.jpg", img)


cv2.waitKey(0)
