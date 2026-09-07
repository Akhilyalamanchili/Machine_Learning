import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data =pd.read_csv("linear_regression_data.csv")
print(data.head)
plt.scatter(data.hours_studied,data.exam_score)
def gradent(mn,bn,L,points):
    m_grad=b_grad=0
    n=len(points)
    for i in range(n):
        x,y=points.iloc[i,0],points.iloc[i,1]
        m_grad+=-(2/n)*x*(y-(mn*x+bn))
        b_grad+=-(2/n)*(y-(mn*x+bn))
    m=mn-(L*m_grad)
    b=bn-(L*b_grad)
    return m,b
m=b=0
L=0.001
does=3000
for i in range(does):
    m,b=gradent(m,b,L,data)
x=np.linspace(data.hours_studied.min(),data.hours_studied.max(), 100)
y=m*x+b;
plt.plot(x,y)
plt.xlabel("Hours_studied")
plt.ylabel("Exam score")
plt.show()
