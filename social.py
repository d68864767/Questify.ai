```python
# social.py

class Social:
    def __init__(self, db, user_service, engagement_service, scalability_service):
        self.db = db
        self.user_service = user_service
        self.engagement_service = engagement_service
        self.scalability_service = scalability_service

    def share_post(self, user_id, post_id):
        # Ensure scalability
        self.scalability_service.handle_new_share()

        # Retrieve post data from the database
        post_data = self.db.get_post_data(post_id)

        # Retrieve user data from the database
        user_data = self.user_service.get_user_data(user_id)

        # Create share data
        share_data = {
            'user_id': user_id,
            'post_id': post_id,
            'username': user_data['username'],
            'post_content': post_data['content']
        }

        # Save share data to the database
        self.db.save_share_data(share_data)

        # Increase user engagement
        self.engagement_service.increase_engagement()

    def share_quest(self, user_id, quest_id):
        # Ensure scalability
        self.scalability_service.handle_new_share()

        # Retrieve quest data from the database
        quest_data = self.db.get_quest_data(quest_id)

        # Retrieve user data from the database
        user_data = self.user_service.get_user_data(user_id)

        # Create share data
        share_data = {
            'user_id': user_id,
            'quest_id': quest_id,
            'username': user_data['username'],
            'quest_content': quest_data
        }

        # Save share data to the database
        self.db.save_share_data(share_data)

        # Increase user engagement
        self.engagement_service.increase_engagement()

    def get_shares(self, user_id):
        # Retrieve share data from the database
        share_data = self.db.get_share_data(user_id)

        # Increase user engagement
        self.engagement_service.increase_engagement()

        return share_data
```
