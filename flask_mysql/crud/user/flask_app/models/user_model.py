from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at= data_dict['updated_at']
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(f"result from database = {results}")
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

        #___________create user
    @classmethod
    def create_user(cls, data_dict):
        query = """
        INSERT INTO users (first_name, last_name, email) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s);"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)