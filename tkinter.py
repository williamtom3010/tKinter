from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
root = Tk()
root.title("TUNE IT!!!")
root.iconbitmap('ml.ico')
root.geometry("650x400")


def LOAD_DATASET():
    file_path = filedialog.askopenfilename()
    return file_path

entry = Entry(root, width=25)
entry .grid(row=0, column=1,padx=15, pady=10)




var = tk.StringVar()
models = {"SVM": "SVM", "NB": "NB"}
for key in models:
    tk.Radiobutton(root, text=key, variable=var, value=models[key]).grid()


def TRAIN(file_path, model):
    test_size = int(entry.get())
    data = pd.read_csv(file_path)
    X = data.iloc[:,:-1].values
    y = data.iloc[:,-1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)
    if model == "SVM":
        clf = svm.SVC(kernel='linear', C=1, random_state=0)
    elif model == "Naive Bayes":
        clf = GaussianNB()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(accuracy)
        print(y_pred)
    return accuracy, y_test, y_pred



def click1():
    pass

def play():
    pass


my_button = Button(root, text="Enter the size of the data", command=click1, fg="white", bg="blue", padx=7, pady=10)
my_button.grid(row=1, column=1)
my_button1 = Button(root, text="LOAD_DATASET", command=LOAD_DATASET, fg="white", bg="blue", padx=7, pady=7)
my_button1.grid(row=1, column=2)
my_button2 = Button(root, text="TRAIN", command=TRAIN, fg="white", bg="blue", padx=7, pady=7)
my_button2.grid(row=1, column=3)
my_button3 = Button(root, text="ACCURACY", command=play, fg="white", bg="blue", padx=7, pady=7)
my_button3.grid(row=1, column=4)
my_button4 = Button(root, text="CONFUSION_MATRIX", command=play, fg="white", bg="blue", padx=7, pady=7)
my_button4.grid(row=1, column=5)
root.mainloop()
