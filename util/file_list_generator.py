########################################
# Jiasheng Wu
# Oct 16, 2018
########################################
import os

folder_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

input_path = folder_path + '/input.txt'
output_path1 = folder_path + '/util/file_list.txt'
output_path2 = folder_path + '/util/output_name.txt'

data = []

with open(input_path, mode='r') as input_file:
    for line in input_file:
        line = line.strip().strip('\n')
        if not line == '' and not line.startswith('#'):
            # output_file.write(line + '\n')
            data.append(line)
    # print(data)

url_prefix = data[0]
ts_file_num = int(data[1])

with open(output_path1, mode='w') as output_file:
    for i in range(1, ts_file_num + 1):
        # print("file '" + url_prefix + str(i) + ".ts'")
        output_file.write("file '" + url_prefix + str(i) + ".ts'\n")

output_name = data[2]

with open(output_path2, mode='w') as output_file:
    output_file.write(output_name)
