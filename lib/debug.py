from lib.models import Base, engine
from lib.models import member, gym_class, booking  # Ensure models are registered

if __name__ == "__main__":
    print("Creating all tables...")
    Base.metadata.create_all(engine)
    print("Done.")
