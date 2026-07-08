from pydantic import BaseModel
from typing import Optional

# Pydantic model for task
class Task(BaseModel):
    title: str
    description: Optional[str] = None