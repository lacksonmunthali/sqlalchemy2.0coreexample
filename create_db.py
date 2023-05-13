from connection import engine
from tables import meta_obj

print("CREATING DATABASE...")

meta_obj.create_all(bind=engine)
