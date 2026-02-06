

from pydantic import BaseModel


class event(BaseModel):
    source: str
    eventType: str
    duration: str | None = None