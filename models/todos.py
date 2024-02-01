# from pydantic import BaseModel, Field
# from typing import List
# from datetime import datetime

# class Todo(BaseModel):
#    company_id : str = Field(..., min_length=1)
#    url : str = Field(..., min_length=1)
#    header : str = Field(..., min_length=1)
#    events : List[str]
#    is_active : bool = True
#    created_at: int = Field(..., description="Unix timestamp representing creation time")
#    updated_at: int = Field(..., description="Unix timestamp representing last update time")

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Todo(BaseModel):
    company_id: str = Field(..., min_length=1)
    url: str = Field(..., min_length=1)
    events: List[str] = Field(..., min_items=1)
    is_active: bool = True
    created_at: int = Field(
        ...,
        description="Unix timestamp representing creation time",
        default_factory=lambda: int(datetime.utcnow().timestamp())
    )
    updated_at: int = Field(
        ...,
        description="Unix timestamp representing last update time",
        default_factory=lambda: int(datetime.utcnow().timestamp())
    )

    