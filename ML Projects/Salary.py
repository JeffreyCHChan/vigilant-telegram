import pandas as pd
import numpy as np
'''from sklearn import preprocessing, model_selection
from sklearn.linear_model import Lasso'''
import tensorflow as tf
from tensorflow.python.data import Dataset
import math
from sklearn import metrics

pd.set_option('display.max_columns', None)
df = pd.read_csv('C:\\Users\\Jeff\\Downloads\\Salaries.csv')

#print(df.columns)
df.fillna(0,inplace= True)
df.replace('Not Provided', 0, inplace= True)
df = df.drop(['Id',"EmployeeName",'Notes'], axis=1)
df.reindex(np.random.permutation(df.index))

def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
            df[column] = list(map(convert_to_int, df[column]))
    return df

handle_non_numerical_data(df)

#print(df.head(10))
#print(df['JobTitle'].unique())

targets = df[["TotalPay"]]

my_feature = df[["JobTitle"]]
feature_columns = [tf.feature_column.numeric_column("JobTitle")]

my_optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns,
    optimizer=my_optimizer)

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):

    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

linear_regressor.train(input_fn = lambda:my_input_fn(my_feature, targets),steps=100)

# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't
# need to repeat or shuffle the data here.
prediction_input_fn =lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# Print Mean Squared Error and Root Mean Squared Error.
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)
'''
X = np.array(df.drop(['BasePay'],1))
y = np.array(df['BasePay'])
X = preprocessing.scale(X)
y = np.array(df['BasePay'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,test_size=0.2)
clf = Lasso()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)
print(accuracy)'''