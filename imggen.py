import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from faker import Factory
from PIL import Image
from random import randint
#from PIL import ImageFilter

def getatt(att):
    return(getattr(fake, att)())

def lastn(fpath): #returns 'oldest' file to continue generating
    lastfiles=os.listdir(fpath)
    fnlist=[]
    for f in lastfiles:
        head, name = os.path.split(f)
        fn,ext=os.path.splitext(name)
        fnlist.append(fn)
    return max(fnlist)

def imgen(y):
    
    randval = randint(100, 1000)
    im_out=Image.new('RGB',(randval,randval),color=getatt('hex_color'))
    im_out.save(os.path.join(os.getcwd(),'output','out%000d.jpg' % y))
    return('out%000d.jpg' % y)



fake = Factory.create('ru')
if __name__ == "__main__":
    # for y in range(100):
    #     imgen(y)
    lastn(os.path.join(os.getcwd(), 'output'))