import person_pb2

person = person_pb2.Person()
person.id = 1234
person.name = "Gunmo"
person.email = "gunmo@gunmo.com"

phone = person.phones.add()
phone.number = "555-4321"
phone.type = person_pb2.Person.HOME

# person.no_such_field = 1  # raises AttributeError
# person.id = "1234"  # raises TypeError

print(person, phone)
