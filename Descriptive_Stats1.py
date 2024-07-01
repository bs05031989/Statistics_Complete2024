"""
1111111111111111111111111
Normal Distribution (Gaussian)
(68-95-99.7) 3 sigma rule

Bell Curve : 

Make a histogram out of a data set : {1,2,2,3,3,4,5,5,5,6,6,7,7,7,8,8}
1 Plot it against the frequency (X-axis : Number ,  Y axis : Frequency)
2 Smoothen the histogram by kernel density estimator (KDE) and convert it into a curve (PDF)

Any Random Variable that follows Normal Dist : 

1. Symmetrical
2. Mean is the central element.
 
Ex : Height of pop, Weight of people, IRIS, Space bar key hit
1111111111111111111111111
2222222222222222222222222
Central Limit Theorem

If my sample size n>30 ; mean x1, 
and multiple samples like above and got x2,x3,x4

Calculate mean of all samples taken with condition that sample size should be equal or grater than 30

If you are going to plot All means : It will give you a normal dist curve

2222222222222222222222222
33333333333333333333
Log Normal Distribution :
Right Skewed Distribution 

If X belongs to log Normal Dist : Y ~ ln(x) = Normal Dist

Ex : Wealth Distribution : X : Amount of Wealth , Y : No of Persons
Ex : Type of Comments : X : Comments types , Y : No of comments

Data transformation tech : used to make log normal dist to normal dist to effectively fit the data in m/c learning training.

33333333333333333333
44444444444444444444
Power Law : 80-20 Rule (Pareto Dist)

If your data follow power law : Y ~ x^a where a is constant

Box -cox transformation used to convert this into a normal dist
 
alpha : Hyperparameter : PDF Curve (Alpha 1 to infinite)

44444444444444444444

Code :

ages = [23,24,24,35,45,34,35]

import numpy as np
print(np.mean(ages))
print(np.median(ages))

import statistics
statistics.mode(ages)  # most frequent element

import seaborn as sns
sns.boxplot(ages) # for plotting use for outlier

5 Number summary

q1,q3 =np.percentile(ages,[25,75])

IQR = Q3-Q1

lower_fence = Q1-1.5(IQR)
Higher_Fence = Q3+1.5(IQR)

Measure of Dispersion

Variance 
statistics.variance(ages) :  It uses the formula of sample variance

np.var(ages,axis=0) : It uses the formula of population variance

def variance(data,dof=0): # Dof = 0 Population Variance  # Dof =1 Sample Variance 
    n=len(ages)
    # mean of data
    mean=sum(data)/n
    #variance
    deviation=[(x-mean)**2 for x in data]
    variance =sum(deviation)/(n-DOF)
    return variance

statistics.pvariance(ages)


# Standard Deviation
import math
math.sqrt(statistics.pvariance(ages))

Histogram

import seaborn as sns
sns.histplot(ages,kde=True)

Normal Dist data creation

s=np.random.normal(0.5,0.2,1000) (mean,sd,no of points)

Log Normal Dist, Power Dist
mu,sigma = 3,1 (mean,std)

s = np.random.lognormal(mu,sigma,100)

df.corr()










"""