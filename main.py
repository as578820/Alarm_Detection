# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
from sklearn.pipeline import Pipeline


def fun01():
    #print("Hi from fun01")
    df = pd.read_excel("Historical Alarm Cases.xlsx")
    x = df[['Ambient Temperature( deg C)', 'Calibration(days)', 'Unwanted substance deposition(0/1)', 'Humidity(%)',
            'H2S Content(ppm)', 'detected by(% of sensors)']]
    y = df['Spuriosity Index(0/1)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])

    pipe.fit(x_train, y_train)
    joblib.dump(pipe, "alarm_pipeline.pkl")
    y_pred = pipe.predict(x_test)
    print("Accuracy score: ", accuracy_score(y_test, y_pred))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    fun01()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
