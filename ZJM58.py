# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:36:11 2022

@author: wllcc
"""

import wntr 
import numpy as np
import networkx as nx
import wntr.network.controls as controls

wn = wntr.network.WaterNetworkModel('ZJTime2.inp') 
wn.options.hydraulic.demand_model = 'PDD'
wn.options.hydraulic.required_pressure = 21
wn.options.hydraulic.minimum_pressure  = 3.5


wn = wntr.morph.split_pipe(wn, '24', '24_B', '24_leak_node')
leak_node2 = wn.get_node('24_leak_node')
leak_node2.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '34', '34_B', '34_leak_node')
leak_node3 = wn.get_node('34_leak_node')
leak_node3.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '43', '43_B', '43_leak_node')
leak_node5 = wn.get_node('43_leak_node')
leak_node5.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '114', '114_B', '114_leak_node')
leak_node7 = wn.get_node('114_leak_node')
leak_node7.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '143', '143_B', '143_leak_node')
leak_node11 = wn.get_node('143_leak_node')
leak_node11.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '166', '166_B', '166_leak_node')
leak_node13 = wn.get_node('166_leak_node')
leak_node13.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '172', '172_B', '172_leak_node')
leak_node15 = wn.get_node('172_leak_node')
leak_node15.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '106', '106_B', '106_leak_node')
#leak_node6 = wn.get_node('106_leak_node')
#leak_node6.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '131', '131_B', '131_leak_node')
#leak_node8 = wn.get_node('131_leak_node')
#leak_node8.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '37', '37_B', '37_leak_node')
#leak_node4 = wn.get_node('37_leak_node')
#leak_node4.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '156', '156_B', '156_leak_node')
#leak_node12 = wn.get_node('156_leak_node')
#leak_node12.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '168', '168_B', '168_leak_node')
#leak_node14 = wn.get_node('168_leak_node')
#leak_node14.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '6', '6_B', '6_leak_node')
#leak_node1 = wn.get_node('6_leak_node')
#leak_node1.add_leak(wn, area=0.08, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '139', '139_B', '139_leak_node')
#leak_node9 = wn.get_node('139_leak_node')
#leak_node9.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '141', '141_B', '141_leak_node')
#leak_node10 = wn.get_node('141_leak_node')
#leak_node10.add_leak(wn, area=0.02, start_time=0, end_time=25200)



#wn = wntr.morph.split_pipe(wn, '38', '38_B', '38_leak_node')
#leak_node16 = wn.get_node('38_leak_node')
#leak_node16.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '105', '105_B', '105_leak_node')
#leak_node17 = wn.get_node('105_leak_node')
#leak_node17.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '135', '135_B', '135_leak_node')
#leak_node18 = wn.get_node('135_leak_node')
#leak_node18.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '153', '153_B', '153_leak_node')
#leak_node19 = wn.get_node('153_leak_node')
#leak_node19.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '155', '155_B', '155_leak_node')
#leak_node20 = wn.get_node('155_leak_node')
#leak_node20.add_leak(wn, area=0.02, start_time=0, end_time=25200)
#wn = wntr.morph.split_pipe(wn, '160', '160_B', '160_leak_node')
#leak_node21 = wn.get_node('160_leak_node')
#leak_node21.add_leak(wn, area=0.02, start_time=0, end_time=25200)

#wn = wntr.morph.split_pipe(wn, '59', '59_B', '59_leak_node')
#leak_node28 = wn.get_node('59_leak_node')
#leak_node28.add_leak(wn, area=0.02, start_time=0, end_time=25200)


fire_flow_demand = 0.252 # 4000 gal/min = 0.252 m3/s
fire_start = 0
fire_end = 4*3600
node = wn.get_node('18')
node.add_fire_fighting_demand(wn, fire_flow_demand, fire_start, fire_end)
fire_flow_demand1 = 0.12 
fire_start1 = 0
fire_end1 = 4*3600
node1 = wn.get_node('110')
node1.add_fire_fighting_demand(wn, fire_flow_demand1, fire_start1, fire_end1)


wn.options.time.duration = 3600
for pipe_name, pipe in wn.pipes():
   pipe.roughness = 111.37
sim = wntr.sim.WNTRSimulator(wn)
results = sim.run_sim()

demand=results.node['demand']
head = results.node['head']
pressure = results.node['pressure']
flowrate=results.link['flowrate']
threshold = 21
pump_flowrate = results.link['flowrate'].loc[:,wn.pump_name_list]
todini = wntr.metrics.todini_index(head, pressure, demand, pump_flowrate, wn,threshold)
print(todini)



expected_demand = wntr.metrics.expected_demand(wn)
wsa = wntr.metrics.water_service_availability(expected_demand, demand)
#print(wsa)

#wsa.to_excel('ZJwsa.xlsx')

#print(head)
#head.to_excel('ZJhead.xlsx')
#print(demand)
#demand.to_excel('ZJdemand.xlsx')
