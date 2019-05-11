# Calculating cross-tabulated areas between two datasets
#
# Syntax: TabulateArea (in_zone_data, zone_field, in_class_data, class_field, out_table, {processing_cell_size})
# --------------------------------------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# TabulateArea("fileName1", "field1", "fileName2", "field2",
#              "path1", 250)
# -----------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "path"
env.extent = "fileName1"
env.snapRaster = "fileName2"

inZoneData = "fileName3"
zoneField = "field1"
inClassData = "fileName4"
classField = "field2"
outTable = "path1"
processingCellSize = 250

TabulateArea(inZoneData, zoneField, inClassData, classField, outTable, processingCellSize)
