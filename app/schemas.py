from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import datetime

class MilSymbolBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    code: str = Field(..., min_length=1, max_length=255)
    type: Optional[str] = Field(None, max_length=100)
    icon_url: Optional[HttpUrl] = None
    description: Optional[str] = None

class MilSymbolCreate(MilSymbolBase):
    pass

class MilSymbolUpdate(BaseModel):
    name: Optional[str]
    code: Optional[str]
    type: Optional[str]
    icon_url: Optional[HttpUrl]
    description: Optional[str]

class MilSymbolInDBBase(MilSymbolBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MilSymbol(MilSymbolInDBBase):
    pass