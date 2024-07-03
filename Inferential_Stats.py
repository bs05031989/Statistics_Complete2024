"""
Hypothesis Testing : We use data from a sample to draw conclusions about a population parameter.

Sample data ------ Conclusion ----- Population

Steps to do hypothesis testing :
1. We have to make an experiment to know weather a coin is fair or not 
2. We need to define a) Null Hypothesis H0 : Its is the by default behaviour we expect : Coin is fair
                     b) Alternate hypothesis H1 : Coin is not fair
3. We need to perform experiment to validate the hypothesis : 100 coin tosses
4. We need to define the confidence interval (Decision Boundary) based on which we are going to accept or reject
the null hypothesis.
5. Domain expertise is needed to define confidence interval
6. Normal prob dist is basis to define CI in percentage
7. if 95% CI remaining is significant value : 5%


Probability Distribution Function contains two types:
1) Probability density function (pdf) : Data is continous Random variable to check distribution.
2) probability mass function (pmf) : Data is Discrete Random variable to check distribution.

Cumulative distribution function

Random Varible : It is the process of mapping the output of a random process/experiment to a number.

example : Toss of a coin : X - {0: if head ; 1: if tail} Based on the outcome of the experiment.

Pdf (Prob density Function) : Distribution of continous random variables : X axis (Random Variable X), Y axis (Prob density)

Prob Density = Gradient Descent of Cumalitive Distribution function

Cumulative distribution function : x axis (X Random Variable) y axis (0 to 1) (S curve)

Probability Mass function : Discrete Random Variables : X axis (Random Variable dice 1,2,3,4,5,6) y axis (probability 1/6,2/6,3/6,4/6,5/6)
"""