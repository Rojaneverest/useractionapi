from django.db import models

class UserAction(models.Model):
    # Define fields to match the PostgreSQL table columns
    product_id = models.IntegerField()  # Matches the product_id column in the table
    action_type = models.CharField(max_length=50)  # Matches the action_type column
    action_datetime = models.DateTimeField(auto_now_add=True)  # Matches the action_datetime column
    user_id = models.IntegerField()  # Matches the user_id column
    # You might need to add more fields here based on your actual table structure
    
    def __str__(self):
        return f'{self.action_type} - {self.action_datetime}'

    class Meta:
        db_table = 'user_action'
