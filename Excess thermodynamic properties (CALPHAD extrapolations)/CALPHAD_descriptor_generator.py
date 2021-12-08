# -*- coding: utf-8 -*-
"""
Created on 21-11-26

@author: Guillaume.Deffrennes
"""
##################################################################################################
# Packages
import pandas as pd

##################################################################################################
# Input
Data = pd.read_csv('Example_Input.csv',skiprows=[1])
Comments = pd.read_csv('Example_Input.csv',nrows=1)
Interaction_para = pd.read_csv('Binary_interaction_parameters.csv', index_col=0, skiprows=[1])
##################################################################################################
# Calculation of the excess thermodynamic properties at each composition point
Ex_H_in_LIQ_extrapolated_from_binaries = ['J/mol']
Ex_S_in_LIQ_extrapolated_from_binaries = ['J/mol/K']
Ex_G_in_LIQ_extrapolated_from_binaries = ['J/mol']

for i in range(len(Data)):
    #Summation of the excess thermodynamic properties across all binaries (Muggianu extrapolation)
    exH_LIQ = 0
    exS_LIQ = 0
    for A in range(1,len(Data.columns)):
        for B in range(A+1,len(Data.columns)):
            T  = Data.iloc[i,0]
            xA = Data.iloc[i,A]/100
            xB = Data.iloc[i,B]/100
            AB_system = Data.columns[A]+Data.columns[B]
            exH_LIQ = exH_LIQ+xA*xB*(Interaction_para.loc['a0',AB_system]+\
                                     Interaction_para.loc['a1',AB_system]*(xA-xB)+\
                                     Interaction_para.loc['a2',AB_system]*(xA-xB)**2+\
                                     Interaction_para.loc['a3',AB_system]*(xA-xB)**3+\
                                     Interaction_para.loc['a4',AB_system]*(xA-xB)**4)   
            exS_LIQ = exS_LIQ-xA*xB*(Interaction_para.loc['b0',AB_system]+\
                                     Interaction_para.loc['b1',AB_system]*(xA-xB)+\
                                     Interaction_para.loc['b2',AB_system]*(xA-xB)**2+\
                                     Interaction_para.loc['b3',AB_system]*(xA-xB)**3+\
                                     Interaction_para.loc['b4',AB_system]*(xA-xB)**4)
            exG_LIQ = exH_LIQ-T*exS_LIQ                 
    Ex_H_in_LIQ_extrapolated_from_binaries.extend([round(exH_LIQ,0)])
    Ex_S_in_LIQ_extrapolated_from_binaries.extend([round(exS_LIQ,3)])
    Ex_G_in_LIQ_extrapolated_from_binaries.extend([round(exG_LIQ,0)]) 

##################################################################################################
# Output
Data = Comments.append(Data)
Data['Ex_H_in_LIQ_extrapolated_from_binaries'] = Ex_H_in_LIQ_extrapolated_from_binaries
Data['Ex_S_in_LIQ_extrapolated_from_binaries'] = Ex_S_in_LIQ_extrapolated_from_binaries
Data['Ex_G_in_LIQ_extrapolated_from_binaries'] = Ex_G_in_LIQ_extrapolated_from_binaries

Data.to_csv('Example_Output.csv', index = False)
