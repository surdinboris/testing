import os
from faker import Factory
from PIL import Image
from random import randint
#from PIL import ImageFilter

def getatt(att):
    return(getattr(fake, att)())

def lastn(fpath=os.path.join(os.getcwd(), 'output')): #returns 'oldest' file to continue generating
    lastfiles=os.listdir(fpath)
    fnlist=[0]
    try:
        for f in lastfiles:
            intlist = []
            head, name = os.path.split(f)
            fn,ext=os.path.splitext(name)
            for sym in fn:
                try:
                    intlist.append(int(sym))
                except ValueError:
                    pass
            fnlist.append(int((''.join(map(str, intlist)))))
    except ValueError:
           intlist=[0]
    return max(fnlist)


def imgen(ran):
    for y in range(ran):
        y=lastn()+1
     #correction procedure related to already generated files
        randval = randint(100, 1000)
        im_out=Image.new('RGB',(randval,randval),color=getatt('hex_color'))
        im_out.save(os.path.join(os.getcwd(),'output','out%000d.jpg' % y))



fake = Factory.create('ru')
if __name__ == "__main__":
    imgen(100)
