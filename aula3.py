import numpy as np
import matplotlib.pyplot as plt 


greyhounds = 500
labs = 500

grey_height = 28 +4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)


#nao aparece barras divididas

plt.hist([grey_height,lab_height],stacked=True,color=['r','b'])
plt.title('google')
plt.show()


#aparece barras divididas

plt.hist([grey_height,lab_height],normed=1,color=['r','b'], histtype='bar', rwidth=0.8)
plt.title('meu')




plt.show()
