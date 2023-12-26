import cv2

# READ IMAGE
img = cv2.imread("solar_system.jpeg")


cv2.putText(img,
            "Sun",
            (140,100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255))

cv2.putText(img,
            "Mercury",
            (225,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (300,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (350,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (410,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (550,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (800,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (990,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1120,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

#DISPLAY COLORED IMAGE
cv2.imshow("output", img)

cv2.waitKey(0)