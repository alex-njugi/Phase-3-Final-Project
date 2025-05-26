from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    join_date = Column(String)

    bookings = relationship('Booking', back_populates='member', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Member {self.name}>"
