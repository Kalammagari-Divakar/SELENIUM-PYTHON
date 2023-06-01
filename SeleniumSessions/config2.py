import yaml
with open('config.yaml') as file:
    content = yaml.safe_load_all(file)

    print(type(content))
    print(next(content))
