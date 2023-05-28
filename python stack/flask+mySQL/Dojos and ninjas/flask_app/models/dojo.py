from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES ( %(name)s , NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        # * Query
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        # *2 Execute
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        print(result)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE dojos 
                SET name=%(name)s 
                WHERE id = %(id)s;"""
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
    
    @classmethod
    def Get_ninjas_dojo(cls, data):
        query = """
        SELECT *
        FROM dojos
        JOIN ninjas
        ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        print(results,"*"*30)
        # we created a dojo instance of the index choosen (left table)  
        this_dojo = cls(results[0]) 
        
        
        theses_ninjas = []
        for row in results:
            ninja_data = {
                "id" : row ['ninjas.id'],
                "dojo_id" : row['dojo_id'],
                "first_name" : row['first_name'],
                "last_name" : row ['last_name'],
                "age" : row ['age'],
                "created_at" : row ['ninjas.created_at'],
                "updated_at" : row ['ninjas.updated_at']
        }
            this_ninja = Ninja(ninja_data)
            theses_ninjas.append(this_ninja)
        this_dojo.ninjas = theses_ninjas
        return this_dojo
            
            
            
        
        # Iterate over the db results and create instances of friends with cls.
        # for dojo in results:
            
            
            
        #     dojos.append(cls(dojo))
        # return dojos

        
        