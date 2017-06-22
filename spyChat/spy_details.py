import datetime
#Use class to improve reusability
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


class ChatMessages:

    def __init__(self,message,was_sent_by_me):
        self.message = message
        self.time = datetime.datetime.now()
        self.was_sent_by_me = was_sent_by_me
#Guest spy
spy = Spy("Pablo",'Mr.',24,5)

#Default friends
frnd1 = Spy('Gastavo', 'Mr.', 34, 2.3)
frnd2 = Spy('Cali', 'Mr.', 38, 4.3)
frnd3 = Spy('Blacky', 'Mr.', 37, 4.95)

friends = [frnd1,frnd2,frnd3]
