# Overlaying several rasters, multiplying each by their given weight and summing them together
#
# Syntax: WeightedSum (in_rasters)
# --------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# outWeightedSum = WeightedSum(WSTable([["fileName1", "VALUE", 0.5], ["fileName2", "VALUE", 0.5]]))
# outWeightedSum.save("path1")
# -----------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# inRaster1 = "fileName1"
# inRaster2 = "fileName2"
# WSumTableObj = WSTable([[inRaster1, "VALUE", 0.5], [inRaster2, "VALUE", 0.5]])
#
# outWeightedSum = WeightedSum(WSumTableObj)
# outWeightedSum.save("path1")
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
# env.workspace = "path"
#
# outsuit = WeightedOverlay(WOTable([["fileName1", 50, 'VALUE', RemapValue([[1, 2], [2, 3], [3, 4], ["NODATA", "NODATA"]])],
# 								   ["fileName2", 50, 'VALUE', RemapValue([[1, 2], [2, 3], [3, 4], [4, 5], ["NODATA", "NODATA"]])]],
# 								  [1, 9, 1]))
# outsuit.save("path1")
# ----------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "path"

inRaster1 = "fileName1"
inRaster2 = "fileName2"

remap1 = RemapValue([[1, 2], [2, 3], [3, 4], ["NODATA", "NODATA"]])
remap2 = RemapValue([[1, 2], [2, 3], [3, 4], [4, 5], ["NODATA", "NODATA"]])

myWOTable = WOTable([[inRaster1, 50, "VALUE", remap1],
                     [inRaster2, 50, "VALUE", remap2]], [1, 9, 1])
outWeightedOverlay = WeightedOverlay(myWOTable)
outWeightedOverlay.save("path1")
