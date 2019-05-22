# Fuzzy membership
#
# Syntax: FuzzyMembership (in_raster, {fuzzy_function}, {hedge})
# --------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy.sa import *
# from arcpy import env
# env.workspace = "path"
#
# outFzyMember = FuzzyMembership("fileName", FuzzyLarge())
# outFzyMember.save("path1")
# --------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# inRaster = "fileName"
# # midpoint = 15
# # spread = 5
# myFuzzyAlgorithm = FuzzyLarge()
#
# outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)
# outFuzzyMember.save("path1")
# ----------------------------
# Combining fuzzy membership rasters data together
#
# Syntax: FuzzyOverlay (in_rasters, {overlay_type}, {gamma})
# ----------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy.sa import *
# from arcpy import env
# env.workspace = "path"
#
# outFzyOverlay = FuzzyOverlay(["fileName1", "fileName2"], "GAMMA", 0.95)
# outFzyOverlay.save("path1")
# ----------------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "path"

inRasterList = ["fileName1", "fileName2"]
outFzyOverlay = FuzzyOverlay(inRasterList, "GAMMA", 0.75)
outFzyOverlay.save("path1")
