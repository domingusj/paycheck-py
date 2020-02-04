import yaml


def readPayee(person_name):
    with open("testdata/directory.yml") as directory:
        try:
            directory = yaml.safe_load(directory)
        except yaml.YAMLError as exc:
            print(exc)

    for person in directory:
        if person['name'] == person_name:
            printCheck(person)


def printCheck(person):
    print("payment for " + person['name'])


readPayee("John Doe")
