# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:29:34 2021

@author: SSD M2
"""
import simpy 
def reloj(env, nombre, tiempo):
    while True:
        print(nombre,env.now)
        yield env.timeout(tiempo)

env= simpy.Environment()
env.process(reloj(env, 'fast', 0.5))
env.process(reloj(env, 'slow', 2))
env.run(until=11)
