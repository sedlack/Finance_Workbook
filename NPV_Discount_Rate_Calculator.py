# -*- coding: utf-8 -*-
"""
WACC - Discount Rate Calculator

Inputs: 
    Current debt to vlaue ratio
    Unlevered Beta
    Tax Rate
    Risk Free Rate
    Market Risk Premium
    
Output: Company Specific WACC (Discount Rate)
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def wacc_calc(current_debt_to_value, unlevered_beta, 
              tax_rate, rf_rate, market_premium):
    
    debt_to_value = []
    debt_to_equity = []

    for i in range(0,100,1):
        d_v = i / 100
        debt_to_value.append(d_v)
    
        d_e = 1 / (1 - d_v) - 1
        debt_to_equity.append(d_e)
        
    wacc_df = pd.DataFrame({'debt_to_value': debt_to_value, 
                            'debt_to_equity': debt_to_equity})
    
    wacc_df['leveraged_beta'] = unlevered_beta * (1 + (1 - tax_rate) 
                                                  * wacc_df['debt_to_equity'])
    
    wacc_df['cost_of_equity'] = (rf_rate + wacc_df['leveraged_beta'] 
                                 * market_premium)
    
    
    # Update this formula with if statements
    c_d = []

    for i in range(0,100,1):
        d_v = i / 100
    
        if d_v <= 0.10:
            c_d.append(.052)
        
        elif d_v <= 0.20:
            c_d.append(.0625)
    
        elif d_v <= 0.30:
            c_d.append(.0650)
            
        elif d_v <= 0.40:
            c_d.append(.0825)
            
        elif d_v <= 0.50:
            c_d.append(.10)
    
        elif d_v <= 0.60:
            c_d.append(.10)
            
        else:
            c_d.append(.125)
    
    
    wacc_df['cost_of_debt'] = c_d
    
    wacc_df['wacc'] = ((1 - wacc_df['debt_to_value']) * wacc_df['cost_of_equity'] + 
                   (1 - tax_rate) * wacc_df['cost_of_debt'] * wacc_df['debt_to_value'])
    

    current_wacc = wacc_df[wacc_df['debt_to_value'] == current_debt_to_value].reset_index()
    wacc = current_wacc['wacc'][0]
    return(wacc)
 
