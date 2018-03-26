'''
Created on 2 ago. 2017

@author: luis
'''
from client_fva.person import PersonClient
from client_fva.user_settings import UserSettings

client = PersonClient(settings=UserSettings())
client.register()
client.authenticate('04-0212-0119')

client.authenticate('04-0212-0119', wait=True)
client.sign('08-0888-0888',  None, "Readme file test", file_path='README.md', wait=True)

client.validate(None, file_path='README.md')
client.validate(None, file_path='README.md', _format='pdf')
client.is_suscriptor_connected('08-0888-0888')
