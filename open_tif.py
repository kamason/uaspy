# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:08:49 2017

@author: kmason
"""

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ds = gdal.Open("DFC_micasense_ortho_NO_radiometric_calibration_GPS_AV_dd84.tif")
channel = np.array(ds.GetRasterBand(1).ReadAsArray())

plt.imshow(channel)
