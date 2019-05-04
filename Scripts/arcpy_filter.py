# Performing a low/high pass filter on a raster
#
# Syntax: Filter (in_raster, {filter_type}, {ignore_nodata})
# ----------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# filterOut = Filter("TMI_100m.tif", "HIGH", "NODATA")
# filterOut.save("D:/Python/Test/Raster/TMI_high.tif")
# ----------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# inRaster = "TMI_100m.tif"
#
# filterOut = Filter(inRaster, "LOW", "NODATA")
# filterOut.save("D:/Python/Test/Raster/TMI_low.tif")
# ---------------------------------------------------
# Calculating a statistic of the values within a specified neighborhood around each input cell location
#
# Syntax: FocalStatistics (in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})
# ---------------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outFocalStat = FocalStatistics("TMI_100m.tif", NbrRectangle(9, 9, "CELL"),
#                                "STD", "NODATA")
# outFocalStat.save("D:/Python/Test/Raster/TMI_std.tif")
# ------------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "D:/Python/Test/Raster"

inRaster = "TMI_100m.tif"
neighborhood = NbrRectangle(9, 9, "CELL")

outFocalStatistics = FocalStatistics(inRaster, neighborhood, "MEAN", "NODATA")
outFocalStatistics.save("D:/Python/Test/Raster/TMI_mean.tif")
