import sqlgenerator

a={"s_column": ["username", "address"], "s_from": "table_name", "s_where": "country='Mexico' and sex = 'female'"}

x=sqlgenerator
s=sqlgenerator.Sql_Generator(a) #Geanerate Instance and below it calls functional name.xxxx
sql=s.sql_search() 

print (sql)