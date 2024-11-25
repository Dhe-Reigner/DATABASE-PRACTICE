from django.db import models




# EVENT = [
#     ('New Year', 'Event 1 Description', 'Event 1 Location', '2022-01-01', '2022-01-31', 'Organizer 1'),
#     ('Christmas', 'Event 2 Description', 'Event 2 Location', '2022-02-01', '2022-02-28', 'Organizer 2'),
#     ('Christmas Eve', 'Event 3 Description', 'Event 3 Location', '2022-03-01', '2022-03-31', 'Organizer 3'),
# ]

# EVENT = [
#     ('New Year', 'A new year event', 'New Year Village', '2022-01-01', '2022-01-31', 'John Doe'),
#     ('Christmas', 'A Christmas event', 'Christmas Village', '2022-02-01', '2022-02-28', 'Jane Doe'),
#     ('Christmas Eve', 'A Christmas Eve event', 'Christmas Eve Village', '2022-03-01', '2022-03-31', 'Mike Doe'),
#     ('Halloween', 'A Halloween event', 'Halloween Village', '2022-10-01', '2022-10-31', 'Emma Johnson'),
# ]
EVENT = [
    ('new_year','New Year'),
    ('christmas','Christmas'),
    ('christmas_eve','Christmas Eve'),
  
]
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    organizer = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event,choices = EVENT, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,default='')
    
    
    def __str__(self):
        return self.name