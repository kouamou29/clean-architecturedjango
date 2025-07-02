from dataclasses import dataclass
from datetime import datetime


@dataclass
class EntierCategory:
   name: str
   def __init__(self, name: str):
        self.name = name
        


@dataclass
class EntiersPost:
    """
    Represents a blog post with a title, content, and publication date.
    """
    id:int
    title: str
    content: str
    user_id: int
    category_id: int
    created_at: str

    