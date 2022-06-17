import win32com.client as win32
import time
ea=win32.gencache.EnsureDispatch('Excel.Application')
ea.Visible=True
s="C:\\Users\\hardugga\\Desktop\\FS Asset List and Mapping.xlsx"
ewb=ea.Workbooks.Open(s)
print(ewb.Worksheets(1).Name)
ewb.Worksheets.Add()