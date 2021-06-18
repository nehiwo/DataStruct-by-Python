# -*- coding: utf-8 -*-
#openpyxl

import openpyxl as xl

if __name__ == "__main__":
    wb = xl.Workbook()
    wb.save("Sample.xlsx")
