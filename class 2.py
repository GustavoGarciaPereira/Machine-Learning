from sklearn.datasets import load_iris

iris = load_iris()

print iris.feature_names

print iris.target_names
print iris.data[0]
print iris.target[0]

for i in range(len(iris.target)):
	print "Exemplo %d: label %s, feature %s "%(i,iris.target[0],iris.data[i])
