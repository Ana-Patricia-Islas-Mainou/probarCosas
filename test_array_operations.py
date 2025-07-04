def oneTimeAlgorithm():
    pass

def buildFileLogger(surfaceName, runName):
    # nombre de columnas
    header= ["t, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\n"] # construir con motors[i].ID

    fn = "LOGS/" + surfaceName + "/" + runName + "_POSITION.csv";     posFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_SPEED.csv";        speFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_CURRENT.csv";      curFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_VOLTAGE.csv";      volFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_TEMPERATURE.csv";  temFile = open(fn, "w")

    posFile.writelines(header)
    speFile.writelines(header)
    curFile.writelines(header)
    volFile.writelines(header)
    temFile.writelines(header)

    return posFile, speFile, curFile, volFile, temFile

def closeFileLogger(files):
    for i in range(0,len(files)):
        files[i].close()

def writeToFIle(filename, data):
    filename.writelines(data)

def readFileLogger():
    pass


def bits2radSec_DataFrame(bits):
    return bits * 0.229 * 0.1047 # bits -> rpm * rmp -> rad/s

def bits2mA_DataFrame(bits):
    return bits.multiply(3.36) # bits -> mA 

def bits2volts_DataFrame(bits):
    return bits * 0.1 # bits -> V

def bits2tep_DataFrame(bits):
    return bits * 1 # bits -> grados celcius 

## -------------------------------------------------------------------------------

# Name of the CSV file
surfaceName = "FLAT"
runName = "TEST1"

#posFile, speFile, curFile, volFile, temFile = buildFileLogger(surfaceName, runName)
#files = [posFile, speFile, curFile, volFile, temFile]

#writeToFIle(posFile, "t, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\n")

#closeFileLogger(files)
