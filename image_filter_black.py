import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", default="image.png", nargs=1)
ap.add_argument("--scale", default=[100], type=int, nargs=1,
                help="Scale of black tolerance (default: 100). More - covert more to black.")
args = vars(ap.parse_args())

imagename = args["image"][0]
res_imagename = "res_" + imagename
print("res_imagename: " + res_imagename)

# Ielādējam attēlu
img = cv2.imread(imagename)

# sadalām attēlu pa krāsu slāņiem
b, g, r = cv2.split(img)

# samazinām katras krāsas intensitāti par scale vienībām
vienibas = args["scale"][0]
b = cv2.subtract(b, vienibas)
g = cv2.subtract(g, vienibas)
r = cv2.subtract(r, vienibas)

# tur, kur intensitāte ir mazāka par 0 gan b gan g gan r, iestatām 0, citādi iestādam 255
sum = cv2.add(b, g)
sum = cv2.add(sum, r)
ret, sum = cv2.threshold(sum, 0, 255, cv2.THRESH_BINARY)

# reizes = 3
# # samazinām attēlu 
# for i in range(reizes):
#     sum = cv2.pyrDown(sum)

# pārveidojam attēlu no pelēka tonu uz RGB
sum = cv2.cvtColor(sum, cv2.COLOR_GRAY2BGR)

# saglabājam rezultātu
cv2.imwrite(res_imagename, sum)
