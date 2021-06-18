from ..config.mysqlconnection import connectToMySQL
from ..models import book


class Author:
    
    
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.books = []
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        con = connectToMySQL("books_schema")
        res = con.query_db(query)
        authors = []
        for r in res:
            authors.append(cls(r))
        return authors
    
    
    @classmethod
    def add_one(cls,data):
        query = "INSERT INTO authors(name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW());"
        con = connectToMySQL("books_schema")
        res = con.query_db(query,data)
        print(res)
        return res
        
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id " \
            "LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"

        results = connectToMySQL("books_schema").query_db(query, data)
        if len(results)==0:
            return {"ERROR":"RETURNED EMPTY"}
        else:
            res = results[0]
            author = Author(results[0])


        if results[0]['id'] != None:
            for row in results:
                row_data = {
                    "id": row['book_id'],
                    "title": row['title'],
                    "num_of_pages": row['num_of_pages'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
                }
                author.books.append(book.Book(row_data))
        return author