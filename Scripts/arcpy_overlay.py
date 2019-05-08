# Overlaying several rasters, multiplying each by their given weight and summing them together
#
# Syntax: WeightedSum (in_rasters)
# --------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outWeightedSum = WeightedSum(WSTable([["Th_UTM40N.tif", "VALUE", 0.5], ["U_UTM40N.tif", "VALUE", 0.5]]))
# outWeightedSum.save("D:/Python/Test/Raster/Th_U.tif")
# -----------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# inRaster1 = "Th_UTM40N.tif"
# inRaster2 = "U_UTM40N.tif"
# WSumTableObj = WSTable([[inRaster1, "VALUE", 0.5], [inRaster2, "VALUE", 0.5]])
#
# outWeightedSum = WeightedSum(WSumTableObj)
# outWeightedSum.save("D:/Python/Test/Raster/Th_U.tif")
# -----------------------------------------------------
# Overlaying several rasters using a common measurement scale and weighting each according to its importance
#
# Syntax: WeightedOverlay (in_weighted_overlay_table)
# ---------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outsuit = WeightedOverlay(WOTable([["Th_Reclassified.tif", 50, 'VALUE', RemapValue([[1, 2], [2, 3], [3, 4], ["NODATA", "NODATA"]])],
# 								   ["U_Reclassified.tif", 50, 'VALUE', RemapValue([[1, 2], [2, 3], [3, 4], [4, 5], ["NODATA", "NODATA"]])]],
# 								  [1, 9, 1]))
# outsuit.save("D:/Python/Test/Raster/Th_U.tif")
# ----------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "D:/Python/Test/Raster"

inRaster1 = "Th_Reclassified.tif"
inRaster2 = "U_Reclassified.tif"

remap1 = RemapValue([[1, 2], [2, 3], [3, 4], ["NODATA", "NODATA"]])
remap2 = RemapValue([[1, 2], [2, 3], [3, 4], [4, 5], ["NODATA", "NODATA"]])

myWOTable = WOTable([[inRaster1, 50, "VALUE", remap1],
                     [inRaster2, 50, "VALUE", remap2]], [1, 9, 1])
outWeightedOverlay = WeightedOverlay(myWOTable)
outWeightedOverlay.save("D:/Python/Test/Raster/Th_U.tif")
