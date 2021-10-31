#initializing
import os
import tkinter
from flask import Flask, render_template,url_for
#import jyserver.Flask as jsf

# FLASK NONSENSE
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('buildings.html')

# THE BUILDING OBJECT
class Building:
  BLDG_NAME = ""
  NUMFLOORS = 0
  busynessList = [[0]]

  # Initializes the building's name and floors
  def __init__(self, name="N/A", floors = 0):
    self.BLDG_NAME = name
    self.NUMFLOORS = floors
    self.makeBusynessList()
  
  # Adds the user's busyness value to a list for a given building floor
  def addBusyNum(self, floor= 2, busyNum = 0):
    rFloor = floor - 1
    for i in range(len(self.busynessList[floor])):
      if self.busynessList[rFloor][i] == 0:
        self.busynessList[rFloor][i] = busyNum
        break
      elif i == len(self.busynessList[floor]) - 1:
        self.busynessList[rFloor].append(busyNum)
        break
  
  # Constructs the base lists we'll be using to store density values
  def makeBusynessList(self):
    arr = [[0]]
    for i in range(self.NUMFLOORS - 1):
      arr.append([0])
    self.busynessList = arr

  # Removes the first index of the list of a given floor
  def removeValue(self, floor = 2):
    self.busynessList[floor - 1].pop(0)

  # Gets the average of all values on a floor
  def getAverage(self, floor = 2):
    values = len(self.busynessList)
    average = 0
    rFloor = floor - 1
    if values != 0:
      total = 0
      for busyNum in self.busynessList[rFloor]:
          total += busyNum
      average = total / len(self.busynessList)
    return average

#print("PCL INFO_____________")
PCL = Building("PCL", 6)
GDC = Building("GDC", 8)
SAC = Building("SAC", 5)

buildings = [PCL, GDC, SAC]

#@jsf.use(app)
#class App:
#  def __init__(self):
#   self.PCL = "PCL"
#    self.GDC = "GDC"
#    self.SAC = "SAC"

#  def setBuilding(self):
#    self.my_building = self.js.event.target.id

if __name__ == '__main__':
  app.run(debug=True)