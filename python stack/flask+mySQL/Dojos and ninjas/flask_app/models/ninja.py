from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.dojo_id = ["dojo_id"]
        self.first_name = data["first_name"]
        self.last_name = data ["last_name"]
        self.age = data ["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s ,%(last_name)s ,%(age)s , NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        # * Query
        query = """
        SELECT * FROM ninjas WHERE id = %(id)s;
        """
        # *2 Execute
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        print(result)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas 
                SET first_name, last_name, age = %(first_name)s, %(last_name)s, %(age)s
                WHERE id = %(id)s;"""
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
    
    # @classmethod
    # def get_dojo_ninjas(cls,data):
    #     query = """
    #     SELECT *
    #     FROM ninjas 
    #     WHERE dojo_id = %(dojo_id)s
    #     """
    #     # aleh nestaamlou fiha f model hedha 
    #     results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
    #     ninjas = []
    #     print(results)
    #     if(results):
    #         for row in results :
    #             ninjas.append(cls(row))
    #         return ninjas
    #     else:
    #         return []
        
        
