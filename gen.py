import os
try:
    for i in range(7,31):
        os.mkdir(f'Day{i}')
except OSError as error:
    print(error)