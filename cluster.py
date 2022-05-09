import matplotlib.pyplot as plt
import numpy as np

data=open("react_si.dat","r")
bond_conect=[]
bond_num=[]
x=data.readlines()
n=len(x)
for i in range(1,n,1):
	#print("bond:",i)
	if x[i].startswith("cycle"):
		pass
	else:
		bond_conect.append(eval(x[i]))

def conect(listin):
	x,y=listin[0]
	#print(x,y)
	listout=[]
	index=[]
	listout.extend(listin[0])
	for i in range(1,len(listin)):
		if (listin[i][0] in listout) or (listin[i][1] in listout):
			index.append(i)
			listout.extend(listin[i])
			listin.pop(i)
	#print (list(set(listout)), index)
	return list(set(listout)), index

CLUSTER=[]
total=1001

for i in range(len(bond_conect)):
	print("Processing step NO.:",i)

	BKN_BOND_LIST = bond_conect[i]
	cluster = []
	cluster_num=[]
	break1 = False 
	    
	while BKN_BOND_LIST:
	    pair1 = BKN_BOND_LIST.pop(0)
	    for atomid in pair1:
	        for i,pair2 in enumerate(BKN_BOND_LIST):
	            if atomid in pair2:
	                pair1.extend(pair2)
	                BKN_BOND_LIST.pop(i)
	                if not BKN_BOND_LIST:
	                    break1 = True
	                break
	        if break1:
	            break
	    cluster.append(pair1)      

	for i in range(len(cluster)):
	    cluster[i]=list(set(cluster[i]))  
	#print(cluster)

	#print(cluster)
	for k in range(len(cluster)):
		cluster_num.append(len(cluster[k]))

	#print(np.mean(np.array(cluster_num)))
	CLUSTER.append(np.mean(np.array(cluster_num)))
#plt.plot(np.arange(0,5000),CLUSTER)
np.savetxt("cluster_ave.dat",np.array(CLUSTER))
