from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import yaml
january = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-01.csv', sep = ',', low_memory=False)
february = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-02.csv', sep = ',', low_memory=False)
march = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-03.csv', sep = ',', low_memory=False)
april = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-04.csv', sep = ',', low_memory=False)
may = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-05.csv', sep = ',', low_memory=False)
june = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-06.csv', sep = ',', low_memory=False)
july = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-07.csv', sep = ',', low_memory=False)
august = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-08.csv', sep = ',', low_memory=False)
september = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-09.csv', sep = ',', low_memory=False)
oktober = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-10.csv', sep = ',', low_memory=False)
november = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-11.csv', sep = ',', low_memory=False)
december = pd.read_csv(r'..\trip-data\2018\yellow_tripdata_2018-12.csv', sep = ',', low_memory=False)
year = [january,february,march,april,may,june,july,august,september,oktober,november,december]
bronx = [3,18,20,31,32,46,47,51,58,59,60,69,78,81,94,119,126,136,147,159,167,168,169,174,182,183,184,
        185,199,200,208,212,213,220,235,240,241,242,247,248,250,254,259]
brooklyn = [11,14,17,21,22,25,26,29,33,34,35,36,37,39,40,49,52,54,55,61,62,63,65,66,67,71,72,76,77,
            80,85,89,91,97,106,108,111,112,123,133,149,150,154,154,155,165,177,178,181,188,189,190,
            195,210,217,222,225,227,228,255,256,257]
manhatten = [4,12,13,24,41,42,43,45,48,50,68,74,75,79,87,88,90,100,103,104,105,107,113,114,116,120,
            125,127,128,137,140,141,142,143,144,148,151,152,153,158,161,162,163,164,166,170,186,194,
            202,209,211,224,229,230,231,232,233,234,236,237,238,239,243,244,246,249,261,262,263]
queens = [2,7,8,9,10,15,16,19,27,28,30,38,53,56,57,64,70,73,82,83,86,92,93,95,96,98,101,102,117,121,
            122,124,129,130,131,132,134,135,138,139,145,146,157,160,171,173,175,179,179,180,191,192,
          193,196,198,201,203,205,207,215,216,218,219,223,226,252,253,258,260]
staten_island = [5,6,23,44,84,99,109,110,115,118,156,172,176,187,204,206,212,214,245,251]
districts = [bronx, brooklyn, manhatten, queens, staten_island]
airports = [132, 138]
month_labels = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER',
                'OKTOBER','NOVEMBER','DECEMBER']
district_labels = ['BRONX', 'BROOKLYN', 'MANHATTEN', 'QUEENS', 'STATEN ISLAND']
tip_labels = ['AVERAGE', 'LOWER', 'UPPER']
airport_labels = ['JFK AIRPORT', 'LA GUARDIA AIRPORT']
airport_directions = ['FROM AIRPORTS', 'TO AIRPORTS']
district_colors = ['darkgray', 'lightskyblue', 'tomato', 'gold', 'plum']
airport_colors = ['gold', 'tomato']
direction = ['FROM', 'TO']