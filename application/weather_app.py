from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer
from datetime import datetime
import sys
import data

class Weather(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setHorizontalSpacing(50)

        #Store labels after init_data() (initialization) so that
        #it would be easier to update data using setText
        self.daily_labels = {}
        self.hourly_labels = {}

        self.init_data() #call init_data which initizalizes all the labels

        self.data_hour = datetime.now().time().hour         #get the hour upon initialization
        self.timer = QTimer(self)                           #set a timer
        self.timer.timeout.connect(self.watch_hour_change)  #set an action if timer timeouts
        self.timer.start(5000)                              #set timer to 5s

    def watch_hour_change(self):                            #checks if the hour change in real time
        current_hour = datetime.now().time().hour           #get the current hour
        if current_hour != self.data_hour:                  #check if hour the data is based is equal to the current hour
            self.data_hour = current_hour
            self.refresh_data()                             #if not, data should be refreshed by calling refresh_data

    def init_data(self):
        # Day data
        day_data_section = QLabel("Update Today")           #initialize a label day_data_section
        self.grid_layout.addWidget(
            day_data_section, 0, 0, 1, 1,                   #add a widget which places the label "Update Today" in row 0 and column 1
            alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignCenter)

        daily_data = data.get_daily_update()                #get data from data.py
        daily_data_list = data.daily_data_list()            #get name: key pair of data for daily_data

        if daily_data[0] == False:                          #if there was an error in the request, simply return "Error" and the status code as
                                                            #a value for each data. (Example: Temperature: Error[500])
            for i, data_name_key in enumerate(daily_data_list):
                data_name = data_name_key[0]
                data_key  = data_name_key[1]
                label = QLabel("{:<26}: {:>25}".format(data_name, "Error[" + hourly_data[1] + "]"))
                self.grid_layout.addWidget(
                        label, 
                        i+1, 
                        0,
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
                    )
                self.daily_labels[label] = (data_name, data_key)
        else:                                                           #if there was no error get data and display the values
            for i, data_name_key in enumerate(daily_data_list):         #Note to future self/reader: daily_data_list contains a list of tuple (data_name, data_key)
                data_name = data_name_key[0]                            #self explanatory from the text above
                data_key  = data_name_key[1]
                label = QLabel("{:<26}: {:>25}".format(data_name, str(daily_data[1][data_key]))) #initialize a label
                self.grid_layout.addWidget(                                                      #use the data key to get the value of daily_data[1], if unclear
                                                                                                 #review data.py file
                        label, 
                        i+1,                                                                     #place the data in a row below the "Update today label" and the next below 
                                                                                                 #the current label
                        0,                                                                       #place all of this in column 0
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
                    )
                self.daily_labels[label] = (data_name, data_key)

        # Hourly data (The explanation for this section is similar to the Day data)
        hour_data_section = QLabel("Hourly Update")
        self.grid_layout.addWidget(hour_data_section, 0, 1, 1, 1,
            alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignCenter)

        hourly_data = data.get_hourly_update()
        hourly_data_list = data.hourly_data_list()

        if hourly_data[0] == False:
            for i, data_name_key in enumerate(hourly_data_list):
                data_name = data_name_key[0]
                data_key  = data_name_key[1]
                label = QLabel("{:<26}: {:>25}".format(data_name, "Error[" + hourly_data[1] + "]"))
                self.grid_layout.addWidget(
                        label, 
                        i+1, 
                        1,
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
                    )
                self.hourly_labels[label] = (data_name, data_key)
        else:
            for i, data_name_key in enumerate(hourly_data_list):
                data_name = data_name_key[0]
                data_key  = data_name_key[1]
                label = QLabel("{:<26}: {:>25}".format(data_name, str(hourly_data[1][data_key])))
                self.grid_layout.addWidget(
                        label, 
                        i+1, 
                        1,
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
                    )
                self.hourly_labels[label] = (data_name, data_key)

    def refresh_data(self):
        daily_data = data.get_daily_update()                                                        #get the latest data
        if daily_data[0] == False:                                                                  #if false do the same in init_data if request fails
            for label, (data_name, data_key) in self.daily_labels.items():                     
                label.setText("{:<26}: {:>25}".format(data_name, "Error[" + hourly_data[1] + "]")) 
        else:
            for label, (data_name, data_key) in self.daily_labels.items():                          #iterate through the daily_labels dictionary
                label.setText("{:<26}: {:>25}".format(data_name, str(daily_data[1][data_key])))     #update the label text using setText the data from updated daily_data
            
        hourly_data = data.get_hourly_update()                                                      #same happens here
        if hourly_data[0] == False:
            for label, (data_name, data_key) in self.hourly_labels.items():                     
                label.setText("{:<26}: {:>25}".format(data_name, "Error[" + hourly_data[1] + "]"))
        else:
            for label, (data_name, data_key) in self.hourly_labels.items():
                label.setText("{:<26}: {:>25}".format(data_name, str(hourly_data[1][data_key])))

app = QApplication(sys.argv)
app.setFont(QFont("Courier New", 16))
window = Weather()
window.show()
app.exec()