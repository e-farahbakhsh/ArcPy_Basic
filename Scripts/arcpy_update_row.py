# Updating rows by UpdateCursor
#
# Syntax: UpdateCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
# --------------------------------------------------------------------------------------------
# Using UpdateCursor with a for loop
#
# import arcpy
# arcpy.env.workspace = "path"
#
# fileName = "fileName"
# arcpy.AddField_management(fileName, "era_period", "TEXT", "", "", 50, "era_period_alias", "NULLABLE")
# field1 = "fieldName1"
# field2 = "fieldName2"
# field3 = "fieldName3"
#
# cursor = arcpy.UpdateCursor(fileName)
# for row in cursor:
#     if row.getValue(field1) != ' ' and row.getValue(field2) != ' ':
#         row.setValue(field3, row.getValue(field1) + "_" + row.getValue(field2))
#     else:
#         row.setValue(field3, "Not Assigned")
#     cursor.updateRow(row)
# -------------------------
# Using UpdateCursor with a while loop
#
# import arcpy
# arcpy.env.workspace = "path"
#
# fileName = "fileName"
# arcpy.AddField_management(fileName, "era_period", "TEXT", "", "", 50, "era_period_alias", "NULLABLE")
# field1 = "fieldName1"
# field2 = "fieldName2"
# field3 = "fieldName3"
#
# cursor = arcpy.UpdateCursor(fileName)
# row = cursor.next()
# while row:
#     if row.getValue(field1) != ' ' and row.getValue(field2) != ' ':
#         row.setValue(field3, row.getValue(field1) + "_" + row.getValue(field2))
#     else:
#         row.setValue(field3, "Not Assigned")
#     cursor.updateRow(row)
#     row = cursor.next()
# -----------------------
# Updating rows by da.UpdateCursor
#
# Syntax: da.UpdateCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
# -----------------------------------------------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "path"

fileName = "fileName"
arcpy.AddField_management(fileName, "era_period", "TEXT", "", "", 50, "era_period_alias", "NULLABLE")
fields = ["field1", "field2", "field3"]

with arcpy.da.UpdateCursor(fileName, fields) as cursor:
    for row in cursor:
        if row[0] != ' ' and row[1] != ' ':
            row[2] = row[0] + "_" + row[1]
        else:
            row[2] = "Not Assigned"
        cursor.updateRow(row)
