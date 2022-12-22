# Copyright 2022, Khaled Ayman, All rights reserved.

import pandas as pd
import os

# dataframe declaration
path = input("Please insert full file path: ")
sheet_number = int(input("Insert sheet number: "))
xlsx = pd.ExcelFile(path)
df = pd.read_excel(xlsx, sheet_name=sheet_number-1)

# removing unnecessary whitespace
df.columns = df.columns.str.strip()

# column to be cleaned
key_column = input("Enter key column (CASE SENSITIVE): ")

# detecting duplicated values & reindexing dataset for proper operation
duplicate_data = df[df.duplicated([key_column], keep=False)]
duplicate_data = duplicate_data.reset_index()


def auto_fill(unfiltered_duplicate):  # ---> Function to allow duplicates to fill from each other (compare_duplicates)
    return


# returns a list of rows to be dropped
def drop_duplicate(duplicates_df):
    dropped_rows = []

    # holds key column of rows covered before
    is_iterated = []

    # immediately drop any row that has null key column
    for row in df[key_column]:
        is_null = pd.isna(row)
        if is_null:
            df.drop(row, inplace=True)

    for index_val in range(len(duplicates_df)):
        # check that row isn't covered
        if duplicates_df.loc[index_val, key_column] in is_iterated:
            continue
        is_iterated.append(duplicates_df.loc[index_val, key_column])

        # holds equivalent duplicate row lengths
        results = []

        # contains equivalent duplicates for priority comparison
        compare_duplicates = [duplicates_df.loc[index_val].values.tolist()]

        # detecting equivalent duplicates and appending to comparison list
        for duplicate_index in range(len(duplicates_df)):
            # skip current row
            if duplicate_index == index_val:
                continue

            # evaluate whether the iterator row is a duplicate of main loop iterator depending on key column
            if duplicates_df.loc[duplicate_index][key_column] == duplicates_df.loc[index_val][key_column]:
                compared_element = duplicates_df.loc[duplicate_index]
                compare_duplicates.append(compared_element.values.tolist())

        # filter out nan values in duplicates
        clean_duplicates = []

        # returns list of booleans for nulls (True for nan)
        check_null = pd.isna(compare_duplicates).tolist()

        for is_null in check_null:
            not_null = []
            # specify outer list index
            list_index = check_null.index(is_null)
            for column_index in range(len(is_null)):
                if is_null[column_index]:
                    # skip nan values
                    continue
                else:
                    not_null.append(compare_duplicates[list_index][column_index])
            clean_duplicates.append(not_null)

        # compute duplicates length for comparison
        for row in range(len(clean_duplicates)):
            row_list = clean_duplicates[row]
            results.append(len(row_list))

        # stores row with highest entries
        drop_invalid = results.index(max(results))

        # comparing index of duplicates index of highest entries (drop if not the same index)
        for drop_candidate in range(len(clean_duplicates)):
            if clean_duplicates[drop_candidate][0] != clean_duplicates[drop_invalid][0]:
                dropped_rows.append(clean_duplicates[drop_candidate])

    return dropped_rows


drops = drop_duplicate(duplicate_data)
print(f'\nFound {len(drops)} duplicates..\n')

# final iteration to drop rows from the original dataframe
for item in drops:
    df = df.drop(item[0])

user_input = int(input("Options:\n1.Overwrite Whole File\n2.Create New File\n3.Append To Existing File\n\nChoice: "))

if user_input == 1:
    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, index=False)
elif user_input == 2:
    new_path = input("Enter new file full path: ")
    df.to_excel(new_path, sheet_name='Cleaned_py', index=False)
elif user_input == 3:
    # creating ExcelWriter object to append sheet to existing file
    with pd.ExcelWriter(path, mode='a', engine='openpyxl') as writer:
        sheet_name = input("Enter Sheet Name: ")
        df.to_excel(writer, sheet_name=sheet_name, index=False)
else:
    print("Error: Invalid Input")

print("Operation Terminated!\n")
os.system("pause")
