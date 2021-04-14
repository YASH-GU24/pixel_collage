import cv2
import dshade
import os
import rcheck

#cv2.imshow('img',rimg1)
i=0
sl1=[]
directory = r'D:/projects/pixel collage/resized_images'
for i in range(0,1038):
                simg=cv2.imread(os.path.join(directory, str(i)+'.jpg'),1)
                sl1.append(dshade.dsahde(simg))
                i=i+1
base2=cv2.imread('base2.jpg',1)
base=cv2.resize(base2,(500,500))
y=0
x=0
min=255*3
dev=0
b=0
i=1
for x in range(0,500,25):
    for y in range(0,500,25):
        cimg=base[x:x+25,y:y+25]
        bl=dshade.dsahde(cimg)
        b=0
        min=255*3
        for i in range (1,1038):
            if os.path.exists(os.path.join(directory, str(i)+'.jpg')):
                #simg=cv2.imread(os.path.join(directory, str(i)+'.jpg'),1)
                if rcheck.check(bl,sl1[i]):
                    dev=abs(bl[0]-sl1[i][0])+abs(bl[1]-sl1[i][1])+abs(bl[2]-sl1[i][2])
                    if(dev<min):
                        min=dev
                        b=i
                else:
                    continue
            else:
                continue
        if b!=0:
            print(b)           
            simg=cv2.imread(os.path.join(directory, str(b)+'.jpg'),1)
            base[x:x+25,y:y+25]=cv2.addWeighted(simg, 0.5, base[x:x+25,y:y+25], 0.5,0)
            os.remove(os.path.join(directory, str(b)+'.jpg'))

        print(x,y)
        
cv2.imshow("image",base)
cv2.imwrite('final/'+'img_rg'+'.jpg',base)
cv2.waitKey(0)
cv2.destroyAllWindows()
