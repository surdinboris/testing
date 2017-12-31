import os
prefs = ['050', '051', '052', '053', '054', '055', '056', '057', '058', '059']

def fun(*args, **kwargs):
    prefix = kwargs['pref']
    number = kwargs['nu']
    output = kwargs['outp']

    with open(os.path.join(os.getcwd(), output), 'w') as outputfile:
        while number <= 100:    #stopper
                number = number + 1
                print(''.join([prefix, str(number).zfill(7)]))
                outputfile.writelines(''.join([prefix, str(number).zfill(7)])+'\n')

        print(outputfile.name)
        outputfile.close()
for pref in prefs:
    fun(outp='output.log', pref=pref, nu=0000000)
