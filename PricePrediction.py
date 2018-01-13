from tkinter import *
import tkinter as tk

import csv
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
reg = linear_model.LinearRegression()

def train_dataset():

    fle = open("TrainDataSet.txt", 'r')
    wfile = open('TrainDataSet.csv', 'w')
    line = fle.readline()

    col = "p_0"
    for i in range(1, 13):
        nn = "p_" + str(i)
        col = col + "," + nn;
    col = col + "," + "PRICE"

    wfile.write(col + "\n")

    for line in fle:
        sep = line.split()
        string = ""
        for i in range(0, len(sep)):
            if (i == 0):
                string = string + str(sep[i])
            else:
                string = string + "," + str(sep[i])
        wfile.write(string + "\n")

    fle.close()
    wfile.close()
    print("Train Data Ok")

    # training is start
    X_features = []
    temp_data = []
    Y_features = []

    data = pd.read_csv("E:/Programming OOP/HousePricePrediction/TrainDataSet.csv").as_matrix()

    for i in range(0, 481):
        temp_data = data[i][:13]
        X_features.append(temp_data)
        Y_features.append(data[i][13:14])


    reg.fit(X_features, Y_features)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    print("Traing is finished")


def Get_Result():
    fle_t = open("TestDataSet.txt", 'r')
    wfile_t = open('TestDataSet.csv', 'w')
    line = fle_t.readline()

    col = "p_0"
    for i in range(1, 13):
        nn = "p_" + str(i)
        col = col + "," + nn;
    col = col + "," + "PRICE"

    wfile_t.write(col + "\n")

    for line in fle_t:
        sep = line.split()
        string = ""
        for i in range(0, len(sep)):
            if (i == 0):
                string = string + str(sep[i])
            else:
                string = string + "," + str(sep[i])
        wfile_t.write(string + "\n")
    fle_t.close()
    wfile_t.close()
    print("Test Data Ok")
    x= int(input_field.get())

    data = pd.read_csv("E:/Programming OOP/HousePricePrediction/TestDataSet.csv").as_matrix()
    X_features_test=[]

    temp_data = data[x][:13]
    X_features_test.append(temp_data)
    houseprice = reg.predict(X_features_test)
    print("price")
    print(x)
    print(houseprice)

    w1_1 = tk.Label(root, bg="white", text="Predicted House Price", fg="black", font=("Helvetica", 10), anchor=W)
    w1_1.place(x=400, y=200)
    w1_1.config(height=2, width=20)

    w1_1 = tk.Label(root, bg="red", text=str(houseprice[0][0]), fg="white", font=("Helvetica", 10), anchor=W)
    w1_1.place(x=400, y=250)
    w1_1.config(height=3, width=20)




def Get_input():
    inputValue = int(input_field.get()) # koto number input
    x=inputValue
    temp_data=[]

    data = pd.read_csv("E:/Programming OOP/HousePricePrediction/TestDataSet.csv").as_matrix()
    #print(data[0])

    temp_data = data[inputValue][:13]

    print(inputValue)

    w1_1 = tk.Label(root, bg="yellow", text=str(temp_data[0]), fg="black", font=("Helvetica", 10), anchor=W)
    w1_1.place(x=150, y=100)
    w1_1.config(height=1, width=20)

    w2_1 = tk.Label(root, bg="yellow", text=str(temp_data[1]), fg="black", font=("Helvetica", 10), anchor=W)
    w2_1.place(x=150, y=130)
    w2_1.config(height=1, width=20)
    w3_1 = tk.Label(root, bg="yellow", text=str(temp_data[2]), fg="black", font=("Helvetica", 10), anchor=W)
    w3_1.place(x=150, y=160)
    w3_1.config(height=1, width=20)
    w4_1 = tk.Label(root, bg="yellow", text=str(temp_data[3]), fg="black", font=("Helvetica", 10), anchor=W)
    w4_1.place(x=150, y=190)
    w4_1.config(height=1, width=20)
    w5_1 = tk.Label(root, bg="yellow", text=str(temp_data[4]), fg="black", font=("Helvetica", 10), anchor=W)
    w5_1.place(x=150, y=215)
    w5_1.config(height=1, width=20)
    w6_1 = tk.Label(root, bg="yellow", text=str(temp_data[5]), fg="black", font=("Helvetica", 10), anchor=W)
    w6_1.place(x=150, y=240)
    w6_1.config(height=1, width=20)
    w7_1 = tk.Label(root, bg="yellow", text=str(temp_data[6]), fg="black", font=("Helvetica", 10), anchor=W)
    w7_1.place(x=150, y=270)
    w7_1.config(height=1, width=20)
    w8_1 = tk.Label(root, bg="yellow", text=str(temp_data[7]), fg="black", font=("Helvetica", 10), anchor=W)
    w8_1.place(x=150, y=300)
    w8_1.config(height=1, width=20)
    w9_1 = tk.Label(root, bg="yellow", text=str(temp_data[8]), fg="black", font=("Helvetica", 10), anchor=W)
    w9_1.place(x=150, y=330)
    w9_1.config(height=1, width=20)
    w10_1 = tk.Label(root, bg="yellow", text=str(temp_data[9]), fg="black", font=("Helvetica", 10), anchor=W)
    w10_1.place(x=150, y=360)
    w10_1.config(height=1, width=20)
    w11_1 = tk.Label(root, bg="yellow", text=str(temp_data[10]), fg="black", font=("Helvetica", 10), anchor=W)
    w11_1.place(x=150, y=390)
    w11_1.config(height=1, width=20)
    w12_1 = tk.Label(root, bg="yellow", text=str(temp_data[11]), fg="black", font=("Helvetica", 10), anchor=W)
    w12_1.place(x=150, y=420)
    w12_1.config(height=1, width=20)
    w13_1 = tk.Label(root, bg="yellow", text=str(temp_data[12]), fg="black", font=("Helvetica", 10), anchor=W)
    w13_1.place(x=150, y=450)
    w13_1.config(height=1, width=20)




#Frame
root = tk.Tk()
root.geometry("600x500+400+100")
root.title("House Price Prediction")
root.resizable(width=False, height=False)
root.config(bg="gray")

frame=tk.Frame(root)
frame.pack()
train_button=tk.Button(root,text="Train Dataset",command=train_dataset)
train_button.config(padx=15,pady=10,bg="white", fg="blue",font=('Times New Roman',20))
train_button.place(x=350,y=0)
#train_button.pack()
#train_button.place(height=100,width=100)

result_button=tk.Button(root,text="Result",command=Get_Result)
result_button.config(padx=15,pady=10,bg="white", fg="blue",font=('Times New Roman',20))
result_button.place(x=400,y=100)
#result_button.pack()

select_button=tk.Button(root,text="select",command=Get_input)
select_button.config(padx=15,pady=10,bg="white", fg="blue",font=('Times New Roman',20))
select_button.place(x=170,y=0)

input_field=tk.Entry(root,bd=5)
input_field.place(x=5,y=20)

w1 = tk.Label(root, text="CRIM", font=("Helvetica", 10))
w1.place(x=10,y=100)
w1.config(height=1,width=10)

w2 = tk.Label(root, text="ZN", font=("Helvetica", 10))
w2.place(x=10,y=130)
w2.config(height=1,width=10)

w3 = tk.Label(root, text="INDUS", font=("Helvetica", 10))
w3.place(x=10,y=160)
w3.config(height=1,width=10)

w4 = tk.Label(root, text="CHAS", font=("Helvetica", 10))
w4.place(x=10,y=190)
w4.config(height=1,width=10)
w5 = tk.Label(root, text="NOX", font=("Helvetica", 10))
w5.place(x=10,y=215)
w5.config(height=1,width=10)
w6 = tk.Label(root, text="RM", font=("Helvetica", 10))
w6.place(x=10,y=240)
w6.config(height=1,width=10)
w7 = tk.Label(root, text="AGE", font=("Helvetica", 10))
w7.place(x=10,y=270)
w7.config(height=1,width=10)
w8 = tk.Label(root, text="DIS", font=("Helvetica", 10))
w8.place(x=10,y=300)
w8.config(height=1,width=10)
w9 = tk.Label(root, text="RAD", font=("Helvetica", 10))
w9.place(x=10,y=330)
w9.config(height=1,width=10)
w10 = tk.Label(root, text="TAX", font=("Helvetica", 10))
w10.place(x=10,y=360)
w10.config(height=1,width=10)
w11 = tk.Label(root, text="PTRATIO", font=("Helvetica", 10))
w11.place(x=10,y=390)
w11.config(height=1,width=10)
w12 = tk.Label(root, text="B", font=("Helvetica", 10))
w12.place(x=10,y=420)
w12.config(height=1,width=10)
w13 = tk.Label(root, text="LSTAT", font=("Helvetica", 10))
w13.place(x=10,y=450)
w13.config(height=1,width=10)




root.mainloop()
