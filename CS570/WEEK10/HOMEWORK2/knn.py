# Import the necessary modules from the scikit-learn library
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# Import the accuracy_score module from the scikit-learn library
from sklearn.metrics import accuracy_score
# Import the KNeighborsClassifier module from scikit-learn library
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
    # Load the iris dataset
    iris = load_iris()

    # Split the dataset into training and testing sets using train_test_split() function
    # test_size = 0.2 means that 20% of the data will be used for testing and the remaining 80% for training
    # random_state = 42 sets the random seed for reproducibility
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)

    # Define the number of neighbors to use
    k = 3

    # Instantiate a KNeighborsClassifier object with the value of k
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the model using the training data
    knn.fit(X_train, y_train)

    # Make predictions on the test data using the trained k-NN classifier
    y_pred = knn.predict(X_test)

    # Calculate the accuracy of the model on the test data
    # by comparing the predicted labels to the actual labels in the test set
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
