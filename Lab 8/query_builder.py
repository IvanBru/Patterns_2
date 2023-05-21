class QueryBuilder:
    def __init__(self, db_type):
        self.db_type = db_type
        self.select_columns = []
        self.where_conditions = []
        self.limit_value = None

    def select(self, *columns):
        self.select_columns = list(columns)

    def where(self, condition):
        self.where_conditions.append(condition)

    def limit(self, limit):
        self.limit_value = limit

    def getSQL(self):
        print('Метод повинен бути реалізований підкласами')