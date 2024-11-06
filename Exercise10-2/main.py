import random

_file_name = 'lotto.txt'
_file = open(_file_name, mode='w+', encoding='utf-8')
_dash = '\n---------------------------------------------------'

def generate_lotto(length, count):
    result = []
    for i in range(0, count):
        lotto = ''
        for n in range(0, length):
            r = random.randint(0, 9)
            lotto += str(r)

        result.append(lotto)

    return result

def write_lotto(lottoes):
    for (i, lotto) in enumerate(lottoes):
        t = f'{lotto}\t'
        if i > 0 and (i+1) % 5 == 0:
            if i != len(lottoes) - 1:
                t += '\n'

        print(t, end='', file=_file)

    print(_dash, file=_file)

#------------------------------------------------------------
print('รางวัลที่ 1', file=_file)
p = generate_lotto(6, 1)
write_lotto(p)

print('รางวัลเลขท้าย 2 ตัว', file=_file)
p = generate_lotto(2, 1)
write_lotto(p)

print('รางวัลเลขหน้า 3 ตัว', file=_file)
write_lotto(generate_lotto(3, 2))

print('รางวัลเลขท้าย 3 ตัว', file=_file)
write_lotto(generate_lotto(3, 2))

print('รางวัลที่ 2', file=_file)
write_lotto(generate_lotto(6, 5))

print('รางวัลที่ 3', file=_file)
write_lotto(generate_lotto(6, 10))

print('รางวัลที่ 4', file=_file)
write_lotto(generate_lotto(6, 50))

print('รางวัลที่ 5', file=_file)
write_lotto(generate_lotto(6, 100))

print(f'สร้างเรียงเบอร์เสร็จเรียบร้อย กรุณาตรวจสอบในไฟล์ {_file_name}')

_file.close()
