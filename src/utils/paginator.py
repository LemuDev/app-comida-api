from sqlmodel import select, Session
from src.config.db import engine


class Paginator():
    def __init__(self, model, page: int = 1, rows_per_page:int = 10):
        self.model = model
        self.page = page
        self.rows_per_page = rows_per_page

        if self.page <= 0:
            self.page = 1
            
        if self.rows_per_page <= 0:
            self.rows_per_page = 1
    
    
    def get_data(self):
        offset = self.page * self.rows_per_page - (self.rows_per_page) 
        with Session(engine) as session:
            results = session.exec(select(self.model).offset(offset).limit(self.rows_per_page)).all()
            
            return results

    def prev_page(self):
        if self.page <= 1:
            return None
        
        new_page = self.page - 1
        return new_page
        
    def next_page(self):
        with Session(engine) as session:
            offset = self.page * self.rows_per_page
            
            results = session.exec(select(self.model).offset(offset).limit(self.rows_per_page)).one_or_none()
            
            if results == None:
                return None

            return self.page + 1