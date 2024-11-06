import os

_file_name = 'contact.txt'

name = input('ชื่อ >>')
phone = input('เบอร์โทรศัพท์ >>')

try:
    if not os.path.exists(_file_name):
        file = open(_file_name, 'w+')
        file.close()

    file = open(_file_name, mode='r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        if line.find(phone) != -1:
            raise Exception('เบอร์โทรนี้มีอยู่แล้ว ข้อมูลไม่ถูกบันทึก')
            #break   ไม่จำเป็นต้องใช้ break เพราะคำสั่ง raise ส่วนที่เหลือจะถูกยกเลิกอยู่แล้ว

    file.close()

    file = open(_file_name, mode='a+', encoding='utf-8')
    file.write(f'{name},{phone}\n')
    file.close()
    print('ข้อมูลถูกบันทึกแล้ว')
except Exception as err:
    print(err)
