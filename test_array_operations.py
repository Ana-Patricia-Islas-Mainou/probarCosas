def oneTimeAlgorithm():
    pass

def buildFileLogger():
    pass

def readFileLogger():
    pass

## -------------------------------------------------------------------------------

# nombre de columnas
header= ["t, 12, 13, 14, \n", "t, 12, 13, 14, \n"] # construir con motors[i].ID

# Name of the CSV file
surfaceName = "GRASS"
runName = "TEST1"

fn = "LOGS/" + surfaceName + "/" + runName + "_POSITION.csv";     posFile = open(fn, "w")
fn = "LOGS/" + surfaceName + "/" + runName + "_SPEED.csv";        speFile = open(fn, "w")
fn = "LOGS/" + surfaceName + "/" + runName + "_CURRENT.csv";      curFile = open(fn, "w")
fn = "LOGS/" + surfaceName + "/" + runName + "_VOLTAGE.csv";      volFile = open(fn, "w")
fn = "LOGS/" + surfaceName + "/" + runName + "_TEMPERATURE.csv";  temFile = open(fn, "w")

posFile.writelines(header)

posFile.close()
speFile.close()
curFile.close()
volFile.close()
temFile.close()