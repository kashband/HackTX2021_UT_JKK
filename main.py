#initializing
import os
import tkinter
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
#import jyserver.Flask as jsf

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

    for i in range(len(self.busynessList[rFloor])):

      if self.busynessList[rFloor][i] == 0:
        self.busynessList[rFloor][i] = busyNum
        break
      elif i == len(self.busynessList[rFloor]) - 1:
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
    rFloor = floor - 1
    floorValues = len(self.busynessList[rFloor])
    average = 0
    
    if floorValues > 0:
      total = 0
      for busyNum in self.busynessList[rFloor]:
        total += float(busyNum)
      average = total / floorValues
      return average
    return self.busynessList[rFloor][0]

  # Return all values of a given floor as a string
  def floorValues(self, floor = 1):
    rFloor = floor - 1
    valString = "[" + str(self.busynessList[rFloor][0])
    
    if (len(self.busynessList[rFloor]) > 0):
      for index in range(len(self.busynessList[rFloor]) - 1):
        valString = valString + ", " + str(self.busynessList[rFloor][index + 1])

    return self.BLDG_NAME + str(floor) + ": " + valString + "]"

#print("PCL INFO_____________")
PCL = Building("PCL", 6)
GDC = Building("GDC", 8)
SAC = Building("SAC", 5)

BLDG_SET = [PCL, GDC, SAC]

def getBuilding(bldg_name):
  for bldg in BLDG_SET:
    if bldg_name == bldg.BLDG_NAME:
      return bldg

# FLASK NONSENSE
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///.db'
db = SQLAlchemy(app)

# Upon bootup this is the main page, redirects to building page
@app.route('/')
def index():
    return redirect(url_for("buildingPage"))

# Page where user chooses their building
@app.route('/building', methods=["POST", "GET"])
def buildingPage():
  if request.method == "POST":
    bldg = request.form['buttonBldg']
    return redirect(url_for("floorPage", bldgName= bldg))
  else:
    return render_template('building.html')

# Page where user chooses the floor they want to see of a Building
@app.route('/floors.html/<bldgName>', methods=["POST", "GET"])
def floorPage(bldgName):
  if request.method == "POST":
    level = request.form['levelBtn']
    return redirect(url_for("busyPage", bldgName = bldgName, floor = level))
  else:
    currentBldg = getBuilding(bldgName)
    floors = currentBldg.NUMFLOORS
    return render_template('floors.html', content=bldgName, floorNums=floors)

# Page where user views or enters their own "busyness" stats
@app.route('/status.html/<bldgName><floor>', methods=["POST", "GET"])
def busyPage(bldgName, floor):
  currentBldg = getBuilding(bldgName)
  average = round(currentBldg.getAverage(int(floor)), 2)

  if request.method == "POST":
    myNum= request.form['busyness']
    
    currentBldg.addBusyNum(int(floor), myNum)
    average = round(currentBldg.getAverage(int(floor)), 2)

    return render_template('status.html', thisBuilding=bldgName, thisFloor=floor, currentAverage=average)
  else:
    return render_template('status.html', thisBuilding=bldgName, thisFloor=floor, currentAverage=average)

if __name__ == '__main__':
  app.run(debug=True)