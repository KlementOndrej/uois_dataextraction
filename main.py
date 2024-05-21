import psycopg2, json
from utils.formaters import dictionarizeTable
from utils.fetchers import fetchTableNames, fetchTableAttributes, fetchTableContent

try:
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
        database="data"
    )
except psycopg2.Error as e:
    print("Error connecting to the database:")
    print(e)
else:
    print("Connection established successfully")

table_names = fetchTableNames(conn)

output = {}

for i in range(len(table_names)):
    output[table_names[i]] = dictionarizeTable(fetchTableContent(conn, table_names[i]), fetchTableAttributes(conn, table_names[i]))

#print(json.dumps(output, sort_keys=True, indent=4, default=str))

file = open('data.json', 'w')
file.write(json.dumps(output, sort_keys=False, indent=4, default=str, ensure_ascii=False))

# close the cursor and connection
conn.close()