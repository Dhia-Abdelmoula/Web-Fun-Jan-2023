from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User:
    # CONSTRUCTOR -
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # CREATE A USER
    @classmethod
    def create(cls, data):
        
        query = """
                    INSERT INTO users (first_name, last_name, email, password)
                    VALUES	(%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        
        result =  connectToMySQL(DB).query_db(query, data)
        print(result,'-'*33)
        return result
    # GET USER BY ID
    @classmethod
    def get_by_id(cls, data):
        query = """
                    SELECT *
                    FROM users
                    WHERE id = %(id)s;
                """
                
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return []
        return cls(results[0])
    # VALIDATION
    
    @classmethod
    def get_by_email(cls, data):
        query = """
                    SELECT *
                    FROM users
                    WHERE email = %(email)s;
                """
                
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return []
        return cls(results[0])
    
    
    
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 1:
            flash('Name is required ! ', "reg")
            is_valid = False
        # check first name
        if len(data['last_name']) < 1:
            flash('Last name is required ! ', "reg" )
            is_valid = False
        # check last name
        if len(data['email'] ) < 1:
            is_valid = False
            flash("Email is required !","reg")
        # 
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!","reg")
            is_valid = False
        # CHECKING IF THE EMAIL EXISTS
        else:
            # email_dict ={
            #     'email' : data['email']
            # }
            potentiel_user = User.get_by_email(data)
            
            if potentiel_user :
                # EMAIL IS NOT UNIQUE
                is_valid = False
                flash("Email is already taken","reg")
            
        if len(data["password"]) <1 :
            is_valid = False
            flash("Password is required !","reg")
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("password dont match !","reg")
        
        return is_valid
