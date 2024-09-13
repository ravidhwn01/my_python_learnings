# loading the data frame
import pandas as pd
df = pd.read_csv('Iris.csv')
df.head()
df.describe()
#splitting in train and test data
x_label = df.drop(['Id', 'Species'], axis=1)
y_label = df[['Species']]
y_label.head()
y_label_uniques = y_label['Species'].unique()
y_label_uniques
# define the value to be tested on :
X = {"SepalLengthCm" : 5.1,
     "SepalWidthCm" : 3.5,
     "PetalLengthCm" : 1.4,
     "PetalWidthCm" : 0.2}

attributes = list(x_label.columns)
def euclidean_distance(x, y):
  dist_list = []
  for i in range(len(x)):
    distance = 0
    for j in attributes:
      distance += (x[j][i] - y[j])**2
    dist_list.append(distance**0.5)
  return dist_list

print(euclidean_distance(x_label, X))
k = 5
distance = euclidean_distance(x_label, X)
# create a df2 data frame containing distance and y_label
df2 = pd.DataFrame(y_label)
df2['distance'] = distance
df2.head()
# getting Species values with lowest distance
df2.sort_values(by='distance', ascending=True, inplace=True)
df2.head()
k = 5

label_dict = {"Iris-setosa" : 0,
              'Iris-versicolor' : 0,
              'Iris-virginica' : 0}

# taking 5 values from species
for i in range(k):
  for j in y_label_uniques:
    if df2['Species'][i] == j:
      label_dict[j] += 1

print(label_dict)
# printing the key with the highest value
for key, value in label_dict.items():
  if value == max(label_dict.values()):
    print(key)