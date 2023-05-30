# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import cv2
import matplotlib.pyplot as plt

# 이미지 읽기
image = cv2.imread('image.jpg')

# 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 라플라시안 필터 적용
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# 결과 이미지 출력
plt.imshow(laplacian, cmap='gray')
plt.axis('off')
plt.show()
