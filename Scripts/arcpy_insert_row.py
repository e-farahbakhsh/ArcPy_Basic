# Inserting new rows by InsertCursor

# Syntax: InsertCursor (dataset, {spatial_reference})
# ---------------------------------------------------
# import arcpy
#
# rows = arcpy.InsertCursor("D:/Python/Test/Vector/Geology_StudyArea.shp")
#
# for i in range(1, 3):
#     row = rows.newRow()
#     row.setValue("Age_era", "Cenozoic")
#     row.setValue("Age_period", "Quaternary")
#     rows.insertRow(row)
#
# del row
# del rows
# --------
# Inserting new rows by da.InsertCursor

# Syntax: InsertCursor (in_table, field_names)
# --------------------------------------------
import arcpy

fields = ["Age_era", "Age_period"]
cursor = arcpy.da.InsertCursor("D:/Python/Test/Vector/Geology_StudyArea.shp", fields)

for i in range(1, 3):
    cursor.insertRow(("Cenozoic", "Quaternary"))

del cursor
