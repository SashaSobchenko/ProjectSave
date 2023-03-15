import cv2
from PIL import Image


image_path = "38c28af56ba152f986f042def45e07f9.jpg"

image = cv2.imread(image_path)


cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
glasses = Image.open("pngimg.com - glasses_PNG54332.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses,(x,int(y+h/4)), glasses)
    cat.save("cat_glasses.png")
    cat_with_glasses = cv2.imread("cat_glasses.png")
    cv2.imshow("Cat_glasses", cat_with_glasses)
    cv2.waitKey()
