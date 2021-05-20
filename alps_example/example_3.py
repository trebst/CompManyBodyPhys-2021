# for alps transverse field:
# z coupling, x field (gamma)
# import pyalps
# import numpy as np


import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

Ls = [8]
hs = np.linspace(0.0, 2, 21)
parms = []
for h in hs:
    for L in Ls:
        parms.append(
            {
                  'LATTICE'        : "chain lattice", 
                  'MODEL'          : "spin",
                  'local_S'        : 0.5,
                  'L'              : L,
                  'Jxy'            : 0,
                  'Jz'             : -1,
                  'Gamma'          : h,
                  'BETA'           : 100.0,
                  'THERMALIZATION' : 10000,
                  'SWEEPS'         : 10000,
                  'ALGORITHM'      : 'loop'
            }
        )
input_file = pyalps.writeInputFiles('1D-SSE-TRANSVERSE-ISING', parms)
res = pyalps.runApplication('loop', input_file, Tmin=1)


# data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='1D-SSE-TRANSVERSE-ISING'),'|Magnetization|')
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='1D-SSE-TRANSVERSE-ISING'),'|Magnetization|')
magnetization = pyalps.collectXY(data,x='Gamma',y='|Magnetization|',foreach=['L'])

magnetization[0].y /= (L/2)

plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('Magnetic Field h')
plt.ylabel('|Magentization|')
plt.legend()
plt.show()