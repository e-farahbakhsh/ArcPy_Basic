# Calculating cross-tabulated areas between two datasets
#
# Syntax: TabulateArea (in_zone_data, zone_field, in_class_data, class_field, out_table, {processing_cell_size})
# --------------------------------------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test"
# TabulateArea("Vector/Geology_StudyArea.shp", "Geo_unit", "Raster/U_Reclassified.tif", "VALUE",
#              "D:/Python/Test/Table/table01.dbf", 250)
# -----------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "D:/Python/Test"
env.extent = "Vector/Frame.shp"
env.snapRaster = "Vector/Frame.shp"

inZoneData = "Vector/Geology_StudyArea.shp"
zoneField = "Geo_unit"
inClassData = "Raster/U_Reclassified.tif"
classField = "VALUE"
outTable = "D:/Python/Test/Table/table01.dbf"
processingCellSize = 250

TabulateArea(inZoneData, zoneField, inClassData, classField, outTable, processingCellSize)
