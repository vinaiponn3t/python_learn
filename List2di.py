#List
datas = [['rank','name','surname','role','address','tel'],
     ['พ.ท.','วินัยพณณ์','อ่อนหวาน','หัวหน้าฝ่ายกรรมวิธีข้อมูล','ฉะเชิงเทรา','0855601955'],
     ['พ.ท.','แดนชัย','เทียนเมืองปัก','','ฉะเชิงเทรา',''],
     ['พ.อ.','ธนา','พรหมจันทร์','','ชลบุรี','']]

#datas[0].append('birth')
datas[0] += ['birth','crma']
print(datas[0])

# print(datas[1][1],datas[1][2])


"""
for n in datas:
    for a in n:
        print(a,'',end='')
    print()
"""