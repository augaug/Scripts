# This is a script to add multiple fields to an existing feature class(es).
# MSA 9/21/2016
# Name: AddFieldstoMultipleFCs.py
# Description: Add multiple/varying new fields to different featureclass tables

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r'C:\Users\maugust/Desktop\Temp\Scripts\PSE_Cultural_Resources.gdb' #the r allows for regular Windows style path i.e., c:\Users\x\x\x\

# Set local variables   (re-use these values in the arcpy.AddField_management steps below)
inFeatures = "Resource_Line"
inFeatures2 = "Resource_Polygon"
inFeatures3 = "Resource_Isolates_Artifacts"
fieldName1 = "Resource_Name"
fieldName2 = "Classification_Name"
fieldName3 = "Artifact_Type"
fieldName4 = "Artifact_Material"
fieldName5 = "Classification" #Has a domain
fieldName6 = "Style"
fieldName7 = "Date_of_Construction"
fieldName8 = "Building_Eng_Arch"
fieldName9 = "Within_District" #Has a domain
fieldName10 = "Contributing" #Has a domain
fieldName11 = "Elevation"
fieldName12 = "Date_Range"
fieldLength = 150
fieldLength2 = 100
fieldLength3 = 500
field_domain = "Yes/No"
field_domain2 = "Classification"
#field_domain3 = "", etc., etc.

# Execute AddField for new fields for 1st featureclass "infeatures" in this example
arcpy.AddField_management (inFeatures, fieldName2, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures, fieldName3, "TEXT", field_length=fieldLength3)
arcpy.AddField_management (inFeatures, fieldName4, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures, fieldName5, "TEXT", field_length=fieldLength, field_domain=field_domain2)
arcpy.AddField_management (inFeatures, fieldName6, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures, fieldName7, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures, fieldName8, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures, fieldName9, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures, fieldName10, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures, fieldName11, "DOUBLE")
arcpy.AddField_management (inFeatures, fieldName12, "TEXT")
# Execute AddField for new fields for 2nd featureclass "infeatures2" defined above
arcpy.AddField_management (inFeatures2, fieldName2, "TEXT",field_length=fieldLength)
arcpy.AddField_management (inFeatures2, fieldName3, "TEXT", field_length=fieldLength3)
arcpy.AddField_management (inFeatures2, fieldName4, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures2, fieldName5, "TEXT", field_length=fieldLength, field_domain=field_domain2)
arcpy.AddField_management (inFeatures2, fieldName6, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures2, fieldName7, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures2, fieldName8, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures2, fieldName9, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures2, fieldName10, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures2, fieldName11, "DOUBLE")
arcpy.AddField_management (inFeatures2, fieldName12, "TEXT")
# Execute AddField for new fields for 3rd featureclass
arcpy.AddField_management (inFeatures3, fieldName2, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures3, fieldName3, "TEXT", field_length=fieldLength3)
arcpy.AddField_management (inFeatures3, fieldName4, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures3, fieldName5, "TEXT", field_length=fieldLength, field_domain=field_domain2)
arcpy.AddField_management (inFeatures3, fieldName6, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures3, fieldName7, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures3, fieldName8, "TEXT", field_length=fieldLength)
arcpy.AddField_management (inFeatures3, fieldName9, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures3, fieldName10, "TEXT", field_length=fieldLength, field_domain=field_domain)
arcpy.AddField_management (inFeatures3, fieldName11, "DOUBLE")
arcpy.AddField_management (inFeatures3, fieldName12, "TEXT")
