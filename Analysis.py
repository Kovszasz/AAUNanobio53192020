#Author: Szabolcs Cselgo Kovacs
#This script extracts information from the merges file of '.arc' of MOPAC output file
import numpy as np
from matplotlib import pyplot as plt
import math
import seaborn as sns
length=int(input('Number of QM regions:\t'))
prefix=input('The prefix of filename:\t')
type=input("Type of histogram (2D,angle,distance):\t")
class QMregion():
    def __init(id):
        self.id=id
        self.dipole=0
        self.angle={}
        self.distance={}

    def add_dispair(self,other,distance):
        self.distance.update({other.id:other.distance})

    def add_angpair(self,other,angle):
        self.angle.update({other.id: angle})

class TrajectoryFrame():
    def __init__(id):
        self.id = id
        self.QMregions=[]
    def add_QMregion(self,QM):
        self.QMregions.append(QM)

def loaddata(QMnumber,prefix):
    trajectory=[]
    filenames=['_dist','_angle','_dipole']
    for f in filenames:
        with open(prefix+f+'.dat','r') as file:
            for i in file:
                QM1={'dipole':[],'qm':[]}
                i=list(i)
                i.pop()
                i.pop()
                i=''.join(i)
                i=i.replace(',;',':')
                i=i.split(';')
                l=i[1].split(':')
                if f == '_dist':
                    for qm1 in range(length):
                        r=l[qm1].split(',')
                        QM2=[]
                        for qm2 in range(length):
                            QM2.append([float(r[qm2])])
                        QM1['qm'].append(QM2)
                    trajectory.append(QM1)
                elif f == '_angle':
                    for qm1 in range(length):
                        r=l[qm1].split(',')
                        for qm2 in range(length):
                            trajectory[int(i[0])]['qm'][qm1][qm2].append(math.acos(round(float(r[qm2]),8))/math.pi)
                else:
                    for qm in l:
                        trajectory[int(i[0])]['dipole'].append(float(qm))
    return trajectory

pairinecies=[[0,5],[5,6],[1,4],[4,7],[2,3],[3,8],[9,14],[14,15],[10,13],[13,16],[11,12],[12,17]]


def histo(data,length,type='2D'):
    dist=[]
    angle=[]
    for i in data:
        for j in range(length):
            for k in range(length):
                if j!=k:
                    dist.append(i['qm'][j][k][0])
                    angle.append(i['qm'][j][k][1])
    if type == '2D':
        plt.hist2d(dist, angle, bins=(200, 200), cmap=plt.cm.jet)
        plt.xlabel('Distance between PHE rings [A]')
        plt.ylabel('Angle between PHE rings [pi/rad]')
        cb=plt.colorbar()
        cb.ax.set_ylabel('Frequency')
    elif type == 'angle':
        plt.hist(angle,bins=200)
        plt.xlabel('Angle between PHE rings [pi/rad]')
        plt.ylabel('Frequency')
    elif type == 'distance':
        plt.hist(dist,bins=200)
        plt.xlabel('Distance between PHE rings [A]')
        plt.ylabel('Frequency')
    plt.show()

def DipoleScatter(data,length):
    dipole1=[i['dipole'][0] for i in data]
    dipole2=[i['dipole'][1] for i in data]
    dipole3=[i['dipole'][2] for i in data]
    angle=[]
    #for i in data:
        #for j in range(length):
    #        for k in range(length):
    #            if j!=k:
    #                dipole1.append(i['dipole'][j])
    #                dipole2.append(i['dipole'][k])
    #                angle.append(i['qm'][j][k][1])
    #plt.scatter(angle,dipole1, s=2)
    #plt.show()
    plt.figure(figsize=(16,10), dpi= 80)
    sns.kdeplot(dipole1, shade=True, color="g", label="Cyl=4", alpha=.7)
    sns.kdeplot(dipole2 == 5, shade=True, color="deeppink", label="Cyl=5", alpha=.7)
    sns.kdeplot(dipole3 == 6,shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)

    # Decoration
    plt.legend()
    plt.show()

DATA=loaddata(length,prefix)
#histo(DATA,length,type)
DipoleScatter(DATA,length)
DATA1p={}
for i in ['h','l','b']:
    type_=i
    DATA1p[i]={}
    for j in range(3):
        DATA1p[i].update(load(j))


DATA6pe['dipole']={}
for i in range(18):
     DATA6pe['dipole'].update(loaddipole(i))



DATA6pe={}
for i in ['h','l','b']:
    type_=i
    DATA6pe[i]={}
    for j in range(-1,19):
        DATA6pe[i].update(load6pep(j))

def cont(list1,list2):
    return list+list2
import matplotlib.pyplot as plt
import numpy as np
def error_QMregions(data,start,end,length):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    xl=[]
    for i in range(start,end):
        if i==-1:
            s='1\u03B1'
        elif i==0:
            s='1\u03B2'
        elif i==17:
            s='18\u03B1'
        elif i==18:
            s='18\u03B2'
        else:
            s=str(i+1)
        xl.append(s)
    x = [str(i) for i in range(20)]
    h = np.array([sum(data['h'][i])/len(data['h'][i]) for i in range(start,end)]) # Effectively y = x**2
    eh = np.array([np.std(data['h'][i]) for i in range(start,end)])

    l = np.array([sum(data['l'][i])/len(data['l'][i]) for i in range(start,end)]) # Effectively y = x**2
    el = np.array([np.std(data['l'][i]) for i in range(start,end)])

    b = np.array([sum(data['b'][i])/len(data['b'][i]) for i in range(start,end)]) # Effectively y = x**2
    eb = np.array([np.std(data['b'][i]) for i in range(start,end)])

    #dip = np.array([sum(data['h'][i])/len(data['h'][i]) for i in range(length)]) # Effectively y = x**2
    #edip = np.array([np.std(data['h'][i]) for i in range(length)])

    ax1.errorbar(xl, h, eh, linestyle='None', marker='^', color='blue', label='HOMO')
    ax1.errorbar(xl, l, el, linestyle='None', marker='o',color='red',label='LUMO')
    ax1.errorbar(xl, b, eb, linestyle='None',marker='x',color='green',label='Band gap')
    ax1.set_ylabel('Energy values [eV]')
    ax1.set_xlabel('Quantum regions')
    #plt.legend(loc='upper right');
    #ax1.errorbar(x, dip, edip, linestyle='None', marker='x',color='grey')
    plt.grid(axis='y',linestyle=':')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()


def averazier(data,start,end,length):
    returndata={}
    li=['h','l','b']
    for i in li:
        returndata[i]=[]
        for j in range(start,end):
            returndata[i]=returndata[i]+data[i][j]

    return returndata

def error_experiments(list_):#list containing p,pe,p6,p6e
    DATA={}
    x = ['1p', '1pe', '6p','6pe']
    li=['h','l','b']
    for dd in li:
        DATA[dd]={}
        for d in range(len(list_)):
            DATA[dd][x[d]]=list_[d][dd]
    print(DATA.keys())
    print(DATA['h'].keys())
    print(DATA['l'].keys())
    print(DATA['b'].keys())
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    h = np.array([sum(DATA['h'][i])/len(DATA['h'][i]) for i in x]) # Effectively y = x**2
    eh = np.array([np.std(DATA['h'][i]) for i in x])

    l = np.array([sum(DATA['l'][i])/len(DATA['l'][i]) for i in x]) # Effectively y = x**2
    el = np.array([np.std(DATA['l'][i]) for i in x])

    b = np.array([sum(DATA['b'][i])/len(DATA['b'][i]) for i in x]) # Effectively y = x**2
    eb = np.array([np.std(DATA['b'][i]) for i in x])

#    dip = np.array([sum(DATA['dipole'][i])/len(DATA['dipole'][i]) for i in range(3)]) # Effectively y = x**2
#    edip = np.array([np.std(DATA['dipole'][i]) for i in range(3)])

    ax1.errorbar(x, h, eh, linestyle='None', marker='^', color='blue', label='HOMO')
    ax1.errorbar(x, l, el, linestyle='None', marker='o',color='red',label='LUMO')
    ax1.errorbar(x, b, eb, linestyle='None', marker='x',color='green',label='Band gap')
#    ax1.errorbar(x, dip, edip, linestyle='None', marker='x',color='grey')
    ax1.set_ylabel('Energy values [eV]')
    ax1.set_xlabel('Different simulation systems')
    #plt.legend(loc='upper');
    plt.grid(axis='y',linestyle='.')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()

def scatter_angle_energy(cutoff,traj,data):
    traj_angle=[]
    lumo_diff=[]
    homo_diff=[]
    bandgap_diff=[]
    for i in range(len(traj)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i][qm1][qm2][0]<cutoff:
                        traj_angle.append(traj[i][qm1][qm2][1])
                        homo_diff.append(abs(abs(data['h'][qm1][i])-abs(data['h'][qm2][i])))
                        lumo_diff.append(abs(abs(data['l'][qm1][i])-abs(data['l'][qm2][i])))
                        bandgap_diff.append(abs(abs(data['b'][qm1][i])-abs(data['b'][qm2][i])))

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(traj_angle,lumo_diff, color='blue',label='LUMO', alpha=0.6)
    ax1.scatter(traj_angle,homo_diff, color='red',label='HOMO',alpha=0.6)
    ax1.scatter(traj_angle,bandgap_diff, color='grey',label='Band gap',alpha=0.6)
    ax1.set_ylabel('Energy values [kJ/mol]')
    ax1.set_xlabel('Angle [rad] (distance cutoff = '+str(cutoff)+' A)')
    plt.legend(loc='upper fight');
    plt.show()

def RMSD(inp):
    return_array=[]
    with open(inp+'.dat','r') as traj:
        for i in traj:
            frame=white_space_remover(i).split(' ')
            return_array.append(float(frame[1]))
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(return_array)
    ax1.set_ylabel('RMSD')
    ax1.set_xlabel('Time step [0.5 fs]')
    plt.show()




#h=[]
#l=[]
#b=[]
#for i in range(3):
#     ha=sum(DATA1p['h'][i])/len(DATA1p['h'][i])
#     la=sum(DATA1p['l'][i])/len(DATA1p['l'][i])
#     ba=sum(DATA1p['b'][i])/len(DATA1p['b'][i])
     #dipa=sum(DATA1p['dipole'][i])/len(DATA1p['dipole'][i])
#    print(i,'\t',ha,'\t',la,'\t',ba,'\t')
