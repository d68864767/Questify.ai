```python
# ai.py

import random

class AI:
    def __init__(self, db):
        self.db = db

    def get_recommendations(self, user_data):
        # Retrieve all quests from the database
        all_quests = self.db.get_all_quests()

        # Filter quests based on user's location
        location_based_quests = [quest for quest in all_quests if quest['location'] == user_data['location']]

        # If there are no location-based quests, return random quests
        if not location_based_quests:
            return random.sample(all_quests, min(5, len(all_quests)))

        # Further filter quests based on user's preferences
        preference_based_quests = [quest for quest in location_based_quests if quest['theme'] in user_data.get('preferences', [])]

        # If there are no preference-based quests, return location-based quests
        if not preference_based_quests:
            return random.sample(location_based_quests, min(5, len(location_based_quests)))

        # Return preference-based quests
        return random.sample(preference_based_quests, min(5, len(preference_based_quests)))

    def get_quest_recommendations(self, user_data):
        # Retrieve all quests from the database
        all_quests = self.db.get_all_quests()

        # Filter quests based on user's location
        location_based_quests = [quest for quest in all_quests if quest['location'] == user_data['location']]

        # If there are no location-based quests, return random quests
        if not location_based_quests:
            return random.sample(all_quests, min(5, len(all_quests)))

        # Further filter quests based on user's preferences
        preference_based_quests = [quest for quest in location_based_quests if quest['theme'] in user_data.get('preferences', [])]

        # If there are no preference-based quests, return location-based quests
        if not preference_based_quests:
            return random.sample(location_based_quests, min(5, len(location_based_quests)))

        # Return preference-based quests
        return random.sample(preference_based_quests, min(5, len(preference_based_quests)))
```
