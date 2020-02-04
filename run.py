import yaml


def readPayee(person_name):
    with open("testdata/directory.yml") as directory:
        try:
            directory = yaml.safe_load(directory)
        except yaml.YAMLError as exc:
            print(exc)

    person_found = False
    for person in directory:
        if person['name'] == person_name:
            person_found = True
            printCheck(person)
    if not person_found:
        print(person_name + " not found!")


def printCheck(person):
    print("payment for " + person['name'])


readPayee("John Doe")
