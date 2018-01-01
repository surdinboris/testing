from faker import Factory

fake = Factory.create('ru')

def getatt(att):
    return(getattr(fake, att)())

for t in range(200):
    print(getatt("hex_color"))