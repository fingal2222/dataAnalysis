# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:32:54 2018

@author: zhaof
"""

import numpy as np
import pandas as pd


class data_clean(object):
    def __init__(self):
        pass
    
    def get_data(self):
        data=pd.read_csv("machine_learning.csv",encoding="gbk")
        return data
    
    def clean_operation(self):
        data=self.get_data()
        data['address']=data['address'].fillna(value='未知')
        for i,j in enumerate(data['address']):
            j=j.replace('[','').replace(']','')
            data['address'][i]=j
        
        for i,j in enumerate(data['industrylabels']):
            j=j.replace('[','').replace(']','')
            data['industrylabels'][i]=j
            
        for i,j in enumerate(data['label']):
            j=j.replace('[','').replace(']','')
            data['label'][i]=j
            
        data['position_detail']=data['position_detail'].fillna('未知')
        for i,j in enumerate(data['position_detail']):
            j=j.replace('\r','').replace('\n','')
            data['position_detail'][i]=j
        
        #处理薪资
        for i,j in enumerate(data['salary']):
            j=j.replace('k','').replace('K','').replace('以上','-0')
            j1=int(j.split('-')[0])
            j2=int(j.split('-')[1])
            j3=1/2*(j1+j2)
            data['salary'][i]=j3*1000
        
        print(data['size'].value_counts())
        
        for i,j in enumerate(data['position_name']):
            if '数据分析' in j:
                j='数据分析工程师'
            if '数据挖掘' in j:
                j='数据挖掘工程师'
            if '机器学习' in j:
                j='机器学习工程师'
            if '深度学习' in j:
                j='深度学习工程师'
            data['position_name'][i]=j
        return data
        
        

opt=data_clean()
data=opt.clean_operation()
data.to_csv("lagou_clean.csv")


    
        
        
    
        
    
        
        