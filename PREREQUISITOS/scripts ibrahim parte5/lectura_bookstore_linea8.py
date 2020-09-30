import os
path = os.path.join('scripts ibrahim parte5/files', 'bookstore.txt')
with open(path, 'r') as f:
  data = f.readlines()

print(data[7])