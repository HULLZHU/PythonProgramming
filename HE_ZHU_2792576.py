'''
1.This python file is for computing of a IRR of a project in Newton Numerical Analysis Method
2.The Purpose of This file is only for my home work to Yaccov's modeling class.
3.For convinience, assuming the cash flow returns in annual frequency, and the IRR is computed annually
4.Hello, Dr yaccov! I am He Zhu. I have asked you whether I can use Python or not. And you told me
Python is OKAY, but Java is not OK. Because I can use python but not very good at R, So I here submit my python
programming Script here. Sincerely He
'''

import math
import matplotlib.pyplot as plt

'''we first define 3 functions which will help me to get the answer'''
def getNumerator(cash_flows,x):
    numerator = 0
    for i,j in enumerate(cash_flows):
        if ( i == 0 ):
            numerator = numerator + j
        else:
            numerator = numerator + j*math.pow(x,i)
    return numerator


     #denominator is df(x)/dx
def getDenominators(cash_flows,x):
    denominator = 0.0;
    for i, j in enumerate(cash_flows):
        if i ==0.0:
            continue
        denominator = denominator + i*j*math.pow(x,i-1)
    return denominator

def getIRR(cash_flows):
    steps=[]
    x0 = 5.0
    delta = 1e-15
    IRR = 0.0;
    while ( getNumerator(cash_flows,x0)>delta):
        x0 = x0 - getNumerator(cash_flows,x0)/getDenominators(cash_flows,x0)
        IRR = (1.0/x0) -1
        steps.append(IRR)
    plt.plot(steps)
    plt.show()
    return IRR;


number_Of_Cash_In_Flow = int(input("Please input the number of cash inflow of your project"))
initial__investment_amount = int(input("please input the initial output cash flow"))

cash_flows = [-initial__investment_amount]

print("now, please enter the return cash flows one by one")
for i in range(number_Of_Cash_In_Flow):
    cash_flows.append(int(input("")))

print("Please double check the cash flow")
for i,j in enumerate(cash_flows):
    print(str ( i )+ ":"+ str(j))

print("Now We will compute our IRR")
print(getIRR(cash_flows))


'''1.According to IRR definition, now what I need to do is to solve the equation: p0 + p1*x + p2*x^2 + ... + pn*x^n = 0
     where p0: initial investment amount
           pn: input cash flow
            x: 1/(1+IRR)
   2.so if I can get the value of x, I can easily get the IRR, which is our final result   
      '''




     #notice numerator's value is that the value of function: p0 + p1*x + p2*x^2 + ... + pn*x^n = 0






