# Identifies the slope from each cell of a raster

# Syntax: Slope (in_raster, {output_measurement}, {z_factor}, {method}, {z_unit})
# -------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# outSlope = Slope("fileName", "DEGREE")
# outSlope.save("path1")
# ----------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# inRaster = "fileName"
# outMeasurement = "DEGREE"
# zFactor = ""
# method = "GEODESIC"
# zUnit = "FOOT"
#
# outSlope = Slope(inRaster, outMeasurement, zFactor, method, zUnit)
# outSlope.save("path1")
# ----------------------
# Deriving the aspect from each cell of a raster surface
#
# Syntax: Aspect (in_raster, {method}, {z_unit})
# ----------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# outAspect = Aspect("fileName")
# outAspect.save("path1")
# -----------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# inRaster = "fileName"
# method = "GEODESIC"
# zUnit = "FOOT"
#
# outAspect = Aspect(inRaster, method, zUnit)
# outAspect.save("path1")
# -----------------------
# Creating a shaded relief from a surface raster
#
# Syntax: Hillshade (in_raster, {azimuth}, {altitude}, {model_shadows}, {z_factor})
# ---------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "path"
#
# outHillshade = Hillshade("fileName", 180, 75, "SHADOWS", 1)
# outHillshade.save("path1")
# --------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "path"

inRaster = "fileName"
azimuth = 180
altitude = 75
modelShadows = "SHADOWS"
zFactor = 1

outHillShade = Hillshade(inRaster, azimuth, altitude, modelShadows, zFactor)
outHillShade.save("path1")
