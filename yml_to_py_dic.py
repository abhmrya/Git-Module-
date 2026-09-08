import yaml

with open("learning.yaml") as file:
    data = yaml.safe_load(file)

print(data)