# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:11:43 2022

@author: wllcc
"""

import wntr 
import numpy as np
import networkx as nx
import wntr.network.controls as controls

wn = wntr.network.WaterNetworkModel('ZJNetwork.inp') 
wn.options.hydraulic.demand_model = 'DD'



#sim = wntr.sim.WNTRSimulator(wn)
#results = sim.run_sim()

#pressure = results.node['pressure']
#pressure_at_1hr = pressure.loc[3600,:]
#demand=results.node['demand']
#head = results.node['head']
#flowrate=results.link['flowrate']



#expected_demand = wntr.metrics.expected_demand(wn)
#wsa = wntr.metrics.water_service_availability(expected_demand, demand)
#print(wsa)

#graph= wntr.graphics.plot_network(wn, node_attribute=pressure_at_1hr, node_size=20, link_width=1, node_colorbar_label='Pressure (m)',title='Pressure at 1 HR')

epicenter = (300,300) # x,y location
magnitude = 5.3 # Richter scale
depth = 10000 # m, shallow depth
earthquake = wntr.scenario.Earthquake(epicenter, magnitude, depth)
distance = earthquake.distance_to_epicenter(wn, element_type=wntr.network.Pipe)
pga = earthquake.pga_attenuation_model(distance)
pgv = earthquake.pgv_attenuation_model(distance)
repair_rate = earthquake.repair_rate_model(pgv)

#pgv.to_excel('ZJpgv.xlsx')

ax = wntr.graphics.plot_network(wn, link_attribute=pgv, node_size=4, link_width=2, link_colorbar_label='PGV')

ax = wntr.graphics.plot_network(wn, link_attribute=pga, node_size=4, link_width=2, link_colorbar_label='PGA')

#pga.to_excel('ZJpga.xlsx')