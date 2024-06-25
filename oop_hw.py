class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        print(f'The {type}, with the registration number: {reg_num} is owned by {owner}')
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(self.owner)
        
# me registering a car under my_name
subaru = Vehicle('123hb33', 'Subaru, Legacy', 'Blake McGuire')
# me changing the registratrion because it was sold
subaru.update_owner('Jerry Senifeld')


class Event:
        def __init__(self, name, date, attendees):
            self.name = name
            self.date = date
            self.attendees = attendees
        
        def add_participant(self, number):
            self.attendees += number
        
        def __str__(self):
            return f'Event Name: {self.name}, Date: {self.date}, Attendees: {self.attendees}'
            
# new event was scheduled at the hilton for my bday!
blakes_bday = Event('blakes bday', 'july 7th 2024', 1)
# no one rsvpd :(
blakes_bday.add_participant(1)
# my mom decided she would check it out and see if the party is bumpin or not
print(blakes_bday)