from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import yaml
import os

districts = {
    'bronx': [3, 18, 20, 31, 32, 46, 47, 51, 58, 59, 60, 69, 78, 81, 94, 119, 126, 136, 147, 159,
              167, 168, 169, 174, 182, 183, 184, 185, 199, 200, 208, 212, 213, 220, 235, 240, 241,
              242, 247, 248, 250, 254, 259],
    'brooklyn': [11, 14, 17, 21, 22, 25, 26, 29, 33, 34, 35, 36, 37, 39, 40, 49, 52, 54, 55, 61,
                  62, 63, 65, 66, 67, 71, 72, 76, 77, 80, 85, 89, 91, 97, 106, 108, 111, 112, 123,
                  133, 149, 150, 154, 154, 155, 165, 177, 178, 181, 188, 189, 190, 195, 210, 217,
                  222, 225, 227, 228, 255, 256, 257],
    'manhattan': [4, 12, 13, 24, 41, 42, 43, 45, 48, 50, 68, 74, 75, 79, 87, 88, 90, 100, 103, 104,
                  105, 107, 113, 114, 116, 120, 125, 127, 128, 137, 140, 141, 142, 143, 144, 148,
                  151, 152, 153, 158, 161, 162, 163, 164, 166, 170, 186, 194, 202, 209, 211, 224,
                  229, 230, 231, 232, 233, 234, 236, 237, 238, 239, 243, 244, 246, 249, 261, 262,
                  263],
    'queens': [2, 7, 8, 9, 10, 15, 16, 19, 27, 28, 30, 38, 53, 56, 57, 64, 70, 73, 82, 83, 86, 92,
                93, 95, 96, 98, 101, 102, 117, 121, 122, 124, 129, 130, 131, 132, 134, 135, 138,
                139, 145, 146, 157, 160, 171, 173, 175, 179, 179, 180, 191, 192, 193, 196, 198,
                201, 203, 205, 207, 215, 216, 218, 219, 223, 226, 252, 253, 258, 260],
    'staten_island': [5, 6, 23, 44, 84, 99, 109, 110, 115, 118, 156, 172, 176, 187, 204, 206, 212,
                      214, 245, 251]
}

airports = [132, 138]

month_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
district_labels = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
airport_labels = ['JFK Airport', 'LaGuardia Airport']
tip_labels = ['average', 'lower', 'upper']

directions = ['from', 'to']
airport_directions = ['from airports', 'to airports']

district_colors = ['darkgray', 'lightskyblue', 'tomato', 'gold', 'plum']
airport_colors = ['gold', 'tomato']

year = []
for month in range(1, 13):
  file_path = os.path.join('..', 'trip-data', '2018', f'yellow_tripdata_2018-{str(month).zfill(2)}.csv')
  year.append(pd.read_csv(file_path, sep=',', low_memory=False))