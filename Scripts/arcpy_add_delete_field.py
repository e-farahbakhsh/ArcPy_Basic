# Adding new fields

# Syntax: AddField_management (in_table, field_name, field_type, {field_precision},\
#                             {field_scale}, {field_length}, {field_alias}, {field_is_nullable},\
#                             {field_is_required}, {field_domain})
# ----------------------------------------------------------------
# Python window

# import arcpy
# arcpy.env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python"
# arcpy.AddField_management("Geology_StudyArea.shp", "test", "TEXT", "", "", 50, "test_alias", "NULLABLE")
# --------------------------------------------------------------------------------------------------------
# Stand-alone script

# import arcpy
# arcpy.env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python"
# in_table1 = "Geology_StudyArea.shp"
# field_name1 = "test"
# field_precision1 = 9
# field_length1 = 50
# field_alias1 = "test_alias"
#
# arcpy.AddField_management(in_table1, field_name1, "TEXT", field_length = field_length1, field_alias=field_alias1,
#                           field_is_nullable="NULLABLE")
# -------------------------------------------------------
# Deleting fields

# Syntax: DeleteField_management (in_table, drop_field)
# -----------------------------------------------------
# Python window

# import arcpy
# arcpy.env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python"
# Copy1 = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python/Geology_StudyArea_Copy.shp"
# Syntax: CopyFeatures_management(in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2},
#                                {spatial_grid_3})
# arcpy.CopyFeatures_management("Geology_StudyArea.shp", Copy1)
# arcpy.DeleteField_management(Copy1, ["test"])
# -------------------------------------------
# Stand-alone script

import arcpy
arcpy.env.workspace = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python"
inFeatures = "Geology_StudyArea.shp"
outFeatureClass = "D:/PhD-AUT/Thesis/Phase 01_Regional Scale/Geology/Python/Geology_StudyArea_Copy.shp"
dropFields = ["test"]

arcpy.CopyFeatures_management(inFeatures, outFeatureClass)
arcpy.DeleteField_management(outFeatureClass, dropFields)
