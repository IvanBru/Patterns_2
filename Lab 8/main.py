from mysql_query_builder import MySQLQueryBuilder
from postgre_query_builder import PostgreSQLQueryBuilder


# Використання PostgreSQLQueryBuilder
postgre_query_builder = PostgreSQLQueryBuilder("PostgreSQL")
postgre_query_builder.select("column1", "column2")
postgre_query_builder.where("column3 = 'value'")
postgre_query_builder.limit(10)
postgre_sql_query = postgre_query_builder.getSQL()

# Використання MySQLQueryBuilder
mysql_query_builder = MySQLQueryBuilder("MySQL")
mysql_query_builder.select("column1", "column2")
mysql_query_builder.where("column3 = 'value'")
mysql_query_builder.limit(10)
mysql_sql_query = mysql_query_builder.getSQL()