import yaml
with open('read.config') as file:
    content = yaml.safe_load_all(file)
    print(content)
def cfg_read():
    file = "read.config"
#with open("read.config") as filename:

   # content = yaml.safe_load_all(filename)
    #filename = "read.config"
    #content = open(filename).read()
    cfg = eval(content)
    username = cfg['username']
    password = cfg['password']
    platformlink = cfg['platformlink']
    print(username)
    print(password)
    print(platformlink)
    #return(username,password,platformlink)
if __name__ == "__main__":
    cfg_read()

