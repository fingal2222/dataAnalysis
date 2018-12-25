import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

data=pd.read_csv("lagou_clean.csv",encoding='utf-8')
data.head()
data.info() #看数据情况，是否有缺失，如果关键特征有缺失要处理
data.describe() #数值型变量统计量描述

plt.hist(data['salary'])
plt.show()

sns.distplot(data['salary'])

#计算目标变量值的偏度和峰度
from scipy import stats
print("skewiness:%f" %data['salary'].skew())
print("kurtosis:%f" %data['salary'].kurt())

data['city'].value_counts()
#查看一下规律，把一些数值比较少的统一归为一类

cols=['city','education','position_name','size','stage','work_year']
for col in cols:
    print(data[col].value_counts())

cities=['北京','上海','深圳','广州']
for i,j in enumerate(cities):
    if j not in cities:
        data['city'][i]='其他'
#看一下薪资水平是否和城市之间有关系，其他因素一样看关系

#解决绘图中的中文字体显示问题
from pylab import *
plt.rcParams['font.sans-serif']=['SimHei']
# plt.rc("font",family="SimHei",size="15")#城市与工资水平
sns.boxplot(x=data['city'],y=data['salary'])
plt.show()
#处理industry变量
for i,j in enumerate(data['industry']):
    if ',' not in j:
        data['industry'][i]=j
    else:
        data['industry'][i]=j.split(',')[0]

industries=['移动互联网','金融']
for i,j in enumerate(industries):
    if j not in industries:
        data['industry'][i]='其他'


#行业与工资水平

sns.boxplot(x=data['industry'],y=data['salary'])
plt.show()

#学历与工资水平
sns.boxplot(x=data['education'],y=data['salary'])
plt.show()

#经验与工资水平
sns.boxplot(x=data['work_year'],y=data['salary'])
plt.show()
#企业发展阶段与工资水平
sns.boxplot(x=data['stage'],y=data['salary'])
plt.show()

#企业规模与工资发展水平
sns.boxplot(x=data['size'],y=data['salary'])
plt.show()
#岗位与工资水平
sns.boxplot(x=data['position_name'],y=data['salary'])
plt.show()

#处理文本
ADV=[]
for i in data['advantage']:
    ADV.append(i)
ADV_text=''.join(ADV)

import jieba
result=jieba.cut(ADV_text)
print("分词结果："+','.join(result))
#查看分词结果，发现讲一些固定词汇也进行了划分
jieba.suggest_freq(('五险一金'),True)
jieba.suggest_freq(('六险一金'),True)
jieba.suggest_freq(('带薪年假'),True)
jieba.suggest_freq(('技术大牛'))
jieba.suggest_freq(('免费三餐'),True)
jieba.suggest_freq(('大数据'),True)
jieba.suggest_freq(('租房补贴'),True)
jieba.suggest_freq(('精英团队'),True)
result=jieba.cut(ADV_text)
print("分词结果："+','.join(result))

#读取标点符号库
f=open("chineseStopwords.txt",'r')
stopwords={}.fromkeys(f.read().split("\n"))
f.close()
#加载用户自定义词典

segs=jieba.cut(ADV_text)
mytext_list=[]
#文本清洗
for seg in segs:
    if seg not in stopwords and seg!=" " and len(seg)!=1:
        mytext_list.append(seg.replace(" ",""))

ADV_cloud_text=",".join(mytext_list)
print("分词结果："+ADV_cloud_text)
from wordcloud import WordCloud
wc = WordCloud(
    background_color='white',# 设置背景颜色
    font_path=r'chinese.stzhongs.ttf',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=2000, # 设置最大现实的字数
    max_font_size=150,# 设置字体最大值
    random_state=30# 设置有多少种随机生成状态，即有多少种配色方案
)

wc.generate_from_text(ADV_cloud_text)
plt.imshow(wc)
plt.show()
data=data.drop(['address','industrylabels','company_name'],axis=1)
data.to_csv("lagou_data5.csv")

import warnings
warnings.filterwarnings('ignore')

#特征工程
pd.get_dummies(data['city'].head())
col_feature=['city','industry','education','position_name','size','stage','work_year']
for col in col_feature:
    temp=pd.get_dummies(data[col])
    data=pd.concat([data,temp],axis=1)
    data=data.drop([col],axis=1)

pd.options.display.max_columns=800
data=data.drop(['advantage','label'],axis=1) #删除无用信息

#职位描述特征的信息提取
for i,j in enumerate(data['position_detail']):
    if 'python' in j:
        data['position_detail'][i]=j.replace('python', 'Python')

data['Python']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'Python' in j:
        data['Python'][i]=1
    else:
        data['Python'][i]=0

data['R']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'R' in j:
        data['R'][i]=1
    else:
        data['R'][i]=0


#sql(SQL),Excel,linux(Linux),Java

for i,j in enumerate(data['position_detail']):
    if 'sql' in j:
        data['position_detail'][i]=j.replace('sql','SQL')

data['SQL']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'SQL' in j:
        data['SQL'][i]=1
    else:
        data['SQL'][i]=0

for i,j in enumerate(data['position_detail']):
    if 'linux' in j:
        data['position_detail'][i]=j.replace('linux','Linux')

data['Linux']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'Linux' in j:
        data['Linux'][i]=1
    else:
        data['Linux'][i]=0

data['Excel']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'Excel' in j:
        data['Excel'][i]=1
    else:
        data['Excel'][i]=0


data['Java']=pd.Series()
for i,j in enumerate(data['position_detail']):
    if 'Java' in j:
        data['Java'][i]=1
    else:
        data['Java'][i]=0
#同样处理其他，比C++,tensorflow,spark等，根据数据的具体情况来确定

#因为已经处理来position_deatil删除掉position_detail,salary是因变量，要从特征中删除
data2=data.drop(['position_detail','salary'],axis=1)

data2.to_csv("lagou_feature.csv")

X=data2
y=np.log(data['salary'].values.reshape(-1,1))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
print(X_train.shape,y_train.shape,X_test.shape,y_test.shape)

from sklearn.model_selection import KFold
from sklearn.ensemble import GradientBoostingRegressor
model=GradientBoostingRegressor(n_estimators=40,max_depth=2)
model.fit(X_train,y_train)

from sklearn.metrics import  mean_squared_error
y_pred=model.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,y_pred)))