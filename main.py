import os
import pandas as pd
import mysql.connector
import chardet

# connection to MySQL
cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="onet_es",
  port=3306
)

cursor = cnx.cursor()

absolute_path = os.path.dirname(__file__)
relative_path = "db_txt"
full_path = os.path.join(absolute_path, relative_path)

dir_name = full_path

# loop for all the files in the directory
for file_name in os.listdir(dir_name):
    if file_name.endswith(".txt"):

        print(file_name)

        with open(os.path.join(dir_name, file_name), 'rb') as f:
            result = chardet.detect(f.read())

        print(result)

        print("Reading CSV")
        # Load the text file in a Panda's DataFrame
        df = pd.read_csv(os.path.join(dir_name, file_name), delimiter="\t", encoding=result['encoding'])

        print("Creating table " + format(os.path.splitext(file_name)))
        # Create MySQL table query
        create_table_query = "CREATE TABLE `{}` (".format(os.path.splitext(file_name)[0])

        print("Preparing columns")
        for col in df.columns:
            print("checking columns " + col)
            # We find the max length from the values of this column
            max_len = df[col].astype(str).map(len).max()

            # Set the column type depending the max value
            if max_len <= 255:
                col_type = "CHAR(" + str(max_len) + ")"
            elif max_len <= 65535:
                col_type = "TEXT"
            else:
                col_type = "LONGTEXT"

            print("Colum type: " + col_type)

            # We add quotes between column names which has special characters
            create_table_query += "`{}` {}, ".format(col, col_type)

        print("Preparing create table query")
        create_table_query = create_table_query[:-2] + ")"

        print("Executing query")
        cursor.execute(create_table_query)

        print("Creating Data")
        # Insert data inside the MySQL table
        for row in df.itertuples():
            values = ', '.join(['%s' for _ in range(len(row) - 1)])
            insert_query = "INSERT INTO `{}` VALUES ({})".format(os.path.splitext(file_name)[0], values)
            cursor.execute(insert_query, row[1:])

        print("Commit")
        cnx.commit()

cursor.close()
cnx.close()
