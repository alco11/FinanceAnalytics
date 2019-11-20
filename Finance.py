import math
import numpy as np
import pandas as pd
import time
from itertools import combinations

def RealInterestRate(NominalRate,Inflation):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    #Turns percentage into decimal
    NominalRate = NominalRate/100
    Inflation = Inflation/100
    
    #Gets formula ready where R = Nominal Interest and i = Inflation
    R = 1 + NominalRate
    i = 1 + Inflation
    
    #Performs Calculation where r = Real Interest
    r = R/i
    r = r - 1
    
    #Turns decimal to percentage
    r = r*100
    
    #Returns percentage and rounds to 3 decimal places
    return round(r,3)

def NominalInterestRate(RealRate,Inflation):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    #Turns percentage into decimal
    RealRate = RealRate/100
    Inflation = Inflation/100
    
    #Gets formula ready where r = Real Interest and i = Inflation
    r = 1 + RealRate
    i = 1 + Inflation
    
    #Performs calculation
    R = r * i
    R = R-1
    
    #Turns into percentage
    R = R * 100
    
    #Returns total round to 3 decimal places
    return round(R,3)

def HoldingPeriodReturn(SalePrice,BuyPrice,Dividend):
    '''
    arg: Takes in float for all arguements ex: 3.14
    returns: float
    '''
    HPR = (SalePrice - BuyPrice) + Dividend
    
    HPR =  HPR/BuyPrice
    
    HPR = HPR*100
    
    return HPR
    
def CapitalGains(SalePrice,BuyPrice):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    CG = (SalePrice - BuyPrice)/(BuyPrice)
    
    CG = CG * 100
    
    return CG

def DividendYield(BuyPrice,Dividend):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    DY = Dividend/BuyPrice
    DY = DY * 100
    return DY

def EAR(APR,Periods):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    EAR = 1+((APR/100)/Periods)
    EAR = EAR**Periods
    EAR = EAR - 1
    
    EAR = EAR * 100
    return round(EAR,3)

def APR(EAR,Periods):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    APR = ((EAR/100)+1)**(1/Periods)
    APR = APR-1
    APR = APR * Periods
    
    APR = APR * 100
    return round(APR,3)

def EARContinousCompounding(APR):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    EAR = math.exp(APR/100)-1
    EAR = EAR*100
    return round(EAR,3)

def APRContinousCompounding(EAR):
    '''
    arg: Takes in float for both arguements ex: 3.14
    returns: float
    '''
    APR = math.log((EAR/100)+1)
    APR = APR * 100
    return round(APR,3)

def PortfolioExpectedReturns(Weights,Returns):
    '''
    args: Takes in list for all arguements
    returns: float
    '''
    
    if len(Weights) != len(Returns):
        raise ValueError('Lists do not equal in length. Make sure both lists are the same length')
    
    for i in Weights:
        if i > 1:
            raise TypeError('Make sure all objects in list are in decimal form')

    for i in Returns:
        if i > 1:
            raise TypeError('Make sure all objects in list are in decimal form')
    
    WeightedReturns = []
    for i in range(len(Weights)):
        WR = Weights[i]*Returns[i]
        WeightedReturns.append(WR)
    
    WeightedReturns = np.sum(WeightedReturns)
    
    WeightedReturns = WeightedReturns*100
    
    return round(WeightedReturns,3)


def NPV(CashFlows,DiscountRate):
    '''
    args: CashFlows = List of free cashflows
          DiscountRate = float
    returns:
        float
        '''
    DR = DiscountRate/100
    
    PV = []
    for i in range(len(CashFlows)):
        Power = 1/(1+DR)**(i+1)
        PVC = CashFlows[i]*Power
        print(PVC)
        PV.append(PVC)
    
    TotalPresentValue = np.sum(PV)
    
    return round(TotalPresentValue,2)
