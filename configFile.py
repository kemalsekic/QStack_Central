from configparser import ConfigParser

config = ConfigParser()
"""
config['DEFAULT'] = {

}
"""
file = open("config.ini", "w")

config.add_section('Person')
config.set('Person', 'Name', 'Todd')
config.set('Person', 'Age', '19')
config.set('Person', 'HasEyes', 'True')
config.set('Person', 'Password', 'e')


config.add_section('Counter')
config.set('Counter', 'Name', 'Todd')

config.write(file)
file.close()