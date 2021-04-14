def check(bl,sl):
    if sl[0]<(bl[0]+30) and sl[0]>(bl[0]-30):
        if sl[1]<(bl[1]+30) and sl[1]>(bl[1]-30):
            if sl[2]<(bl[2]+30) and sl[2]>(bl[2]-30):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#check([10,20,30],[25,30,40])