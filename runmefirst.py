import os
import time


print('Pas pak do te instalohen modulet e nevojshme per ekzekutimin e programit.')

time.sleep(1)

try:
    print('Duke instaluar...')
    time.sleep(1)
    os.system('pip install ttkthemes')

except:
    print('Ju nuk jeni i lidhur me internetin')
