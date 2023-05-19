# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:15:04 2022

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

wn = wntr.morph.split_pipe(wn, '34', '34_B', '34_leak_node')
leak_node3 = wn.get_node('34_leak_node')
leak_node3.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '114', '114_B', '114_leak_node')
leak_node7 = wn.get_node('114_leak_node')
leak_node7.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '143', '143_B', '143_leak_node')
leak_node11 = wn.get_node('143_leak_node')
leak_node11.add_leak(wn, area=0.02, start_time=0, end_time=25200)
wn = wntr.morph.split_pipe(wn, '166', '166_B', '166_leak_node')
leak_node13 = wn.get_node('166_leak_node')
leak_node13.add_leak(wn, area=0.02, start_time=0, end_time=25200)

fire_flow_demand = 0.252
fire_start = 0
fire_end = 4*3600
node = wn.get_node('9')
node.add_fire_fighting_demand(wn, fire_flow_demand, fire_start, fire_end)


wn.options.time.duration = 3600
for pipe_name, pipe in wn.pipes():
   pipe.roughness = 97.63
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
#todini.to_excel('ZJtodini.xlsx')


#expected_demand = wntr.metrics.expected_demand(wn)
#wsa = wntr.metrics.water_service_availability(expected_demand, demand)
#print(wsa)

#wsa.to_excel('ZJwsa.xlsx')