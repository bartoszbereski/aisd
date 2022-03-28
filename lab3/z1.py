import glob, os, shutil
if __name__ == '__main__':
    f = glob.glob('zadanie1/*')
    for file in f:
       y = file.split('\\')[1]
       try:
         os.mkdir(f'zadanie1/{y[0]}')
       except FileExistsError:
           pass
       os.rename(f'{file}', f'zadanie1/{y[0]}/{y}')
