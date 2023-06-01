import yaml
from pprint import pprint
obj="C:\\Users\\uif48567\\PycharmProjects\\Selenium-Python\\prac.yaml"
l=[]
with open("prac.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    pprint((data))
for i in data:
    if 'item' in i:
        print(data[i])
        l.append(data[i])
print(l)

