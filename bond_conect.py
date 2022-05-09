import matplotlib.pyplot as plt
import numpy as np
data=open("bond_conection1.dat","r")
bond_conect=[]
bond_num=[]
x=data.readlines()
n=len(x)
for i in range(1,n,1):
	if x[i].startswith("cycle"):
		pass
	else:
		bond_conect.append(eval(x[i]))
for j in range(n//2):	
	bond_num.append(len(bond_conect[j]))


np.savetxt("bond_num.dat",np.array(bond_num))
plt.plot(np.array(bond_num))
plt.savefig("bond_num.png",dpi=300)
