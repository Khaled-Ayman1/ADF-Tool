
# Advanced Duplicate Filter 1.0 (Beta)#

- ADF is a data analysis tool for filtering column duplicates relative to their number of entries in a certain row, also filling null
entries into the original rows from droppable rows


## Returns ##

- A list of duplicate rows that has the least number of entries than their equivalents (originally dropped), though it's
optional to retrieve this list into a separate sheet, as well as other functionalities to modify your data sheet

## Goal ##

- Open Source Contribution through GitHub, I present you this tool for free use and modification!

## Usage (additional support for csv).. ##

**In your CLI issue the adf command and the following**

-ex : To specify as Excel file
-csv : To specify as CSV file

-path : Insert file path (file name only if in same directory as directory)

-sheet : Insert sheet number (In case of an Excel)

-fill : initiate auto fill null values from duplicates to enhance accuracy

-get : to get a list of the droppable results
-drop : to drop duplicates mentioned in list from original df

-ovr : Overwrite your EXCEL FILE with result sheet

-new : Create new file with result sheet
-npath : New file path

-app : Append to existing file as new sheet
-nsheet : New sheet name

## Notes ##

- For Excel users, exported sheets aren't natively in table format, so make sure to manually edit it
- Upcoming build will future updates for the table issue!!

## Contributing ##

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
