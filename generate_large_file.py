import os

MB1 = 1024*1024 # 1GB
size = 24 # desired size in GB
with open('large_file.random', 'wb') as fout:
    for i in range(size + 1):
        fout.write(os.urandom(MB1))