# Copyright 2023, Khaled Ayman, All rights reserved.

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


# Function to allow duplicates to fill from each other (compare_duplicates)
def auto_fill(compare_duplicates):
    auto_filled = []
    for primary_list in compare_duplicates:

        for secondary_list in compare_duplicates:
            if primary_list == secondary_list:
                continue
            primary_na = pd.isna(primary_list).tolist()
            secondary_na = pd.isna(secondary_list).tolist()

            for null_check in range(len(primary_na)):
                primary_bool = primary_na[null_check]
                secondary_bool = secondary_na[null_check]

                if primary_bool != secondary_bool:
                    if primary_bool:
                        primary_list[null_check] = secondary_list[null_check]
                    if secondary_bool:
                        secondary_list[null_check] = primary_list[null_check]
    auto_filled.append(primary_list)
    return auto_filled


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
        main_value = duplicates_df.loc[index_val, key_column]
        if main_value in is_iterated:
            continue
        is_iterated.append(main_value)

        # holds equivalent duplicate row lengths
        results = []
        compared_element = duplicates_df.loc[index_val].values.tolist()

        # contains equivalent duplicates for priority comparison
        compare_duplicates = [compared_element]

        # detecting equivalent duplicates and appending to comparison list
        for duplicate_index in range(len(duplicates_df)):
            # skip current row
            if duplicate_index == index_val:
                continue

            loop_value = duplicates_df.loc[duplicate_index][key_column]

            # evaluate whether the iterator value is a duplicate of main loop value depending on key column
            if loop_value == main_value:
                compared_element = duplicates_df.loc[duplicate_index].values.tolist()
                compare_duplicates.append(compared_element)

        auto_fill(compare_duplicates)

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

        # stores row with the highest entries
        drop_invalid = results.index(max(results))

        # comparing index of duplicates index with the highest entries (drop if not the same index)
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
    new_path = input("Enter new file full path (Include file name): ")
    sheet_name = input("Enter Sheet Name: ")
    df.to_excel(new_path, sheet_name=sheet_name, index=False)
elif user_input == 3:
    # creating ExcelWriter object to append sheet to existing file
    with pd.ExcelWriter(path, mode='a', engine='openpyxl') as writer:
        sheet_name = input("Enter Sheet Name: ")
        df.to_excel(writer, sheet_name=sheet_name, index=False)
else:
    print("Error: Invalid Input")

print("Operation Terminated!\n")
os.system("pause")
