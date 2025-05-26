from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class GymClass(Base):
    __tablename__ = 'gym_classes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    schedule = Column(String)
    capacity = Column(Integer)

    bookings = relationship('Booking', back_populates='gym_class', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<GymClass {self.name} at {self.schedule}>"
