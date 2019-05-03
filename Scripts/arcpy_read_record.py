# Reading records by SearchCursor
#
# Syntax: SearchCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
# --------------------------------------------------------------------------------------------
# Using SearchCursor with a for loop
#
# import arcpy
# arcpy.env.workspace = "path"
#
# fileName = "fileName"
# field = "fieldName"
#
# cursor = arcpy.SearchCursor(fileName)
# for row in cursor:
#     if row.getValue(field) != ' ':
#         print(row.getValue(field))
# --------------------------------
# Using SearchCursor with a while loop
#
# import arcpy
# arcpy.env.workspace = "path"
#
# fileName = "fileName"
# field = "fieldName"
#
# cursor = arcpy.SearchCursor(fileName)
# row = cursor.next()
# while row:
#     if row.getValue(field) != ' ':
#         print(row.getValue(field))
#     row = cursor.next()
# -----------------------
# Sorting fields
#
# import arcpy
#
# rows = arcpy.SearchCursor("path",
#                           fields="fieldName1; fieldName2",
#                           sort_fields="fieldName1 A")
#
# for row in rows:
#     if row.getValue("fieldName1") != ' ' and row.getValue("fieldName2") != ' ':
#         print("fieldName1: {0}, fieldName2: {1}".format(
#             row.getValue("fieldName1"),
#             row.getValue("fieldName2")))
# ----------------------------------------
# Reading records by da.SearchCursor
#
# Syntax: SearchCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
# --------------------------------------------------------------------------------------------------------------------
# import arcpy
# arcpy.env.workspace = "path"
#
# fileName = "fileName"
# fields = ["fieldName1", "SHAPE@AREA"]
#
# with arcpy.da.SearchCursor(fileName, fields) as cursor:
#     for row in cursor:
#         print(u"{0}: {1}".format(row[0], row[1]))
# -----------------------------------------------
import arcpy
arcpy.env.workspace = "path"

fileName = "fileName"

expression = u"{} <> ' '".format(arcpy.AddFieldDelimiters(fileName, "fieldName"))

with arcpy.da.SearchCursor(fileName, ["fieldName", "SHAPE@AREA"],
                           where_clause=expression) as cursor:
    for row in cursor:
        print(u"{0}: {1}".format(row[0], row[1]))
