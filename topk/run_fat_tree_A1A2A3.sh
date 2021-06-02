#!/bin/bash
# make_dataset : --sort no (2)
# send_py : --dist (--parameter) (--fat_tree) (--host_number) --entry 
# receive.py : --save_index --type

# for i in `seq 1 5`

#트리이동, 유동레지스터
python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A1.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A1.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A1.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A1_vareg_2core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A2.py && sleep 2
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A2.py && sleep 2
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A2.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2
bash /home/mnc/p4-dev/topk/run_fat_tree_A2_vareg_2core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A3.py && sleep 2
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A3.py && sleep 2
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A3.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_vareg_2core.sh && sleep 3

#트리이동, 고정레지스터
python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A1.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A1.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A1_stat_2core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A2.py && sleep 2
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A2.py && sleep 2
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A2_stat_2core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A3.py && sleep 2
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A3.py && sleep 2
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_stat_2core.sh && sleep 3

#트리이동X, 유동레지스터
python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A1_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A1_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A1.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A1_vareg_1core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A2_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A2_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A2.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A2_vareg_1core.sh && sleep 3\

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A3_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A3_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A3.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_vareg_1core.sh && sleep 3

#트리이동X, 고정레지스터
python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A1_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A1_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_stat_1core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A2_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A2_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_stat_1core.sh && sleep 3

python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A3_stat.py && sleep 2 
python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A3_stat.py && sleep 2 
sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_stat.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2 
bash /home/mnc/p4-dev/topk/run_fat_tree_A3_stat_1core.sh && sleep 3

# python /home/mnc/p4-dev/topk/rule/generate_rules_topk_A3_stat.py && sleep 2
# python /home/mnc/p4-dev/topk/daiet/rule/generate_rules_A3_stat.py && sleep 2
# sudo cp -f /home/mnc/p4-dev/topk/topology/topo_topk_hw_A3.py /home/mnc/p4-dev/topk/topology/topo_topk_hw.py && sleep 2
# bash /home/mnc/p4-dev/topk/run_fat_tree_A3.sh && sleep 3





#sudo simple_switch -i 0@veth0 -i 1@veth2 -i 2@veth4 -i 3@veth6 --thrift-port 9090 --log-console /home/mnc/p4-dev/topk/topk_for_daiet.json
#simple_switch_CLI --thrift-port 9090 < /home/mnc/p4-dev/topk/rule/topk_rule
#sudo python /home/mnc/p4-dev/topk/packets/receive.py --i veth4 --s 0 --type topk
##python /home/mnc/p4-dev/topk/packets/dataset/make_dataset_hw.py --dist 'z' --parameter 1.1
#sudo python /home/mnc/p4-dev/topk/packets/send.py --i veth0 --di '10.0.0.16' --num 1000 --dif '10.0.1.1' --num_flush 1 --dist z --entry 3000 --parameter 1.1 --sort 3
