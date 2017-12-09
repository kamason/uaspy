# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:10:16 2017

@author: kmason
"""

#Normalize FLIR photos the same
from libtiff import TIFFimage
from skimage.io import imread
from osgeo import gdal
import numpy
import os

#put directory of images here
folder = "E:\Workspace\FLIR Test 07072017\UAV data"
savefolder = "E:\Workspace\FLIR Test 07072017\Normalized Images Python"

def normalize(image,minall,maxall):
    floatimg = image.astype(float)
    #converts 16bit numpy array to float
    normalimg = ((floatimg - minall) / (maxall-minall))*65535
    #normalizes image to between 0 and 1 and then to 16 bit range
    newimage = normalimg.astype(numpy.uint16)
    #changes image back from float to 16bit
    return newimage

listmax = []
#blank list for appending max values of images
listmin = []
#blank list for appending min values of images

for image in os.listdir(folder):
    #changing working directory to where images are
    os.chdir(folder)
    #open image
    t = gdal.Open(image)
    #convert image to numpyarray
    numpyimg = numpy.array(t.GetRasterBand(1).ReadAsArray())
    #find min of image
    minx = numpy.amin(numpyimg)
    #find max of image
    maxx = numpy.amax(numpyimg)
    #append to lists
    listmax.append(maxx)
    listmin.append(minx)

#find max of all images and min of all images for normalization to make sure all images are stretched the same
maxall = max(listmax)
minall = min(listmin)

for image in os.listdir(folder):
    #changing working directory to location where images are
    os.chdir(folder)
    #open image
    t = gdal.Open(image)
    #convert to numpyarray
    numpyimg = numpy.array(t.GetRasterBand(1).ReadAsArray())
    #normalize image
    norm = normalize(numpyimg, minall, maxall)
    #change directory to save folder
    os.chdir(savefolder)
    #save new image as 16bit tiff
    newimg = TIFFimage(norm,description='')
    newimg.write_file(image,compression='lzw')