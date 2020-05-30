#Author: Szabolcs Cselgo Kovacs
#This script extracts information from the merges file of '.arc' of MOPAC output file
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

length=int(input('Number of QM regions:\t'))
type_=input('LUMOcorr(l), BandGapcorr(b), HOMO(h):\t')
start_frame=int(input('Start frame:\t'))
end_frame=int(input('End frame:\t'))
heatmap={}
def white_space_remover(string):
   string=list(string)
   string.pop()
   string="".join(string)
   return string

def load(l):
    QMdict={l:[]}
    with open('HOMO'+str(l)+".txt",'r') as f:
        for i in f:
            s=white_space_remover(i)
            s=s.split(',')
            if type_=='h':
                QMdict[l].append(float(s[0]))
            elif type_=='l':
                QMdict[l].append(float(s[1]))
            elif type_=='b':
                QMdict[l].append(float(s[0])-float(s[1]))
            else:
                raise 'Please choos either \'h\' or \'l\' or \'b\' '
    return QMdict

def load6pep(l):
    QMdict={l:[]}
    if l==-1:
        d='HOMO0.alpha.txt'
    elif l==0:
        d='HOMO0.beta.txt'
    elif l==17:
        d='HOMO17.alpha.txt'
    elif l==18:
        d='HOMO17.beta.txt'
    else:
        d='HOMO'+str(l)+".txt"
    with open(d,'r') as f:
        for i in f:
            s=white_space_remover(i)
            s=s.split(',')
            if type_=='h':
                QMdict[l].append(float(s[0]))
            elif type_=='l':
                QMdict[l].append(float(s[1]))
            elif type_=='b':
                QMdict[l].append(float(s[0])-float(s[1]))
            else:
                raise 'Please choos either \'h\' or \'l\' or \'b\' '
    return QMdict


def loaddipole(l):
    QMdict={l:[]}
    with open('DIPOLE'+str(l)+".txt",'r') as f:
        for i in f:
            s=white_space_remover(i)
            QMdict[l].append(float(s))
    return QMdict

def loadtotal(l):
    QMdict={l:[]}
    with open('TOTAL'+str(l)+".txt",'r') as f:
        for i in f:
            s=white_space_remover(i)
            QMdict[l].append(float(s))
    return QMdict

for i in range(length):
    heatmap.update(load(i))

QMregions=['QM'+str(i) for i in heatmap.keys()]
HeatMapValues=[]
for i in heatmap.keys():
    row=[]
    for j in heatmap.keys():
        average=0
        for k in range(start_frame,end_frame):
            hm = abs(abs(heatmap[i][k])-abs(heatmap[j][k]))
            average = average+hm
        average=average/(end_frame-start_frame)
        row.append(round(average,3))
    HeatMapValues.append(row)
HeatMapValues=np.array(HeatMapValues)

fig, ax = plt.subplots()
im = ax.imshow(HeatMapValues)
ax.set_xticks(np.arange(len(QMregions)))
ax.set_yticks(np.arange(len(QMregions)))
ax.set_xticklabels(QMregions)
ax.set_yticklabels(QMregions)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
for i in range(len(QMregions)):
    for j in range(len(QMregions)):
        text = ax.text(j, i, HeatMapValues[i, j],
                       ha="center", va="center", color="w")
fig.tight_layout()

text=''
if type=='l':
    text='LUMOcorr'
elif type=='h':
    text='HOMOcorr'
elif type=='b':
    text='BandGapcorr'
#else:
#    raise 'Please choos either \'h\' or \'l\' or \'b\' '
ax.set_title(text)
plt.savefig(text+'.png')
