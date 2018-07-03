import pandas as pds
import matplotlib

matplotlib.use('MacOSX')
from matplotlib import pyplot

with open('grades.txt', 'r') as f:
    l = f.readlines()
    k = []
    for i in l:
        k.append(int(i.rstrip()[-1]))

grades = pds.DataFrame(k)
