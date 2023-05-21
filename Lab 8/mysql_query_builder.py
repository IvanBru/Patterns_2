from query_builder import QueryBuilder

class MySQLQueryBuilder(QueryBuilder):
    def getSQL(self):
        sql = "SELECT "

        if self.select_columns:
            sql += ", ".join(self.select_columns)
        else:
            sql += "*"

        sql += " FROM your_table"

        if self.where_conditions:
            sql += " WHERE " + " AND ".join(self.where_conditions)

        if self.limit_value is not None:
            sql += " LIMIT " + str(self.limit_value)

        return sql