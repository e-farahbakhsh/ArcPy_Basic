# Fuzzy membership
#
# Syntax: FuzzyMembership (in_raster, {fuzzy_function}, {hedge})
# --------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy.sa import *
# from arcpy import env
# env.workspace = "D:/Python/Test/Raster"
#
# outFzyMember = FuzzyMembership("U_UTM40N.tif", FuzzyLarge())
# outFzyMember.save("D:/Python/Test/Raster/U_Fuzzy.tif")
# -------------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# inRaster = "Th_UTM40N.tif"
# # midpoint = 15
# # spread = 5
# myFuzzyAlgorithm = FuzzyLarge()
#
# outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)
# outFuzzyMember.save("D:/Python/Test/Raster/Th_Fuzzy.tif")
# ---------------------------------------------------------
# Combining fuzzy membership rasters data together
#
# Syntax: FuzzyOverlay (in_rasters, {overlay_type}, {gamma})
# ----------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy.sa import *
# from arcpy import env
# env.workspace = "D:/Python/Test/Raster"
#
# outFzyOverlay = FuzzyOverlay(["Th_Fuzzy.tif", "U_Fuzzy.tif"], "GAMMA", 0.95)
# outFzyOverlay.save("D:/Python/Test/Raster/Th_U_Gamma.tif")
# ----------------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "D:/Python/Test/Raster"

inRasterList = ["Th_Fuzzy.tif", "U_Fuzzy.tif"]
outFzyOverlay = FuzzyOverlay(inRasterList, "GAMMA", 0.75)
outFzyOverlay.save("D:/Python/Test/Raster/Th_U_Gamma.tif")
