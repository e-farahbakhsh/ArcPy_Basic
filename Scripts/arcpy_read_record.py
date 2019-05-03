# Reading records by SearchCursor
#
# Syntax: SearchCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
# --------------------------------------------------------------------------------------------
# Using SearchCursor with a for loop
#
# import arcpy
# arcpy.env.workspace = "D:/Python/Test/Vector"
#
# fileName = "Geology_StudyArea.shp"
# field = "Age_era"
#
# cursor = arcpy.SearchCursor(fileName)
# for row in cursor:
#     if row.getValue(field) != ' ':
#         print(row.getValue(field))
# --------------------------------
# Using SearchCursor with a while loop
#
# import arcpy
# arcpy.env.workspace = "D:/Python/Test/Vector"
#
# fileName = "Geology_StudyArea.shp"
# field = "Age_era"
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
# rows = arcpy.SearchCursor("D:/Python/Test/Vector/Geology_StudyArea.shp",
#                           fields="Age_era; Age_period",
#                           sort_fields="Age_era A")
#
# for row in rows:
#     if row.getValue("Age_era") != ' ' and row.getValue("Age_period") != ' ':
#         print("Age_era: {0}, Age_period: {1}".format(
#             row.getValue("Age_era"),
#             row.getValue("Age_period")))
# ----------------------------------------
# Reading records by da.SearchCursor
#
# Syntax: SearchCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
# --------------------------------------------------------------------------------------------------------------------
# import arcpy
# arcpy.env.workspace = "D:/Python/Test/Vector"
#
# fileName = "Geology_StudyArea.shp"
# fields = ["Label", "SHAPE@AREA"]
#
# with arcpy.da.SearchCursor(fileName, fields) as cursor:
#     for row in cursor:
#         print(u"{0}: {1}".format(row[0], row[1]))
# -----------------------------------------------
import arcpy
arcpy.env.workspace = "D:/Python/Test/Vector"

fileName = "Geology_StudyArea.shp"

expression = u"{} <> ' '".format(arcpy.AddFieldDelimiters(fileName, "Label"))

with arcpy.da.SearchCursor(fileName, ["Label", "SHAPE@AREA"],
                           where_clause=expression) as cursor:
    for row in cursor:
        print(u"{0}: {1}".format(row[0], row[1]))
