#-*-coding:utf-8-*-
# %run d:chi_square_test.py
from io import StringIO
import pandas as pd    
from scipy import stats
import numpy as np
from IPython.display import display, HTML
'''
text = u"""
source	ismoblie	visits
社交媒体分享	否	1 
社交媒体分享	是	1 
本站来源	否	361 
本站来源	是	361 
付费搜索	否	333 
付费搜索	是	333 
付费引荐	否	500 
付费引荐	是	500 
自然搜索	是	50 
自然搜索	否	50 
友情引荐	是	939 
友情引荐	否	939 
直接来源	是	3827 
直接来源	否	3827 

"""
'''
#df = pd.read_csv(StringIO(text),sep='\t')
df = pd.read_csv('d:\\python\\data.csv',encoding='gbk')
#df = pd.read_excel('d:\\data.xlsx',sep='\t')
print(df)

x = df.pivot("sku","ismoblie","quantity")
x.fillna(0,inplace=True)
x.sort_values(by=u'否',inplace=True,ascending=False)
display(x.astype('int'))

mat = x.values.T
chi2, p, dof, ex = stats.chi2_contingency(x.values.T)
if p>0.05:
    print(u"通过卡方检验，P值为{}，用户购买产品和设备无关。".format(p))
else:
    print(u"通过卡方检验，P值为{}，用户购买产品和设备有关。".format(p))
    
#原假设，两个序列是独立的，没有关联，即两个序列的差值不为0
#如果p值小于0.05，拒绝原假设，则两个序列有相关性。
#如果p值小于0.05,那么用户对产品的购买是收到设备影响的。

n = mat.sum()      # 计算样本量
crmersv = np.sqrt(chi2 / (n*(min(mat.shape)-1)))
print u"Crmer'sV相关系数: %s" % crmersv



