##########################
BMV2_PATH=~/behavioral-model
P4C_BM_PATH=/home/mnc/behavioral-model/p4c-bm
##########################

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

P4C_BM_SCRIPT=$P4C_BM_PATH/p4c_bm/__main__.py
SWITCH_PATH=$BMV2_PATH/targets/simple_switch/simple_switch
CLI_PATH=$BMV2_PATH/targets/simple_switch/sswitch_CLI

sudo PYTHONPATH=$PYTHONPATH:$BMV2_PATH/mininet/ python2 /home/mnc/p4-dev/topk/topology/topo_topk_hw.py \
    --behavioral-exe $BMV2_PATH/targets/simple_switch/simple_switch \
    --switch /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw.json \
    --switch0 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw0.json \
    --switch12 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw12.json \
    --switch21 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw21.json \
    --switch23 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw23.json \
    --switch32 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw32.json \
    --switch123 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw123.json \
    --switch213 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw213.json \
    --switch312 /home/mnc/p4-dev/topk/daiet/daiet_bmv2_sw312.json \
    --cli $CLI_PATH 