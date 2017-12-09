# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:39:27 2017

@author: kmason
"""
import cv2
import numpy as np
import os
#Performing a vignette correction on images from sony a7r 35mm sony lens

#Import panel images and images to be corrected
#rawpanelpath = 'F:\Workspace\Vignette Corrections for Mark\Sony_a7R_21mm_voightlander\DSC02818.ARW'
#rawimagepath = 'F:\Workspace\Vignette Corrections for Mark\test_images_fort_laramie\DSC02406.ARW'
jpgpanel = 'F:\Workspace\Vignette Corrections for Mark\Sony_a7R_21mm_voightlander\DSC02816.JPG'
jpgimagesfolder = ['T:\ProjectWorkspace\UAS\Missions\Active\WY_Ft_Laramie_NPS_LIDAR_Nell_Conti\data\UAV_data\Photo_Survey_East_flight3',
                  'T:\ProjectWorkspace\UAS\Missions\Active\WY_Ft_Laramie_NPS_LIDAR_Nell_Conti\data\UAV_data\Photo_Survey_East_redo_flight8',
                   'T:\ProjectWorkspace\UAS\Missions\Active\WY_Ft_Laramie_NPS_LIDAR_Nell_Conti\data\UAV_data\Photo_Survey_Mid_flight7',
                  'T:\ProjectWorkspace\UAS\Missions\Active\WY_Ft_Laramie_NPS_LIDAR_Nell_Conti\data\UAV_data\Photo_Survey_Mid_flight9',
                   'T:\ProjectWorkspace\UAS\Missions\Active\WY_Ft_Laramie_NPS_LIDAR_Nell_Conti\data\UAV_data\Photo_Survey_Mid_flight10']
#jpgimagesfolder = ['F:\Workspace\Vignette Corrections for Mark\Test']
savedir = 'F:\Workspace\Vignette Corrections for Mark\Test'
#rawimagename = 'test.tiff'

#for jpgs
panel_jpg = cv2.imread(jpgpanel)
vignette1 = panel_jpg[:,:,0]
vignette2 = panel_jpg[:,:,1]
vignette3 = panel_jpg[:,:,2]

#Perform low-pass filter on panel image
lowpasskernel = np.ones((501,501),np.float32)/251001
#dstraw = cv2.filter2D(panel_raw,-1,lowpasskernel)
dstjpg1 = cv2.filter2D(vignette1,-1,lowpasskernel)
dstjpg2 = cv2.filter2D(vignette2,-1,lowpasskernel)
dstjpg3 = cv2.filter2D(vignette3,-1,lowpasskernel)

#Divide all pixels by the max value. 
#vignettemodelraw = dstraw / dstraw.max()
vignettemodeljpg1 = dstjpg1.astype(float) / dstjpg1.max()
vignettemodeljpg2 = dstjpg2.astype(float) / dstjpg2.max()
vignettemodeljpg3 = dstjpg3.astype(float) / dstjpg3.max()

#for raw
#with rawpy.imread(rawpanelpath) as raw:
   # panel_raw = raw.postprocess()

#Find the max value and make sure it isn't over saturated
maxpanel = panel_jpg.max()

d = 0
while d < len(jpgimagesfolder):
    for file in os.listdir(jpgimagesfolder[d]):
        if file[-3:]=='JPG':
            #open image for correcting
            path = os.path.join(jpgimagesfolder[d],file)
            image_jpg = cv2.imread(path)
            jpgcorrname = file
            #with rawpy.imread(rawimagepath) as raw:
                #image_raw = raw.postprocess()
           
            #Divide images to be corrected by vignette correction array
            #corrimageraw = image_raw /vignettemodelraw
            corrimagejpg_1 = image_jpg[:,:,0]/ vignettemodeljpg1
            corrimagejpg_2 = image_jpg[:,:,1]/ vignettemodeljpg2
            corrimagejpg_3 = image_jpg[:,:,2]/ vignettemodeljpg3
            
            maximage = max(corrimagejpg_1.max(), corrimagejpg_2.max(),corrimagejpg_3.max())
            corrimagejpg_1 = (corrimagejpg_1/maximage)*256
            corrimagejpg_2 = (corrimagejpg_2/maximage)*256
            corrimagejpg_3 = (corrimagejpg_3/maximage)*256
            
            corrimagejpg = np.dstack((corrimagejpg_1,corrimagejpg_2,corrimagejpg_3))
            
            os.chdir(savedir)
            savefolder = os.path.join(savedir,jpgimagesfolder[d].split('\\')[-1:][0])
            if not os.path.exists(savefolder):
                os.mkdir(savefolder)
            os.chdir(savefolder)
            #img = PIL.Image.fromarray(corrimageraw, mode=None)
            #img.save(rawimagename)
            cv2.imwrite(jpgcorrname,corrimagejpg)
    d = d + 1