from datetime import datetime

filename = 'Imp.txt'

with open(filename, 'a') as f:
    now = datetime.now()
    f.write(f'Today is {now.strftime("%Y-%m-%d")}\n')
    f.write(f'This one is for you david\n')