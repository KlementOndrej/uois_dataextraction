#lists all table names
def fetchTableNames(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    result = cursor.fetchall()
    cursor.close()
    output = []
    for i in range(len(result)):
        output.append(result[i][0])
    return output

#lists all atributes from a table
def fetchTableAttributes(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns where table_schema = 'public' and table_name= '{table_name}'")
    result = cursor.fetchall()
    cursor.close()
    output = []
    for i in range(len(result)):
        output.append(result[i][0])
    return output

#fetches all rows from a table
def fetchTableContent(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM public.{table_name}")
    result = cursor.fetchall()
    cursor.close()
    return result