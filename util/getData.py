import pandas as pd
from util.optimize import optimize


def getDataTest(colNames=None):
    y2004 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2004.csv", encoding='latin-1'))
    if colNames == None:
        return y2004
    else:
        return y2004[colNames]
    

def getData(colNames=None, skip=[None]):
    y1987 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1987.csv"))       
    y1988 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1988.csv"))
    y1989 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1989.csv"))
    y1990 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1990.csv"))
    y1991 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1991.csv"))
    y1992 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1992.csv"))
    y1993 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1993.csv"))
    y1994 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1994.csv"))
    y1995 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1995.csv"))
    y1996 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1996.csv"))
    y1997 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1997.csv"))
    y1998 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1998.csv"))
    y1999 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/1999.csv"))
    y2000 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2000.csv"))
    y2001 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2001.csv", encoding='latin-1'))
    y2002 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2002.csv", encoding='latin-1'))
    y2003 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2003.csv", encoding='latin-1'))
    y2004 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2004.csv", encoding='latin-1'))
    y2005 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2005.csv", encoding='latin-1'))
    y2006 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2006.csv", encoding='latin-1'))
    y2007 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2007.csv", encoding='latin-1'))
    y2008 = pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/DaneDecompress/2008.csv", encoding='latin-1'))
    
    if colNames == None:
        return pd.concat([y1987, y1988, y1989, y1990, y1991, y1992, y1993, y1994, y1995, y1996, y1997, y1998, y1999, y2000, y2001, y2002, y2003, y2004, y2005, y2006, y2007, y2008])
    else:
        y1987 = y1987[colNames]
        y1988 = y1988[colNames]
        y1989 = y1989[colNames]
        y1990 = y1990[colNames]
        y1991 = y1991[colNames]
        y1992 = y1992[colNames]
        y1993 = y1993[colNames]
        y1994 = y1994[colNames]
        y1995 = y1995[colNames]
        y1996 = y1996[colNames]
        y1997 = y1997[colNames]
        y1998 = y1998[colNames]
        y1999 = y1999[colNames]
        y2000 = y2000[colNames]
        y2001 = y2001[colNames]
        y2002 = y2002[colNames]
        y2003 = y2003[colNames]
        y2004 = y2004[colNames]
        y2005 = y2005[colNames]
        y2006 = y2006[colNames]
        y2007 = y2007[colNames]
        y2008 = y2008[colNames]
        
        return pd.concat([y1987, y1988, y1989, y1990, y1991, y1992, y1993, y1994, y1995, y1996, y1997, y1998, y1999, y2000, y2001, y2002, y2003, y2004, y2005, y2006, y2007, y2008])  
    
def getAirports():
    return pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/Dane/airports.csv"))

def getCarriers():
    return pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/Dane/carriers.csv"))

def getPlaneData():
    return pd.DataFrame(pd.read_csv("C:/PDW/Projekt2/Dane/plane-data.csv"))