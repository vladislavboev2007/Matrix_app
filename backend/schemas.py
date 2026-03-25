from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name:  str
    grade:      str

class UserOut(BaseModel):
    id:         int
    first_name: str
    last_name:  str
    grade:      str
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class TestResultCreate(BaseModel):
    user_id:          int
    test_id:          int
    test_title:       str
    total_questions:  int
    correct_answers:  int
    percentage:       int
    time_spent:       int
    detailed_results: str

class TestResultOut(BaseModel):
    id:               int
    user_id:          int
    test_id:          int
    test_title:       str
    total_questions:  int
    correct_answers:  int
    percentage:       int
    time_spent:       int
    detailed_results: str
    timestamp:        Optional[datetime] = None
    class Config:
        from_attributes = True