
# Generation of fake Data
from faker import Faker as fk

f = fk('en_IN')

# datetime.date(2025, 3, 12)
# f.date_between(start_date='-5m', end_date='+5m') # m, y, d for month year days

# fake.date_time_between(start_date='-30y', end_date='now')
# datetime.datetime(2007, 2, 28, 11, 28, 16)

for i in range(10):
    print('----------------')
    t = f'''
    Name : {f.name()}
    Address : {f.address()}
    Email : {f.email()}
    Contact : {f.phone_number()}
    Date : {f.date_between(start_date='-5m', end_date='+5m')} 
    '''
    print(t)
