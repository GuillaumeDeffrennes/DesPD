# -*- coding: utf-8 -*-
"""
Created on 21-11-26

@author: Guillaume.Deffrennes
"""
##################################################################################################
# Packages and functions
import pandas as pd 

def weighted_mean(composition,property):
    return sum([a * b for a, b in zip(composition, property)])
 
def weighted_avgdev(composition,property):
    return sum([abs(b-weighted_mean(composition,property))*a for a, b in zip(composition, property)])

def get_data(Temperature,Property):
    #The 2 lines from the tabulation corresponding to the value below and above the temperature of interst are extracted
    Reduced_Database = Thermo_PURE.iloc[(Thermo_PURE['T(K)']-Temperature).abs().argsort()[:2]].reset_index(drop=bool)
    #A linear interpolation is performed to obtain the property of interest at the temperature of interest
    return (T-Reduced_Database.iloc[0,0])*(Reduced_Database.loc[1,Property]-Reduced_Database.loc[0,Property])\
    /(Reduced_Database.iloc[1,0]-Reduced_Database.iloc[0,0])+Reduced_Database.loc[0,Property]
##################################################################################################
# Input
Data = pd.read_csv('Example_Input.csv',skiprows=[1])
Comments = pd.read_csv('Example_Input.csv',nrows=1)
Thermo_PURE = pd.read_csv('Thermo_of_pure_elements.csv')

##################################################################################################
# Calculation of the mean and average deviation of the of the thermodynamic properties among elements in composition at each point
Cp_mean=['J/mol/K']
Cp_avgdev=['J/mol/K']
H_mean=['J/mol']
H_avgdev=['J/mol']
S_mean=['J/mol/K']
S_avgdev=['J/mol/K']
Hfus_mean=['J/mol']
Hfus_avgdev=['J/mol']
Sfus_mean=['J/mol/K']
Sfus_avgdev=['J/mol/K']

for i in range(len(Data)):
    T = Data.iloc[i,0]
    Composition=[]
    Cp=[]
    H=[]
    S=[]
    Hfus=[]
    Sfus=[]
    for el in range(1,len(Data.columns)):        
        Composition.extend([Data.loc[i,Data.columns[el]]/100])
        Cp.extend([get_data(T,Data.columns[el]+'_Cp')])
        H.extend([get_data(T,Data.columns[el]+'_H')])
        S.extend([get_data(T,Data.columns[el]+'_S')])
        Hfus.extend([get_data(T,Data.columns[el]+'_Hfus')])        
        Sfus.extend([get_data(T,Data.columns[el]+'_Sfus')])
    Cp_mean.extend([round(weighted_mean(Composition,Cp),3)])
    Cp_avgdev.extend([round(weighted_avgdev(Composition,Cp),4)])
    H_mean.extend([round(weighted_mean(Composition,H),0)])
    H_avgdev.extend([round(weighted_avgdev(Composition,H),4)]) 
    S_mean.extend([round(weighted_mean(Composition,S),3)])
    S_avgdev.extend([round(weighted_avgdev(Composition,S),4)]) 
    Hfus_mean.extend([round(weighted_mean(Composition,Hfus),0)])
    Hfus_avgdev.extend([round(weighted_avgdev(Composition,Hfus),4)])   
    Sfus_mean.extend([round(weighted_mean(Composition,Sfus),3)])
    Sfus_avgdev.extend([round(weighted_avgdev(Composition,Sfus),4)])    
    
##################################################################################################
# Output
Data = Comments.append(Data)
Data['Cp_mean'] = Cp_mean
Data['Cp_avgdev'] = Cp_avgdev
Data['H_mean'] = H_mean
Data['H_avgdev'] = H_avgdev
Data['S_mean'] = S_mean
Data['S_avgdev'] = S_avgdev
Data['Hfus_mean'] = Hfus_mean
Data['Hfus_avgdev'] = Hfus_avgdev
Data['Sfus_mean'] = Sfus_mean
Data['Sfus_avgdev'] = Sfus_avgdev

Data.to_csv('Example_Output.csv', index = False)