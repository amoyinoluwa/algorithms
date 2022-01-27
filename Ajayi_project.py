'''
=======================================================================================================
This program computes and displays the descriptive statistics of a data set in a CSV file.
The second and third columns of the CSV file must contain only numbers, otherwise an exception will be raised.
For this program to work properly, the matplotlib, breezypythongui, pandas, scipy and PIL modules
need to be installed on the user's system.
=======================================================================================================
'''
__author__ = "Joseph Ajayi"
from breezypythongui import EasyFrame
import matplotlib.pyplot as plt
import csv
from tkinter.font import Font
from tkinter import *
import tkinter.filedialog
import pandas as pd
from PIL import ImageTk, Image
import statistics
from scipy import stats
from scipy.stats import kurtosis, skew  
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
class DataAnalytics(EasyFrame): #class that takes in the Easyframe method as argument
    def __init__(self):
        EasyFrame.__init__(self, title = "Data Analytics Report")
        self.calculate = self.addButton("Report Statistics", row = 1, column = 0, command = self.computeStats)
        self.outputArea = self.addTextArea(text = "", row = 2, column = 0)
        self.summaryValue  = self.addTextArea(text = "", row = 3, column = 0)
        self.readBtn = self.addButton(text = "Select File", row = 0, column = 0, command = self.importFile)
        self.imageLabel = self.addLabel(text = "", row = 5, column = 0, sticky = "NSEW")
        font = Font(family = "Courier", weight = "normal")
        self.summaryValue["font"] = font
        self.outputArea["font"] = font
        self.imageName = "newPlot.png" #image name for the scatter plot

    def importFile(self): #function to read in file from the user's system
        inputFile =  tkinter.filedialog.askopenfilename(parent = self, filetypes = (("CSV Files","*.csv"),))
        if inputFile != "": #checks if user selected a file
            with open(inputFile, encoding='utf-8', newline = '') as newFile:
                self.dataSet = pd.read_csv(newFile) #read in selected file
                self.outputArea["state"] = "normal"
                self.outputArea.setText(self.dataSet) #set first text area equal to contents of user's file
                self.outputArea["state"] = "disabled"

    def computeStats(self): #function to compute descriptive statistics
        try:
            message = "Descriptive statistics of " + self.dataSet.columns[1].lower() + ":\n"
            message += "Minimum: " + str(self.dataSet.iloc[:, 1].min()) + "\n" + "Mean: " + \
            str(self.dataSet.iloc[:, 1].mean()) + "\n" + "Mode: " + str(statistics.mode(self.dataSet.iloc[:, 1])) + \
            "\n" + "Sum: " + str(sum(self.dataSet.iloc[:, 1])) \
            + "\n" + "Range: " + str(max(self.dataSet.iloc[:, 1]) - min(self.dataSet.iloc[:, 1]))+ "\n" + "Count: " + \
            str(len(self.dataSet)) + "\n" + "Median: " + str(self.dataSet.iloc[:, 1].median()) + "\n" + "Maximum: " + \
            str(self.dataSet.iloc[:, 1].max()) + "\n" + "Variance:" + " " + str(statistics.variance(self.dataSet.iloc[:, 1]))+ \
            "\n" + "Standard Deviation: " + str(statistics.stdev(self.dataSet.iloc[:, 1])) + "\n" + \
            "Kurtosis: " + str(kurtosis(self.dataSet.iloc[:, 1], bias=False)) + "\n" + "Skewness: " + \
            str(skew(self.dataSet.iloc[:, 1], bias=False)) + "\n\n"
            message += "Descriptive statistics of " + self.dataSet.columns[2].lower() + ":\n"
            message += "Minimum:" + " " + str(self.dataSet.iloc[:, 2].min()) + "\n" + "Mean: " + \
            str(self.dataSet.iloc[:, 2].mean()) + "\n" + "Mode: " + str(statistics.mode(self.dataSet.iloc[:, 2])) + \
            "\n" + "Sum: " + str(sum(self.dataSet.iloc[:, 2])) + "\n" + \
            "Range: " + str(max(self.dataSet.iloc[:, 2]) - min(self.dataSet.iloc[:, 2]))+ "\n" + \
            "Count: " + str(len(self.dataSet)) + "\n" + "Median: " + str(self.dataSet.iloc[:, 2].median()) + "\n" + \
            "Maximum:" + " "+ str(self.dataSet.iloc[:, 2].max()) + "\n" + \
            "Variance:" + " " + str(statistics.variance(self.dataSet.iloc[:, 2])) + "\n" + \
            "Standard Deviation:" + " "+ str(statistics.stdev(self.dataSet.iloc[:, 2])) + "\n" + \
            "Kurtosis: " + str(kurtosis(self.dataSet.iloc[:, 2], bias=False)) + "\n" + "Skewness: " + \
            str(skew(self.dataSet.iloc[:, 2], bias=False))
        except: #raise error if user tries to compute statistics without selecting file
            raise Exception(self.messageBox(title = "Error", message = "An error has occured. Make sure you have" + \
            " selected a valid csv file that contains only numbers in the second and third columns")) from None
        try:
            self.summaryValue["state"] = "normal"            
            self.summaryValue.setText(message) #send the statistics computed to second text area
            self.summaryValue["state"] = "disabled"
        except: #raise exception if any other error occurs.
            raise Exception(self.messageBox(title = "Error", message = "An error has occured. Make sure you have" + \
            " selected a valid csv file that contains only numbers in the second and third columns")) from None
        plt.clf() #clears the current plot, if there's any, to avoid overlaying plots
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.dataSet.iloc[:, 1],self.dataSet.iloc[:, 2]) #get the slope and intercept
        line = slope*self.dataSet.iloc[:, 1]+intercept
        plt.scatter(self.dataSet.iloc[:, [1]], self.dataSet.iloc[:, [2]], color = 'g') #scatter plot function
        plt.plot(self.dataSet.iloc[:, 1], line, 'r', label='Regression line Y={:.2f}x+{:.2f}'.format(slope,intercept))
        plt.xlabel(self.dataSet.columns[1]) #label for x-axis
        plt.ylabel(self.dataSet.columns[2]) #label for y-axis
        plt.title("Scatter plot of " + self.dataSet.columns[2].lower() + " vs " + self.dataSet.columns[1].lower()) #plot title
        plt.legend(loc = 2) #this creates the legend and sets the location to the upper left corner
        plt.savefig(self.imageName) #save plot as image
        self.imageFile = ImageTk.PhotoImage(Image.open(self.imageName)) #access the image saved
        self.imageLabel["image"] = self.imageFile #set image attribute of label created to the image saved.
        self.readBtn["text"] = "Select another file"
def main():
    DataAnalytics().mainloop()
if __name__ == "__main__":
    main()
print("Created by", __author__) #Joseph Ajayi

