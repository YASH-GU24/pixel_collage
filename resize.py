import os
import cv2
directory = r'D:/projects/pixel collage/images'
i=0
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        print(os.path.join(directory, filename))
        img=cv2.imread(os.path.join(directory, filename),1)
        rimg=cv2.resize(img,(25,25))
        cv2.imwrite('resized_images/'+str(i)+'.jpg',rimg)
        i=i+1
    else:
        continue