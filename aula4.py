from sklearn import datasets
iris = datasets.load_iris()

x = iris.data     #caracteristicas
y = iris.target   #marcadores

#print "x",x
#print "y",y


#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .5)


#classificador
#from sklearn import tree
#my_classifier = tree.DecisionTreeClassifier()

#outro classificador
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(x_train,y_train)

prediction = my_classifier.predict(x_test)
print prediction


from sklearn.metrics import accuracy_score
print accuracy_score(y_test , prediction)