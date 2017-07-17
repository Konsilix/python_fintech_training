#!/usr/bin/env python

# see https://medium.com/@dhwajraj/python-regression-analysis-part-4-multiple-linear-regression-ed09a0c31c74

from pandas.core import datetools
import numpy as np
import statsmodels.api as sm

import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


X= [[150,100],[159,200],[170,350],[175,400],[179,500],[180,180],[189,159],[199,110],[199,400],[199,230],[235,120],[239,340],[239,360],[249,145],[249,400]]

Y= [0.73,1.39,2.03,1.45,1.82,1.32,0.83,0.53,1.95,1.27,0.49,1.03,1.24,0.55,1.3]

# perform linear regression
X_1=sm.add_constant(X)
results=sm.OLS(Y,X_1).fit()

# regression coefficients
# Y= c + a.X1 + b.X2
# c=1.63384178, a=-0.00637932 and b=0.00316077
print(results.params)

# now using pandas
df2=pd.DataFrame(X,columns=['Price','AdSpends'])
df2['Sales']=pd.Series(Y)

# We have created the DataFrame with our input data. And now in the steps below, we will invoke ols method of formula api
model = smf.ols(formula='Sales ~ Price + AdSpends', data=df2)
results_formula = model.fit()
print(results_formula.params)

x_surf, y_surf = np.meshgrid(np.linspace(df2.Price.min(), df2.Price.max(), 100),np.linspace(df2.AdSpends.min(), df2.AdSpends.max(), 100))
onlyX = pd.DataFrame({'Price': x_surf.ravel(), 'AdSpends': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df2['Price'],df2['AdSpends'],df2['Sales'],c='blue', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='None', alpha=0.01)
ax.set_xlabel('Price')
ax.set_ylabel('AdSpends')
ax.set_zlabel('Sales')
#plt.show()

X_new= [[180,100],[199,200],[170,370],[195,400],[279,400],[280,280]]
df2_new= pd.DataFrame(X_new,columns=['Price','AdSpends'])
results_new = results_formula.predict(df2_new)
print(results_new)



