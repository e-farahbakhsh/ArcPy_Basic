# Selecting by attribute

# Syntax: SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})
# ----------------------------------------------------------------------------------------------
# import arcpy
# arcpy.env.workspace = "D:/Python/Test/Vector"
# arcpy.MakeFeatureLayer_management("Geology_StudyArea.shp", "Geology_StudyArea_Layer")
# arcpy.SelectLayerByAttribute_management("Geology_StudyArea_Layer", "NEW_SELECTION", "Geo_unit = 'Ev'")
# arcpy.CopyFeatures_management("Geology_StudyArea_Layer", "Geology_StudyArea_Layer_Ev")
# ------------------------------------------------------------------------------------
# Selecting by location

# Syntax: SelectLayerByLocation_management (in_layer, {overlap_type}, {select_features}, {search_distance},
#                                          {selection_type}, {invert_spatial_relationship})
# -----------------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "D:/Python/Test/Vector"
arcpy.MakeFeatureLayer_management("Mineralization_StudyArea.shp", "Mineralization_StudyArea_Layer")
arcpy.SelectLayerByLocation_management("Mineralization_StudyArea_Layer", "INTERSECT", "Geology_StudyArea_Layer_Ev.shp")
arcpy.CopyFeatures_management("Mineralization_StudyArea_Layer", "Mineralization_StudyArea_Layer_Ev")
