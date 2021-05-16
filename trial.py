import sqlgenerator

a={"s_column": ["username", "address"], "s_table": "table_name", "s_where": "country='Mexico' and sex = 'female'"}

s=sqlgenerator.Sql_Generator(a) #Geanerate Instance and below it calls functional name.xxxx
sql=s.sql_search() 
print (sql)

del s

dic_sql_generator={
    #--- insert method ---*
    "s_table":"table",
    "s_column_value": {"column1": ["value1", "value11"], "column2": "value2"}
} 
s=sqlgenerator.Sql_Generator(dic_sql_generator) #Geanerate Instance and below it calls functional name.xxxx
sql2=s.sql_insert() 

print (sql2)

del s
