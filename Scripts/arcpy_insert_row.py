# Inserting new rows by InsertCursor
#
# Syntax: InsertCursor (dataset, {spatial_reference})
# ---------------------------------------------------
# import arcpy
#
# rows = arcpy.InsertCursor("path")
#
# for i in range(1, 3):
#     row = rows.newRow()
#     row.setValue("field1", "value1")
#     row.setValue("field2", "value2")
#     rows.insertRow(row)
#
# del row
# del rows
# --------
# Inserting new rows by da.InsertCursor
#
# Syntax: da.InsertCursor (in_table, field_names)
# -----------------------------------------------
import arcpy

fields = ["field1", "field2"]
cursor = arcpy.da.InsertCursor("path", fields)

for i in range(1, 3):
    cursor.insertRow(("value1", "value2"))

del cursor
