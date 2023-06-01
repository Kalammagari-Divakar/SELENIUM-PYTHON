import yaml
with open('read.config') as file:
    content = yaml.safe_load_all(file)
def config_read():
#with open("read.config") as filename:

   # content = yaml.safe_load_all(filename)
    #filename = "read.config"
    #content = open(filename).read()
    config = eval(content)
    username = config['username']
    password = config['password']
    platformlink = config['platformlink']
    print(username)
    print(password)
    print(platformlink)
    return(username,password,platformlink)
if __name__ == "__main__":

    config_read()

