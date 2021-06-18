from ..config.mysqlconnection import connectToMySQL

class Favorite:
    
    
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.author_id = data['author_id']
        self.book_id = data['book_id']
    
    
    @classmethod
    def add_one(cls,data):
        query = "INSERT INTO favorites(author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        con = connectToMySQL("books_schema")
        res = con.query_db(query,data)
        print(res)
        return res
    
