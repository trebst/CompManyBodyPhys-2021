import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

Ls = [4,8]
Ts = np.arange(1.0, 4.0, 0.1)

parms = []
for L in Ls:
    for T in Ts:
        parms.append(
            {
                'LATTICE'        : "honeycomb lattice",
                'T'              : T,
                'J'              : 1 ,
                'THERMALIZATION' : 10000,
                'SWEEPS'         : 50000,
                'UPDATE'         : "local",
                'MODEL'          : "Ising",
                'L'              : L
            }
        )

input_file = pyalps.writeInputFiles('parm1a',parms)   
pyalps.runApplication('spinmc',input_file,Tmin=1,writexml=True)

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm1a'),'Energy Density')
magnetization = pyalps.collectXY(data,x='T',y='Energy Density',foreach=['L'])

plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('Temperature $T/J$')
plt.ylabel('Energy $E$')
plt.xlim(1,4)
plt.legend()
plt.show()