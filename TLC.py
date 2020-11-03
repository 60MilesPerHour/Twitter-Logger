import hashlib

def Cleaner():
  output_file_path = "/home/miles/Desktop/Python 3/Cleaned.txt"
  input_file_path = "/home/miles/Desktop/Python 3/Dirty.txt" # YOU DEFINED THIS IN LINE 

  completed_lines_hash = set()

  output_file = open(output_file_path, "w")

  for line in open(input_file_path, "r"):

    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

    if hashValue not in completed_lines_hash:
      output_file.write(line)
      completed_lines_hash.add(hashValue)

  output_file.close()