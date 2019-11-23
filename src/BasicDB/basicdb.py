import csv
import json
import operator

schema = None
db = None

### Database commands ###

# Create a new empty database
def create_db():
    global schema 
    schema = []
    global db 
    db = {}

# Load a database
def load_db(schema_filename):
    create_db()
    global schema
    with open(schema_filename) as f_schema:
        schema = json.load(f_schema)
    for table in schema:
        with open(table['filename']) as f_table:
            reader = csv.DictReader(f_table, fieldnames = table['fields'])
            db[table['name']] = list(reader)   

# Save a database
def save_db(schema_filename):
    with open(schema_filename, 'w') as f_schema:
        json.dump(schema, f_schema)
    for table in schema:
        with open(table['filename'], 'w') as f_table:
            writer = csv.DictWriter(f_table, table['fields'])
            writer.writerows(db[table['name']])



### Table commands ###

# Creates an empty table with the specified fields
# SQL: CREATE TABLE table_name (fields);
def create_table(table_name, field_names):
    new_table = {}
    new_table['name'] = table_name
    new_table['filename'] = table_name + '.csv'
    new_table['fields'] = field_names
    schema.append(new_table)
    
    db[table_name] = []
    
# Removes the specified table from the database
# SQL: DROP TABLE table_name;
def drop_table(table_name):
    global schema
    new_schema = []
    for table in schema:
        if table['name'] != table_name:
            new_schema.append(table)
    schema = new_schema
    del db[table_name]


# Add specified row to table_name
# SQL: INSERT INTO table_name VALUES row;
def insert(table_name, row):
    db[table_name].append(row)

# Delete specified row from table_name
# SQL: DELETE FROM table_name ...
def delete(table_name, delete_row):
    db[table_name].remove(delete_row)



### Rowset commands ###

# Returns all the rows from table_name
# SQL: FROM table_name;
def db_from(table_name):
    return db[table_name]

# Extracts specified field
# SQL: SELECT field 
def select(rows, field):
    values = []
    for row in rows: 
        values.append(row[field])
    return values

# Return list of only the rows where field == value
# SQL: WHERE field=value
def where(rows, field, value):
    new_rows = []
    for row in rows:
        if row[field] == value:
            new_rows.append(row)
    return new_rows

# Returns only the distinct rows in a list
# SQL DISTINCT 
def distinct(rows):
	new_rows = []
	for row in rows:
	    if row not in new_rows:
	        new_rows.append(row)
	return new_rows

# Sort a list of rows based on their value in field
# SQL: ORDER BY field 
def orderby(rows, field):
    return sorted(rows, key = operator.itemgetter(field))


# Counts the number of rows
# SQL: COUNT(*)
def count(rows):
    return len(rows)
    
# Totals the values in field
# SQL: SUM(field)
def db_sum(rows, field):
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total


# Combine rows which have the same value in field in both tables
# SQL: INNER JOIN ... ON rows1.field = rows2.field
def join(rows1, rows2, field):
    new_rows = []
    for row1 in rows1:
        for row2 in rows2:
            if row1[field] == row2[field]:
                new_row = {}
                new_row.update(row1)
                new_row.update(row2)
                new_rows.append(new_row)
    return new_rows




