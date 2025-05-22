from faker import Faker
fake = Faker()

titulo = "GENERATOR OF DATA"
print(titulo.center(120))
LOGO = '''
                   ____ 
                .-'    `-.
               /_...._   \\
               || ||||   |
               || ||||   |
              (|| ||||   |
              || ||||   |
              || ||||   |
             / ||||||   |
           .'  ||||||   |
        _.'    | ||||   |
     .-'       | ||||   |
    /          | ||||   |
   |    .-.    | ||||   |
   \\   (   )   | ||||   |
    '-.__.'    |______.-'
               |_| |_| 
             VV-Linux
'''

for linea in LOGO.strip('\n').split('\n'):
    print(linea.center(120))

print('-----------------------------------------------------------')


t = int(input("What size do you want the array?:"))

for A in range(t):
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print(fake.year())
    print(fake.date())
    print(fake.job())
    print(fake.phone_number())
    print(fake.city())
    print(fake.country())
    print(fake.state())
    print(fake.date_of_birth())
    print('-------------------------------')

