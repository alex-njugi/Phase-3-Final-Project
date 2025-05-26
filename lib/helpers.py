from lib.models import Session
from lib.models.member import Member
from lib.models.gym_class import GymClass
from lib.models.booking import Booking

def list_members():
    session = Session()
    members = session.query(Member).all()
    for m in members:
        print(f"[{m.id}] {m.name} - {m.phone}")
    session.close()

def list_classes():
    session = Session()
    classes = session.query(GymClass).all()
    for c in classes:
        print(f"[{c.id}] {c.name} - {c.schedule} (Capacity: {c.capacity})")
    session.close()

def list_bookings():
    session = Session()
    bookings = session.query(Booking).all()
    for b in bookings:
        print(f"Member: {b.member.name} → Class: {b.gym_class.name}")
    session.close()

def add_member():
    name = input("Name: ")
    phone = input("Phone: ")
    join_date = input("Join date (YYYY-MM-DD): ")
    session = Session()
    m = Member(name=name, phone=phone, join_date=join_date)
    session.add(m)
    session.commit()
    session.close()
    print("Member added.")

def add_class():
    name = input("Class name: ")
    schedule = input("Schedule: ")
    capacity = int(input("Capacity: "))
    session = Session()
    c = GymClass(name=name, schedule=schedule, capacity=capacity)
    session.add(c)
    session.commit()
    session.close()
    print("Class added.")

def book_member():
    member_id = int(input("Enter member ID: "))
    class_id = int(input("Enter class ID: "))
    session = Session()

    gym_class = session.query(GymClass).get(class_id)
    booking_count = session.query(Booking).filter_by(gym_class_id=class_id).count()

    if booking_count >= gym_class.capacity:
        print("⚠️ Class is full!")
    else:
        b = Booking(member_id=member_id, gym_class_id=class_id)
        session.add(b)
        session.commit()
        print("Booking successful.")
    
    session.close()

def delete_member():
    member_id = int(input("Enter member ID to delete: "))
    session = Session()
    member = session.query(Member).get(member_id)
    if member:
        session.delete(member)
        session.commit()
        print("Member deleted.")
    else:
        print("Member not found.")
    session.close()

def delete_class():
    class_id = int(input("Enter class ID to delete: "))
    session = Session()
    gym_class = session.query(GymClass).get(class_id)
    if gym_class:
        session.delete(gym_class)
        session.commit()
        print("Class deleted.")
    else:
        print("Class not found.")
    session.close()
