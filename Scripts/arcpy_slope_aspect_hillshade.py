# Identifies the slope from each cell of a raster

# Syntax: Slope (in_raster, {output_measurement}, {z_factor}, {method}, {z_unit})
# -------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outSlope = Slope("ASTER_UTM40N.tif", "DEGREE")
# outSlope.save("D:/Python/Test/Raster/ASTER_slope.tif")
# ------------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# inRaster = "ASTER_UTM40N.tif"
# outMeasurement = "DEGREE"
# zFactor = ""
# method = "GEODESIC"
# zUnit = "FOOT"
#
# outSlope = Slope(inRaster, outMeasurement, zFactor, method, zUnit)
# outSlope.save("D:/Python/Test/Raster/ASTER_slope.tif")
# ------------------------------------------------------
# Deriving the aspect from each cell of a raster surface
#
# Syntax: Aspect (in_raster, {method}, {z_unit})
# ----------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outAspect = Aspect("ASTER_UTM40N.tif")
# outAspect.save("D:/Python/Test/Raster/ASTER_aspect.tif")
# --------------------------------------------------------
# Stand-alone script
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# inRaster = "ASTER_UTM40N.tif"
# method = "GEODESIC"
# zUnit = "FOOT"
#
# outAspect = Aspect(inRaster, method, zUnit)
# outAspect.save("D:/Python/Test/Raster/ASTER_aspect.tif")
# --------------------------------------------------------
# Creating a shaded relief from a surface raster
#
# Syntax: Hillshade (in_raster, {azimuth}, {altitude}, {model_shadows}, {z_factor})
# ---------------------------------------------------------------------------------
# Python window
#
# import arcpy
# from arcpy import env
# from arcpy.sa import *
# env.workspace = "D:/Python/Test/Raster"
#
# outHillshade = Hillshade("ASTER_UTM40N.tif", 180, 75, "SHADOWS", 1)
# outHillshade.save("D:/Python/Test/Raster/ASTER_hillshade.tif")
# --------------------------------------------------------------
# Stand-alone script
#
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "D:/Python/Test/Raster"

inRaster = "ASTER_UTM40N.tif"
azimuth = 180
altitude = 75
modelShadows = "SHADOWS"
zFactor = 1

outHillShade = Hillshade(inRaster, azimuth, altitude, modelShadows, zFactor)
outHillShade.save("D:/Python/Test/Raster/ASTER_hillshade.tif")
