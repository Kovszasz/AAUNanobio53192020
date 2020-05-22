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


def HeatMap(data,length):
    pass


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

def error_angleQMregions(data,start,end,length):
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

def error_experiments(list_,xlabel='Energy values [eV]',li=['h','l','b']):#list containing p,pe,p6,p6e
    DATA={}
    x = ['1p', '1pe', '6p','6pe']
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
    if 'h' in li:
        h = np.array([sum(DATA['h'][i])/len(DATA['h'][i]) for i in x]) # Effectively y = x**2
        eh = np.array([np.std(DATA['h'][i]) for i in x])
        ax1.errorbar(x, h, eh, linestyle='None', marker='^', color='blue', label='HOMO')
    elif 'l' in li:
        l = np.array([sum(DATA['l'][i])/len(DATA['l'][i]) for i in x]) # Effectively y = x**2
        el = np.array([np.std(DATA['l'][i]) for i in x])
        ax1.errorbar(x, l, el, linestyle='None', marker='o',color='red',label='LUMO')
    elif 'b' in li:
        b = np.array([sum(DATA['b'][i])/len(DATA['b'][i]) for i in x]) # Effectively y = x**2
        eb = np.array([np.std(DATA['b'][i]) for i in x])
        ax1.errorbar(x, b, eb, linestyle='None', marker='x',color='green',label='Band gap')
    elif 'dipol' in li:
        dip = np.array([sum(DATA['dipole'][i])/len(DATA['dipole'][i]) for i in x]) # Effectively y = x**2
        edip = np.array([np.std(DATA['dipole'][i]) for i in x])
        ax1.errorbar(x, b, eb, linestyle='None', marker='o',color='blue')
#    dip = np.array([sum(DATA['dipole'][i])/len(DATA['dipole'][i]) for i in range(3)]) # Effectively y = x**2
#    edip = np.array([np.std(DATA['dipole'][i]) for i in range(3)])

def error_experimentsDipole(list_,xlabel='Dipole [Debye]'):#list containing p,pe,p6,p6e
    DATA={}
    x = ['','1p','', '1pe','', '6p','','6pe']
    for d in range(len(list_)):
        DATA[x[d]]=list_[d]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    print(np.mean(list_[0]),'\t',np.mean(list_[1]),'\t',np.mean(list_[2]),'\t',np.mean(list_[3]))
    r=ax1.violinplot(list_, [1,2,3,4], points=20, widths=0.3,
                     showmeans=True, showextrema=True, showmedians=True)
#    dip = np.array([sum(DATA['dipole'][i])/len(DATA['dipole'][i]) for i in range(3)]) # Effectively y = x**2
#    edip = np.array([np.std(DATA['dipole'][i]) for i in range(3)])




#    ax1.errorbar(x, dip, edip, linestyle='None', marker='x',color='grey')
    ax1.set_xticklabels(x)
    ax1.set_ylabel(xlabel)
    ax1.set_xlabel('Different simulation systems')
    #plt.legend(loc='upper');
    print(r)
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

def scatter_angle_frequency(cutoff,traj,first,second,third,fourth,fifth):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    traj_angle1=[]
    traj_angle2=[]
    traj_angle3=[]
    traj_angle4=[]
    traj_angle5=[]
    for i in range(round(len(traj)*first)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i]['qm'][qm1][qm2][0]<cutoff:
                        traj_angle1.append(traj[i]['qm'][qm1][qm2][1])
    for i in range(round(len(traj)*first),round(len(traj)*second)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i]['qm'][qm1][qm2][0]<cutoff:
                        traj_angle2.append(traj[i]['qm'][qm1][qm2][1])
    for i in range(round(len(traj)*second),round(len(traj)*third)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i]['qm'][qm1][qm2][0]<cutoff:
                        traj_angle3.append(traj[i]['qm'][qm1][qm2][1])
    for i in range(round(len(traj)*third),round(len(traj)*fourth)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i]['qm'][qm1][qm2][0]<cutoff:
                        traj_angle4.append(traj[i]['qm'][qm1][qm2][1])
    for i in range(round(len(traj)*fourth),round(len(traj)*fifth)):
        for qm1 in range(18):
            for qm2 in range(18):
                if qm1!=qm2:
                    if traj[i]['qm'][qm1][qm2][0]<cutoff:
                        traj_angle5.append(traj[i]['qm'][qm1][qm2][1])
    ax1.hist([traj_angle1,traj_angle2,traj_angle3],histtype='barstacked', normed=False,bins=60, alpha=0.8,color=["green","blue","red"],label=[str((round(len(traj)*first)*0.5)/1000)+' ps',str((round(len(traj)*second)*0.5)/1000)+' ps',str((round(len(traj)*third)*0.5)/1000)+' ps'])
    #ax1.hist(traj_angle1, normed=False,bins=60, alpha=0.3,color="green",label=str((round(len(traj)*first)*0.5)/1000)+' ps')
    #ax1.hist(traj_angle2, normed=False,bins=60, alpha=0.3,color="blue",label=str((round(len(traj)*second)*0.5)/1000)+' ps')
    #ax1.hist(traj_angle3, normed=False,bins=60, alpha=0.4,color="red",label=str((round(len(traj)*third)*0.5)/1000)+' ps')


    #ax1.hist(traj_angle4, normed=True,bins=30, alpha=0.4,color="black",label=str(fourth))
    #ax1.hist(traj_angle5, normed=True,bins=30, alpha=0.4,color="purple",label=str(fifth))
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Angle [rad] (distance cutoff = '+str(cutoff)+' A)')
    plt.legend(loc='upper left');
    plt.show()


def homo_lumo_traj(DATA,modes,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATA['h'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap'}
    x=[]
    for i in range(frame_range[0],frame_range[1]):
        if i<8:
            x.append(i*500)
        else:
            x.append(i*50+(7*500))
    for i in regions:
        for j in modes:
            if i==2:
                ax1.plot(x,DATA[j][i][frame_range[0]:frame_range[1]],color=c[j],label=l[j])
            else:
                ax1.plot(x,DATA[j][i][frame_range[0]:frame_range[1]],color=c[j])
    print(max(x))
    plt.ylabel('Energy [eV]')
    plt.xlabel('Timestep [0.5 fs]')
    plt.grid(axis='y',linestyle=':')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()


def homo_lumo_traj_diff(DATAs,modes,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATAs[0]['h'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap'}
    x=[]
    for i in range(frame_range[0],frame_range[1]):
        if i<8:
            x.append(i*500)
        else:
            x.append(i*50+(7*500))
    for i in regions:
        for j in modes:
            p=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])
            pe=np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            corr=np.corrcoef(p, pe)
            print(corr)
            if i==2:
                ax1.scatter(p,pe,color=c[j],label=l[j])
            else:
                ax1.scatter(p,pe,color=c[j])
            #d=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])-np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            #diff=np.mean(d)
            #rms = d-diff
            #ax1.scatter(d, usevlines=True, normed=True, maxlags=50, lw=2)
                #ax1.plot(x,rms,color=c[j])
    print(max(x))
    ax1.grid(True)
    plt.ylabel('6p')
    plt.xlabel('6pe')
    #plt.grid(axis='y',linestyle=':')
    #plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    #plt.tight_layout()
    plt.show()

def dipole_traj_diff(DATAs,modes,xlabel,ylabel,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATAs[0]['h'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey','dipole':'green'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap','dipole':'Dipole'}
    x=[]
    for i in range(frame_range[0],frame_range[1]):
        if i<8:
            x.append(i*500)
        else:
            x.append(i*50+(7*500))
    for i in regions:
        for j in modes:
            p=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])
            pe=np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            corr=np.corrcoef(p, pe)
            print(corr)
            ax1.scatter(p,pe,label='QM'+str(i)+'(corr='+str(round(corr[0][1],4))+')', alpha=0.6)
            #d=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])-np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            #diff=np.mean(d)
            #rms = d-diff
            #ax1.scatter(d, usevlines=True, normed=True, maxlags=50, lw=2)
                #ax1.plot(x,rms,color=c[j])
    print(max(x))
    ax1.grid(True)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.grid(axis='y',linestyle=':')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()

def dipole_traj_diffNAMD(DATAs,modes,xlabel,ylabel,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATAs[0]['dipole'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey','dipole':'green'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap','dipole':'Dipole'}
    x=[i for i in range(frame_range[0],frame_range[1])]
    for i in regions:
        for j in modes:
            p=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])
            pe=np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            corr=np.corrcoef(p, pe)
            print(corr)
            if 10<i:
                ax1.scatter(p,pe,label='QM'+str(i)+'(corr='+str(round(corr[0][1],4))+')', alpha=0.6)
            else:
                ax1.scatter(p,pe,label='QM'+str(i)+'(corr='+str(round(corr[0][1],4))+')',marker='x', alpha=0.6)
            #d=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])-np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            #diff=np.mean(d)
            #rms = d-diff
            #ax1.scatter(d, usevlines=True, normed=True, maxlags=50, lw=2)
                #ax1.plot(x,rms,color=c[j])
    print(max(x))
    ax1.grid(True)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.grid(axis='y',linestyle=':')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()

data6pe={}
data6pe['dipole']={}
for j in DATAe:
    for i in range(18):
        if i in data6pe['dipole'].keys():
             data6pe['dipole'][i].append(j['dipole'][i])
        else:
            data6pe['dipole'][i]=[j['dipole'][i]]

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


def CorrelationMatrix(matrix):
    phe = ['','', '']
    layer = ['Single peptide',1,2,3,4,5,6]
    correlation = np.array(matrix)
    print(correlation)
    fig, ax = plt.subplots()
    im = ax.imshow(correlation,vmin=-100,vmax=100,cmap=cm.coolwarm)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(phe)))
    ax.set_yticks(np.arange(len(layer)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(phe)
    ax.set_yticklabels(layer)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(layer)):
        for j in range(len(phe)):
            text = ax.text(j, i, (str(correlation[i, j])+'%'),
                       ha="center", va="center", color="w")
    fig.tight_layout()
    plt.colorbar(im)
    plt.show()


def DipoleCorrelationMatrix(DATAs,modes,xlabel,ylabel,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATAs[0]['dipole'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey','dipole':'green'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap','dipole':'Dipole'}
    x=[i for i in range(frame_range[0],frame_range[1])]
    rev=False
    corrm=[[-0.0221,-0.0396,-0.0528]]
    ci=[]
    for i in regions:
        for j in modes:
            p=np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]])
            pe=np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]])
            corr=np.corrcoef(p, pe)
            ci.append(round(corr[0][1],4))
        if ((i+1)%3==0):
            if rev:
                corrm.append(ci.reverse())
            else:
                corrm.append(ci)
            rev = !rev
            ci=[]

    CorrelationMatrix(corrm)


def DipoleAverageDifferencenMatrix(DATAs,modes,xlabel,ylabel,regions=[],frame_range=[]):
    if len(frame_range)==0:
        frame_range=[0,len(DATAs[0]['dipole'][0])]
    if len(regions)==0:
        regions=[i for i in range(0,18)]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    c={'h':'red','l':'blue','b':'grey','dipole':'green'}
    l={'h':'HOMO','l':'LUMO','b':'Band gap','dipole':'Dipole'}
    x=[i for i in range(frame_range[0],frame_range[1])]
    rev=False
    corrm=[[4.9,-2.1,-20.32]]
    ci=[]
    for i in regions:
        for j in modes:
            p=np.average(np.array(DATAs[0][j][i][frame_range[0]:frame_range[1]]))
            pe=np.average(np.array(DATAs[1][j][i][frame_range[0]:frame_range[1]]))
            ci.append(round((1-(pe/p))*100,2))
        if ((i+1)%3==0):
            if rev:
                corrm.append(ci.reverse())
            else:
                corrm.append(ci)
            rev = !rev
            ci=[]
    CorrelationMatrix(corrm)




meanDipole=[0.1299,0.1272,0.1175,0.1199]

for i in pairinecies:
    for j in DATA6:
        pairs[str(i[0]+1)+'-'+str(i[1]+1)]['d'].append(j['qm'][i[0]][i[1]][0])
        pairs[str(i[0]+1)+'-'+str(i[1]+1)]['a'].append(j['qm'][i[0]][i[1]][1])


pairs={}
for i in ['1-6','6-7','2-5','5-8','3-4','4-9','10-15','15-16','11-14','14-17','12-13','13-18']:
    pairs[i]={'d':[],'a':[]}

pairinecies=[[0,5],[5,6],[1,4],[4,7],[2,3],[3,8],[9,14],[14,15],[10,13],[13,16],[11,12],[12,17]]

for i in pairs.keys():
    if int(i.split('-')[0])<9:
        ax1.plot(pairs[i]['a'],label=i)
    else:
        ax1.plot(pairs[i]['a'],label=i,linestyle='dashed')
#h=[]
#l=[]
#b=[]
#for i in range(3):
#     ha=sum(DATA1p['h'][i])/len(DATA1p['h'][i])
#     la=sum(DATA1p['l'][i])/len(DATA1p['l'][i])
#     ba=sum(DATA1p['b'][i])/len(DATA1p['b'][i])
     #dipa=sum(DATA1p['dipole'][i])/len(DATA1p['dipole'][i])
#    print(i,'\t',ha,'\t',la,'\t',ba,'\t')
