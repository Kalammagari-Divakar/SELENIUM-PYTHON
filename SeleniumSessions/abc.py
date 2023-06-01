from configparser import ConfigParser
config = ConfigParser()
config.read('config.yaml')
print(config.sections())
print(config['teacher']['name'])
#adding section
#config.add_section('student')
#config.set('student','name','nobody')
#with open('config.yaml','w')as file:
 #   config.write(file)
#editing section
config.set('student','name','no_body'  )
with open('config.yaml','w')as file:
    config.write(file)
#removing section
#config.remove_section('student')
#with open('config.yaml','w')as file:
    #config.write(file)