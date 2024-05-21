# function that puts tables to list of dictionaries
def dictionarizeTable(table, attributes):
    output_table = []
    for i in range(len(table)):
        dictionary = {}
        for j in range(len(table[i])):
            dictionary[attributes[j]] = table[i][j]
        output_table.append(dictionary)
    return output_table