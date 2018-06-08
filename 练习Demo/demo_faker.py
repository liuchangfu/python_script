from faker import Faker
fake = Faker('zh-cn')

print(fake.name())

print(fake.address())

for _ in range(10):
  print(fake.name())


print(fake.street_name())