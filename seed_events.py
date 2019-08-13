from event_models import Event
import datetime;

def seed_data():
    event_1 = Event(event_name="Basketball game",
              location="gym",
              organization_name="Basketball Team",
              category="Athletics",
              college_name="Loyola Marymount University",
              date_and_time=datetime.date(2019, 9, 10))
    event_1.put()
