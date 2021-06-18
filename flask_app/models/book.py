from ..config.mysqlconnection import connectToMySQL
from ..models import author


class Book:
    
    
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.authors = []
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        con = connectToMySQL("books_schema")
        res = con.query_db(query)
        books = []
        for r in res:
            books.append(cls(r))
        return books
    
    
    @classmethod
    def add_one(cls,data):
        query = "INSERT INTO books(title,num_of_pages,created_at,updated_at) VALUES (%(title)s,%(num_of_pages)s,NOW(),NOW());"
        con = connectToMySQL("books_schema")
        res = con.query_db(query,data)
        print(res)
        return res
        
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id " \
            "LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)
        if len(results)==0:
            return 
        else:
            res = results[0]
            book = cls(results[0])
        print(results[0])
        if results[0]['id'] != None:
            for row in results:
                row_data = {
                    "id": row['authors.id'],
                    "name": row['name'],
                    "created_at": row['authors.created_at'],
                    "updated_at": row['authors.updated_at']
                }
                book.authors.append(author.Author(row_data))
        return book