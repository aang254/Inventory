import os

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
print(os.path.join(BASE_DIR, '..\\secrets.json'))
print(os.path.abspath('..\STOCK_Print'))

#os.startfile("D:\\Django-Project\\STOCK_Print\\LOT_3.pdf", "print")