import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    data_name = "iris"
    target_var = "species"

    data=sns.load_dataset(data_name)
    (X, y) =(data.drop(target_var,axis=1),data[target_var])

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,random_state=1)
    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)

    accuracy=accuracy_score(ytest, y_model)
    print(f"accuracy: {accuracy}")
