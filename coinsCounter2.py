from cv2 import cv2
import numpy as np

img = cv2.imread('Path to your image')

radius = []
coins = []
five, ten, fifty = 0, 0, 0

def detectCircles(imgAux, img):
    circles = cv2.HoughCircles(imgAux, cv2.HOUGH_GRADIENT, 1, 50, param1=255, param2=35, minRadius=30, maxRadius=300)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype('int')

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 3)
            radius.append([r, x, y])
            

height, width = img.shape[0], img.shape[1]

img = cv2.resize(img, (width, height))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.medianBlur(imgGray, 7)

detectCircles(imgBlur, img)

cv2.imwrite('Desired path to your image', img)

radius.sort()
minim = radius[0][0]
    
for i in radius:
    coins.append(i[0] / minim)

print(radius)
print(coins)

for coin in coins:
    if coin <= 1.08: five += 1
    elif coin <= 1.25: ten += 1
    else: fifty += 1
    
print('You have ' + str(len(coins)) + ' coins')

print('5: ' + str(five) + ' coins')
print('10: ' + str(ten) + ' coins')
print('50: ' + str(fifty) + ' coins')

sum = five * 5 + ten * 10 + fifty * 50
print ('Total sum is: ' + str(sum / 100) + ' lei')

cv2.waitKey(0)

"""
REUIREMENTS BEFORE USING THE SCRIPT:
1. DO NOT MAKE THE PHOTO TO CLOSE TO THE GROUND. DISTORTION LENS DESTROY THE ACCURACY
2. USE APPROPRIATE GROUND WITH CONTRAST. WORKS BEST ON BLACK
3. DO NOT PUT THE COINS TO CLOSE TO EACH OTHER
"""
