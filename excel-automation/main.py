import pandas as pd

print(
    "==================== Excel Data Generator =================\nThis is a simple python script that creates an excel "
    "sheet from a '.txt' file")


def get_excel_data():
    exit_function = False

    try:
        input_received = input("How many columns does your data(your '.txt' file) have? ")
        if input_received == '>':
            exit_function = True
        number_of_columns = int(input_received)

    except ValueError:
        if exit_function:
            return print("Thank you for trying out this automation tool!")

        print("Exit anytime by pressing '>'")
        get_excel_data()

    else:
        column_names = []

        for column in range(number_of_columns):
            column_name = input(f"Column name {column + 1}: ")
            if column_name[-1] == " ":
                column_names.append(column_name[:-1])
                continue
            column_names.append(column_name)

        with open("excel_data.txt") as file:
            excel_data = file.readlines()
            data_for_columns = [[] for _ in column_names]

            for line in excel_data:
                for column_index in range(len(column_names)):
                    if column_names[column_index].lower() in line or column_names[column_index].title() in line or \
                            column_names[column_index].upper() in line:
                        data = line[len(column_names[column_index]):].replace(':', '')
                        if data[0] == ' ':
                            data_for_columns[column_index].append(data[1:])
                            continue

                        data_for_columns[column_index].append(data)

            pd_series = [pd.Series(data_for_columns[data], name=column_names[data].title()) for data in
                         range(len(data_for_columns))]
            df = pd.concat(pd_series, axis=1)

            df.to_excel("new-data.xlsx", index=False)
            print("Excel sheet successfully generated! Check for this folder for a 'new-data.xlsx' file.")


get_excel_data()
