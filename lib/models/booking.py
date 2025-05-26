from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    gym_class_id = Column(Integer, ForeignKey('gym_classes.id'))

    member = relationship('Member', back_populates='bookings')
    gym_class = relationship('GymClass', back_populates='bookings')

    def __repr__(self):
        return f"<Booking: Member {self.member_id} → Class {self.gym_class_id}>"
