# Traffic-intersection-problem
Markov decision process applied to the traffic intersection problem

Final Project for the AI class in UC3M. 
Created by Elena de Toledo Hernández and Carlos Carmona Ramos.

Problem statement:
A traffic interfection can be approached by vehicles from the North, East and West.
The flow of vehicles in each direction encounters a traffic light before reaching the intersection, which can be either green or red. An operator must select every 20 seconds which 
of the three traffic lights will turn to green : the other two will automatically turn red.

Sensors measure the level of traffic in each direction prior to the intersection. The values can be High or Low.
When the traffic light in one direction is green, the level will normally stay the same or go down, only very occasionally increasing.

Design automaton that opens the appropiate traffic light at each cycle following the optimal policy of the corresponding MDP. The target situation is that traffic in all three
directions is Low. In such a situation, the automaton stops working.
