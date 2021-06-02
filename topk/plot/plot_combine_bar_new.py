import csv
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

## Parameters
p = '1.1'
p2 = '2'
num_exp = 1

result_daiet_A1 = {}
result_daiet_A2 = {}
result_daiet_A3 = {}
result_topk_1core_A1 = {}
result_topk_1core_A2 = {}
result_topk_1core_A3 = {}
result_topk_2core_A1 = {}
result_topk_2core_A2 = {}
result_topk_2core_A3 = {}
output_daiet = []
output_topk_1core = []
output_topk_2core = []

xtick_l = []
xtick_r = []
xtick_str = ['S-DAIET','S-RAINA','RA-RAINA' ]
k = -1

for entry in [4000]: #,5000]: # FIXME : modify just this line
    k = k + 1

    result_daiet_A1[ str(entry) ] = []
    result_daiet_A2[ str(entry) ] = []
    result_daiet_A3[ str(entry) ] = []
    result_topk_1core_A1[ str(entry) ] = []
    result_topk_1core_A2[ str(entry) ] = []
    result_topk_1core_A3[ str(entry) ] = []
    result_topk_2core_A1[ str(entry) ] = []
    result_topk_2core_A2[ str(entry) ] = []
    result_topk_2core_A3[ str(entry) ] = []    

    for i in range (1,num_exp+1):
        dist = 'z'
        t = 'topk_2core'
        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A1-{}-{}-4444-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        a = float(opened_file[-1].split(',')[1])
        b = float(opened_file[-1].split(',')[3]) /10
        result_topk_2core_A1[str(entry)].append(float(a))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A2-{}-{}-17778-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        c = float(opened_file[-1].split(',')[1]) + float(a)
        d = float(opened_file[-1].split(',')[3]) /10 + float(b)
        result_topk_2core_A2[str(entry)].append(float(c))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_2core_A3-{}-{}-31111-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        e = float(opened_file[-1].split(',')[1]) + float(c)
        f = float(opened_file[-1].split(',')[3]) /10 + float(d)
        result_topk_2core_A3[str(entry)].append(1-float(e)/float(f))

    for i in range (1,num_exp+1):
        dist = 'z'
        t = 'topk_1core'
        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_1core_A1-{}-{}-4444-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        a = float(opened_file[-1].split(',')[1])
        b = float(opened_file[-1].split(',')[3]) /10
        result_topk_1core_A1[str(entry)].append(float(a))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_1core_A2-{}-{}-17778-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        c = float(opened_file[-1].split(',')[1]) + float(a)
        d = float(opened_file[-1].split(',')[3]) /10 + float(b)
        result_topk_1core_A2[str(entry)].append(float(c))

        f = open('/home/mnc/p4-dev/topk/logs/mininet/topk/topk-fat_tree_vareg_1core_A3-{}-{}-31111-{}-{}.csv'.format(dist,p,entry,i), 'r') #daiet-fat_tree-z-1.1-1000-5000-1
        opened_file = f.readlines()
        e = float(opened_file[-1].split(',')[1]) + float(c)
        f = float(opened_file[-1].split(',')[3]) /10 + float(d)
        result_topk_1core_A3[str(entry)].append(1-float(e)/float(f))


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
    output_topk_1core.append(result_topk_1core_A3[str(entry)])
    output_topk_2core.append(result_topk_2core_A3[str(entry)])
    
    xtick_l.append(k)
    print(xtick_l)
    xtick_r.append(str(entry))
    print(xtick_str)

out_daiet = []
out_topk_1core = []
out_topk_2core = []
total_result = []
plt.rcParams['figure.figsize'] = [7.5, 6.5]
plt.figure()
x = np.arange(len(xtick_str))
print(x)

for i in range (0,1):
    out_daiet += output_daiet[i]
    out_topk_1core += output_topk_1core[i]
    out_topk_2core += output_topk_2core[i]

total_result += out_daiet
total_result += out_topk_1core
total_result += out_topk_2core
print(out_daiet)
print(out_topk_1core)
print(out_topk_2core)
print(total_result)

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=BIGGER_SIZE) # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE) # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE+4) # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE) # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE) # fontsize of the tick labels
plt.rc('legend', fontsize=18) # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

colors = ['tab:blue','tab:gray','antiquewhite']
hatches = ['//', '-', '////']
bar = plt.bar(x, total_result, color=colors, edgecolor='black', width=0.55)
bar[0].set_hatch('//')
bar[1].set_hatch('-')
bar[2].set_hatch('////')
plt.xlim(-0.5,2.5)

plt.xticks(x , xtick_str)
plt.ylabel('Reduction ratio')
plt.xlabel('Type of tree')
plt.savefig('graph-fat_tree_final_bar_tri_20000_news.png')