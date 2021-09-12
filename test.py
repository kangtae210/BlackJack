import openpyxl
import make_SHEET


make_SHEET.make_sheet()


apply = openpyxl.load_workbook(('apply.xlsx'))
apply_sheet = apply.active

locker = openpyxl.load_workbook(('locker.xlsx'))
locker_sheet = locker.active

apply_list = []
for cell in apply_sheet:
    element = []
    for i in range(8):
        element.append(cell[i].value)
    apply_list.append(element)

print(apply_list)


apply.save('apply.xlsx')
locker.save('locker.xlsx')
apply.close()
locker.close()

