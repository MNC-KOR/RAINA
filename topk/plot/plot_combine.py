import csv
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

## Parameters
p = '1.1'
p2 = '2'
num_exp = 1

result_daiet_A1 = {}
result_daiet_A2 = {}
result_daiet_A3 = {}
result_topk_A1 = {}
result_topk_A2 = {}
result_topk_A3 = {}
output_daiet = []
output_topk = []

xtick_l = []
xtick_r = []
k = -1

for entry in [1000,2000,3000,4000,5000,6000,7000,8000]: #,5000]: # FIXME : modify just this line
    k = k + 1

    result_daiet_A1[ str(entry) ] = []
    result_daiet_A2[ str(entry) ] = []
    result_daiet_A3[ str(entry) ] = []
    result_topk_A1[ str(entry) ] = []
    result_topk_A2[ str(entry) ] = []
    result_topk_A3[ str(entry) ] = []

    for i in range (1,num_exp+1):
        dist = 'z'
        t = 'topk'
        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A1-{}-{}-4444-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        a = float(opened_file[-1].split(',')[1])
        b = float(opened_file[-1].split(',')[3]) /10
        result_topk_A1[str(entry)].append(float(a))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A2-{}-{}-17778-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        c = float(opened_file[-1].split(',')[1]) + float(a)
        d = float(opened_file[-1].split(',')[3]) /10 + float(b)
        result_topk_A2[str(entry)].append(float(c))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A3-{}-{}-31111-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        e = float(opened_file[-1].split(',')[1]) + float(c)
        f = float(opened_file[-1].split(',')[3]) /10 + float(d)
        result_topk_A3[str(entry)].append(1-float(e)/float(f))


    for i in range (1,num_exp+1):
        dist = 'z'
        t = 'daiet'
        f = open('/home/mnc/p4-dev/topk/logs/mininet/daiet/daiet-fat_tree_stat_1core_A1-{}-{}-4444-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        a = float(opened_file[-1].split(',')[1])
        b = float(opened_file[-1].split(',')[3]) /10
        result_daiet_A1[str(entry)].append(float(a))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/daiet/daiet-fat_tree_stat_1core_A2-{}-{}-17778-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        c = float(opened_file[-1].split(',')[1]) + float(a)
        d = float(opened_file[-1].split(',')[3]) /10 + float(b)
        result_daiet_A2[str(entry)].append(float(c))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/daiet/daiet-fat_tree_stat_1core_A3-{}-{}-31111-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        e = float(opened_file[-1].split(',')[1]) + float(c)
        f = float(opened_file[-1].split(',')[3]) /10 + float(d)
        result_daiet_A3[str(entry)].append(1-float(e)/float(f))



    output_daiet.append(result_daiet_A3[str(entry)])
    output_topk.append(result_topk_A3[str(entry)])
    
    xtick_l.append(k)
    print(xtick_l)
    xtick_r.append(str(entry))
    print(xtick_r)

print(output_daiet)
print(output_topk)

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=BIGGER_SIZE) # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE) # fontsize of the axes title
plt.rc('axes', labelsize=20) # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE) # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE) # fontsize of the tick labels
plt.rc('legend', fontsize=18) # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

plt.rcParams['figure.figsize'] = [12, 7.5]

plt.plot( output_daiet, label='DAIET', marker="^", markersize=13)
plt.plot( output_topk, label='RAINA', marker="D", markersize=10)


plt.legend()

plt.ylabel('Reduction ratio')
plt.xlabel('The number of entry types (fat-tree)')
plt.xticks( xtick_l , xtick_r )
plt.yticks(np.arange(0,1.05,0.1))
plt.savefig('graph-fat_tree_final_vareg_comp.png')