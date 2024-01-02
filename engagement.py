```python
# engagement.py

class Engagement:
    def __init__(self, db):
        self.db = db
        self.engagement_data = {
            'user_engagement': 0,
            'quest_engagement': 0,
            'reward_engagement': 0,
            'community_engagement': 0
        }

    def increase_engagement(self, engagement_type):
        # Increase the specific type of engagement
        self.engagement_data[engagement_type] += 1

        # Save updated engagement data to the database
        self.db.save_engagement_data(self.engagement_data)

    def get_engagement(self, engagement_type):
        # Retrieve the specific type of engagement data from the database
        engagement_data = self.db.get_engagement_data(engagement_type)

        return engagement_data

    def get_total_engagement(self):
        # Retrieve all engagement data from the database
        total_engagement = self.db.get_total_engagement()

        return total_engagement
```
