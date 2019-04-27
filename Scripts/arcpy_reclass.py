# Reclassification

# Syntax: Reclassify(in_raster, reclass_field, remap, {missing_values})
# ---------------------------------------------------------------------
# Python window

import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geophysics/Python"
# outReclass1 = Reclassify("fileName", "Value",
#                          RemapValue([[1,9],[2,8],[3,7],[4,6],[5,2],[6,4],[7,3]]))
# outReclass1.save("D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geophysics/Python/filename_reclassified.tif")
#
# outReclass2 = Reclassify("TMI_100m.tif", "Value",
#                          RemapRange([[-3000,-2000,"NODATA"],[-2000,-1000,1],[-1000,0,2],
#                                      [0,1000,3],[1000,2000,4],[2000,3000,5]]))
# outReclass2.save("D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geophysics/Python/TMI_100m_Reclassified.tif")
# ---------------------------------------------------------------------------------------------------------
# Stand-alone script

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geophysics/Python"

inRaster = "TMI_100m.tif"
reclassField = "Value"
remap = RemapValue([[-3000,-2000,"NODATA"],[-2000,-1000,1],[-1000,0,2], [0,1000,3],[1000,2000,4],[2000,3000,5]])
outReclassify = Reclassify(inRaster, reclassField, remap, "NODATA")
outReclassify.save("D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geophysics/Python/TMI_100m_Reclassified.tif")
