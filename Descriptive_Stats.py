"""

1111111111111111111111111111111111111111
Statistics:

1. Descriptive
2. Inferential

1. Descriptive : Summarizing, analyze & visualize Data
a) Measure of central Tendency
b) Measure of Dispersion
c) Correlation, Covariance, PDF, CDF, PMF
d) Histogram, Univariate, Bivariate 
e) Box-Plots, Whisker Plot, Outlier

2. Inferential : Hypothesis Testing : a) Null Hypothesis b) Alternate Hypothesis
Sample Data ---------- conclusion to population
ztest, t test, chi square test, Anova test - Ftest

Example : SBI bank at a location : Distance, Frequency

Data ---- Statstools

Data Never Lies

KPI identification

11111111111111111111111111111111111111111111111111111111111111

222222222222222222222222222222222222222222222222222222222
What is statistics & its types
statistics is the science of collecting , organizing and analyzing data
 
DATA : Facts or pieces of information

Eg : Height of students in class ( 123cm, 134cm, 172cm)
Gender of a person visiting the doctor (M,F,M,M)

Types of stats

1. Descriptive : It consists of organizing & summarizing of data.
2. Inferential : It consists of using data you have (sample) measured to form conclusions(population)

Descriptive stats ( Measure of central tendency a) Mean, b) Median, c) Mode)
(Measure of Dispersion : a) Variance b) stddev)
(Different types of distribution of data )
(Histograms, PDF, PMF)


Inferential Stats : ( Z test, T test, Chi -Square test, Anova  F test) : Hypothesis Testing
(H0, H1 , P value )

Ex : Lets consider there are 20 classrooms in the college, and you have collected the ages of the student in the class

Ages (19,21,24,27)

Descriptive : What is the common age in the stats call : Mean age (central Tendency )

Inferential : Are the ages of the student in the classes similar to the ages in the university

Sample : Ages of the student in class
Population : Ages of the student in university

333333333333333333333333333333333333333333333333333333333333333333333333333
Population & Sample

Population : The group that we are interested in studying.
Sample : A subset of the Population 

Example : Exit Poll {Which party will won ? }
Parameters : Age >18 Years  
Overall Population : Population

Ex : Average Height of the People

Sampling Techniques : The goal of sampling is to create a sample that is representative of the entire population

Population (N) : sample (n)

Types of sampling : 1) Simple Random Sampling , When performing simple random sampling, every member of the population(N) 
has an equal chance of being selected for your sample(n).

2) Stratified Sampling : Stratified : Strata : Layers non overlapping group 
Ex : Pop -----------Male -------- Female (Non Overlapping Group)

Stratified Sampling is a method of sampling in which the population is divided into homogeneous subgroups called strata, 
and a simple random sample is taken from each stratum. The sample is then combined to form a representative sample of the population.

3) Systematic sampling : Every 4th person outside the mall (Survey)

4) Convenience Sampling (Voluntary response sampling) : Topic (Data Science)--- Domain Expertise 

exit Poll : Random ,    Disease Info : Convenience Sampling , Household Expenses : Stratified Sampling 333333333333333333333333333333333333333333333333333333333333333333333333333

44444444444444444444444444444444444444444444444444444444444444444444444444444
What are variables and its types?
variable : variable is a property that can take on many values
ex: age : 12
            13
Height : 173.15 : variable is singular 

ages : Plural mode {23,45,65}

Variable Types :
1) Quantitative : a) Discrete: Always Whole Number : No of Bank Accounts : 1 b) Continuous : Height : 175.5,180.9
2) Qualitative/Categorical : It is based on property : Ex : Classification  : Gender :M :F
44444444444444444444444444444444444444444444444444444444444444444444444444444

55555555555555555555555555555555555555555555555555555555555555555555555555

Measure of Central Tendency : Mean : Median : Mode

Central tendency refers to the measure used to determine the center of the distribution of data.

Mean (Average) : It is the sum of all the observations divided by the number of observations. It is bad in case of outliers
Median : Sort all the numbers, Find the Central Element 
Two cases : 1) Odd Length  : Very easy
            2) Even Length : Two Elements Central Element : Take average of these two numbers 

            It Is easiest way to handle outliers

Mode : Most Frequent Element from the set

It is used to handle categorical variables
55555555555555555555555555555555555555555555555555555555555555555555555555

666666666666666666666666666666666666666666666666666
Measure of Dispersion : Variance : Standard Deviation

Dispersion refers to the measure used to quantify the amount of variation or spread in a set of values.  : Spread

Take Normal Distribution curve as reference

Variance : Sigma^2  for Population Formula

Variance : Sum of (x - Mean)^2 / N 

Variance for sample : (x-xi)^2/n-1 : (n-1) = Bessels Correction , Degree of freedom

Example : X = {1,2,3,4,5}

Sample Variance : {Spread of data}

Standard Deviation : Sigma = sqrt(Variance)

If Mean is known : Sample standard deviation is known :  mu + Sigma 

If Variance is a Big Number : Sd is also a big number : Large Spread
If Variance is a small Number : Sd is also a small number : Less Spread , Height Higher

6666666666666666666666666666666666666666666666666

777777777777777777777777777777777777777777777

Percentiles & Quartiles : 

Percentage : {1,2,3,4,5}

% of the numbers that are even

2/5  = 40 % of the numbers are even

Percentile : A percentile is a value below which a certain percentage of observation lies.

95 percentile : Person has got better marks than 95 percent of the entire sample.

Ex : {2,2,3,4,5,5,5,6,7,8,8,8,8,8,9,9,10,11,11,12}
What is the Percentile ranking of 10

Total Count = n = 20

Percentile Rank of x  = (# of values below x /n ) x 100

16/20 = 80 Percentile 

10 Value is bigger than the entire pop

** What value exist at percentile rank of 25

value = (Percentile /100) x(n+1)

5.25 as per formula : Index : Goes on the index in set to get the exact value

Quartiles : 1/4 

25 Percent = 1st Quartile
75 Percent = 3rd Quartile

IQR = Q3-Q1 : IQR helps us to find outliers using box -plot

777777777777777777777777777777777777777

888888888888888888888888888

Five Number summary : Box Plot
1 : Minimum
2: First Quartile (25%) Q1
3: Median 
4: Third Quartile (75%) Q3
5: Maximum

Removing the outliers

{1,2,2,2,3,3,4,5,5,5,6,6,6,6,7,8,8,9,27}

[Try to define : Lower Fence ----- Higher Fence ]

Lower Fence : Q1-1.5(IQR)
Higher Fence : Q3+1.5(IQR)

Q1 = 3 , Q3 = 7 ( Taken by index values)
LF = -3 : HF = 13

Box Plot used to draw 

8888888888888888888888888888888

9999999999999999999999999999

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

dataset = [11,21,13,14,25]

plt.hist(dataset) : can be used to see outliers

# Zscore 

outliers =[]
def detect_outliers(data):
    threshold=3 # 3rd standard deviation
    mean=np.mean(data)
    std=np.std(data)

    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:
            outliers.append(i)
    return outliers


def detect_outliers(dataset):


# IQR Technique

1 Sort the data
2 Calculate Q1 and Q3
3 IQR(Q3-Q1)
4 Find Lower Fence 
5 Find Upper Fence

dataset = sorted(dataset)
q1,q3 = np.percentile(dataset,[25,75])
lower_fence= q1 - 1.5 * (q3-q1)     
Higher_fence= q3 + 1.5 * (q3-q1)

sns.boxplot(dataset)
9999999999999999999999999999
"""