
# Advanced Duplicate Filter 1.0 (Beta)

- ADF (Advanced Data Filtering) is a powerful data analysis tool that specializes in identifying and filtering column duplicates based on their frequency of occurrence within a specific row. It provides functionality to identify duplicate values in a column and determine their relative number of entries across rows.

- Additionally, ADF offers the capability to fill null entries in the original rows with data from droppable rows. This feature ensures that missing or incomplete information is populated using relevant data from other rows, enhancing the completeness and accuracy of the dataset.

- By leveraging ADF's unique filtering and data filling capabilities, analysts can efficiently clean and enhance their datasets, eliminating duplicate values and filling in missing data to create more reliable and robust data for analysis and decision-making.


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
