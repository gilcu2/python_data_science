import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data_name="iris"
target_var="species"

def load():
    return sns.load_dataset('iris')

def pair_plot(data):
    sns.pairplot(data, hue=target_var, height=1.5)

def extract_features_and_target(data):
    return (data.drop(target_var,axis=1),data[target_var])

if __name__ == '__main__':
    iris=load()
    print(iris.head())

    # pair_plot(iris)
    # plt.show()

    (X,y)=extract_features_and_target(iris)

    print(X.shape,y.shape)