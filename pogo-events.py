import requests
import json
from datetime import datetime
from ics import Calendar, Event

response = requests.get("https://raw.githubusercontent.com/bigfoott/ScrapedDuck/refs/heads/data/events.json")

events = response.json()

print(type(events))

#pos_events = []
wanted_types = ['raid-day', 'event', 'raid-hour', 'raid-battles']
wanted_events = []
for event in events:
    #if event['eventType'] not in pos_events:
    #    pos_events.append(event['eventType'])
    if event['eventType'] in wanted_types:
        start_datetime = datetime.fromisoformat(event['start'])
        end_datetime = datetime.fromisoformat(event['end'])
        duration = str(end_datetime - start_datetime)
        new_event = {
            "name": event['name'],
            "start": event['start'],
            "duration": duration,
            "event_type": event['eventType']
        }
        wanted_events.append(new_event)

for w_event in wanted_events:
    print(json.dumps(w_event, indent=4))

    cal = Calendar()

    event = Event()
    event.name = "Gible Community Day Classic"
    event.begin = w_event['start']
    event.description = f"Duration: {w_event['duration']}"

    cal.events.add(event)

    with open("community-day.ics", "w") as f:
        f.writelines(cal)
