from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SurveyCreate(BaseModel):
    job_type:    Optional[str] = Field(None, description="직무 (예: 백엔드 개발)")
    region:      Optional[str] = Field(None, description="근무 희망 지역")
    occupation:  Optional[str] = Field(None, description="직업군 (예: IT/개발)")
    career_type: Optional[str] = Field(None, description="신입 | 경력")
    education:   Optional[str] = Field(None, description="학력")


class SurveyUpdate(SurveyCreate):
    pass


class SurveyOut(SurveyCreate):
    id:         str
    user_id:    str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
