# Adding new fields
#
# Syntax: AddField_management(in_table, field_name, field_type, {field_precision},\
#                            {field_scale}, {field_length}, {field_alias}, {field_is_nullable},\
#                            {field_is_required}, {field_domain})
# ---------------------------------------------------------------
# Python window
#
# import arcpy
# arcpy.env.workspace = "path"
# arcpy.AddField_management("fileName", "test", "TEXT", "", "", 50, "test_alias", "NULLABLE")
# -------------------------------------------------------------------------------------------
# Stand-alone script
#
# import arcpy
# arcpy.env.workspace = "path"
# in_table1 = "fileName"
# field_name1 = "fieldName"
# field_precision1 = 9
# field_length1 = 50
# field_alias1 = "fieldName_alias"
#
# arcpy.AddField_management(in_table1, field_name1, "TEXT", field_length=field_length1, field_alias=field_alias1,
#                           field_is_nullable="NULLABLE")
# -------------------------------------------------------
# Deleting fields
#
# Syntax: DeleteField_management(in_table, drop_field)
# ----------------------------------------------------
# Python window
#
# import arcpy
# arcpy.env.workspace = "path"
# copy1 = "path1"
# Syntax: CopyFeatures_management(in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2},
#                                {spatial_grid_3})
# arcpy.CopyFeatures_management("fileName", copy1)
# arcpy.DeleteField_management(copy1, ["fieldName"])
# --------------------------------------------------
# Stand-alone script

import arcpy
arcpy.env.workspace = "path"
inFeatures = "fileName"
outFeatureClass = "path1"
dropFields = ["fieldName"]

arcpy.CopyFeatures_management(inFeatures, outFeatureClass)
arcpy.DeleteField_management(outFeatureClass, dropFields)
