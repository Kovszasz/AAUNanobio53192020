#Author: Szabolcs Cselgo Kovacs
#This script extracts information from the merges file of '.arc' of MOPAC output file

length=input('Number of QM regions:\t')
path=input('Path:\t')
def extract_homo(string):
#    print(string)
    string=string.replace(' ',',').replace('\n','').split(',')
#    print(string)
    if string[-2]=='':
        string[-2]=string[-3]
    return string[-2]+','+string[-1]

def converter(string,t):
    if t== 'DIPOLE':
        string=string.replace('DEBYE',';')
    elif t=='HOMO':
        return extract_homo(string)
    elif t=='TOTAL':
        string=string.replace('EV',';')
    string.replace(' ','')
    string=list(string)
    while string[-1]!=';':
        string.pop()
    string.pop()
    string.pop()
    string="".join(string)
    string=string.replace(' ','')
    string=string.split('=')
    return string[1]

def findt(l):
    variables=['DIPOLE','HOMO','TOTAL']
    for v in variables:
        file=path+"QMMM_qmout."+str(l)+".arc"
        rf=open(path+v+str(l)+".txt",'w')
        with open(file,'r') as f:
            for i in f:
                if i.find('PM7')==-1:
                    if i.find(v)>-1:
                        rf.write(converter(i,v)+'\n')

for i in range(int(length)):
    findt(i)
