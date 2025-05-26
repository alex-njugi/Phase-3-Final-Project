from lib.models import Session
from lib.models.member import Member
from lib.models.gym_class import GymClass
from lib.models.booking import Booking

session = Session()

# Create members
m1 = Member(name="Alice", phone="0712345678", join_date="2024-01-10")
m2 = Member(name="Bob", phone="0723456789", join_date="2024-02-15")

# Create gym classes
c1 = GymClass(name="Yoga", schedule="Mon 8AM", capacity=10)
c2 = GymClass(name="Boxing", schedule="Wed 6PM", capacity=5)

# Create bookings
b1 = Booking(member=m1, gym_class=c1)
b2 = Booking(member=m2, gym_class=c2)

# Add and commit
session.add_all([m1, m2, c1, c2, b1, b2])
session.commit()
session.close()

print("Seeded database.")
