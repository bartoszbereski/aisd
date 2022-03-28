import glob
import os
if __name__ == '__main__':
    f = glob.glob('zadanie1/*')
    for x in f:
       y = x.split('\\', 1)[1]
       path=y[0]
       try:
           os.mkdir(path)
       except OSError as error:
           print(error)
