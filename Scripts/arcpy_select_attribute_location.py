# Selecting by attribute

# Syntax: SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})
# ----------------------------------------------------------------------------------------------
# import arcpy
# arcpy.env.workspace = "path"
# arcpy.MakeFeatureLayer_management("fileName", "layerName")
# arcpy.SelectLayerByAttribute_management("layerName", "NEW_SELECTION", "fieldName = 'Value'")
# arcpy.CopyFeatures_management("layerName", "fileName1")
# ------------------------------------------------------------------------------------
# Selecting by location

# Syntax: SelectLayerByLocation_management (in_layer, {overlap_type}, {select_features}, {search_distance},
#                                          {selection_type}, {invert_spatial_relationship})
# -----------------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "path"
arcpy.MakeFeatureLayer_management("fileName", "layerName")
arcpy.SelectLayerByLocation_management("layerName", "INTERSECT", "fileName1")
arcpy.CopyFeatures_management("layerName", "fileName2")
