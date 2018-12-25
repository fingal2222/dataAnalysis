#过滤法值方差筛选
from sklearn.feature_selection import  VarianceThreshold
X=[[0,0,1],[0,1,0],[1,0,0],[0,1,1],[0,1,0],[0,1,1]]
sel=VarianceThreshold(threshold=0.8*(1-0.8))
print(sel.fit_transform(X))#第一列为0的比例超过了80%，会在结果中删除这一列

#过滤法之卡方检验
from sklearn.datasets import load_iris
from sklearn.feature_selection import  SelectKBest
from sklearn.feature_selection import chi2
iris=load_iris()
x,y=iris.data,iris.target
print(x.shape)
x_new=SelectKBest(chi2,k=2).fit_transform(x,y)#通过卡方筛选出两个最好的特征
print(x_new.shape)

#包装法
#选择一些算法，根据算法在数据上的表现来选择特征集合，一般选择的算法包括随机森林，支持向量机和k近邻法
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import  StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import  make_classification

x,y=make_classification(n_samples=1000,n_features=25,n_informative=3,n_redundant=2,
                        n_repeated=0,n_classes=8,n_clusters_per_class=1,random_state=0
                        )
svc=SVC(kernel='linear')
rfecv=RFECV(estimator=svc,step=1,cv=StratifiedKFold(2),scoring='accuracy')
rfecv.fit(x,y)

print("optimal number of feature: %d"  %rfecv.n_features_)

plt.figure()
plt.xlabel("number of feature selector")
plt.ylabel("cross validatuon score (nb of correct classification)")
plt.plot(range(1,len(rfecv.grid_scores_)+1),rfecv.grid_scores_)
plt.show()


#嵌入法之基于惩罚项的特征选择法

from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
iris=load_iris()
x,y=iris.data,iris.target
print("原始数据特征纬度：",x.shape)
lsvc=LinearSVC(C=0.01,penalty="l1",dual=False).fit(x,y)
model=SelectFromModel(lsvc,prefit=True)
x_new=model.transform(x)
print("l1惩罚处理之后的数据纬度：",x_new.shape)

#嵌入法之基于树模型的特征选择法
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import  load_iris
from sklearn.feature_selection import SelectFromModel

iris=load_iris()
x,y=iris.data,iris.target
print("原始数据特征纬度：",x.shape)

clf=ExtraTreesClassifier()
clf=clf.fit(x,y)
clf.feature_importances_
model=SelectFromModel(clf,prefit=True)
x_new=model.transform(x)
print("树模型处理之后的数据纬度：",x_new.shape)


