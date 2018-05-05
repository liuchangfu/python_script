DB_FILE = 'staff_db.db'
COL = ['id', 'name', 'age', 'phone', 'dept', 'enrolled_date']

data = {}

for i in COL:
    data[i] = []
print(data)

f = open(DB_FILE, 'r', encoding='utf-8')
for line in f:
    staff_id, name, age, phone, dept, enrolled_date = line.split(',')
    data['id'].append(staff_id)
    data['name'].append(name)
    data['age'].append(age)
    data['phone'].append(phone)
    data['dept'].append(dept)
    data['enrolled_date'].append(enrolled_date)

print(data)
