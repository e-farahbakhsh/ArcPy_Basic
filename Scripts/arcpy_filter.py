# Performing a low/high pass filter on a raster
#
# Syntax: Filter (in_raster, {filter_type}, {ignore_nodata})
# ----------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# filterOut = Filter("fileName", "HIGH", "NODATA")
# filterOut.save("path")
# ----------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# inRaster = "fileName"
#
# filterOut = Filter(inRaster, "LOW", "NODATA")
# filterOut.save("path")
# ----------------------
# Calculating a statistic of the values within a specified neighborhood around each input cell location
#
# Syntax: FocalStatistics (in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})
# ---------------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# outFocalStat = FocalStatistics("fileName", NbrRectangle(9, 9, "CELL"),
#                                "STD", "NODATA")
# outFocalStat.save("path")
# -------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "path"

inRaster = "fileName"
neighborhood = NbrRectangle(9, 9, "CELL")

outFocalStatistics = FocalStatistics(inRaster, neighborhood, "MEAN", "NODATA")
outFocalStatistics.save("path")
