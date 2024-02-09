import os

def get_all_files_recursively(folder_path):
    files = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(foldername, filename))
    return files

# Replace 'your_folder_path' with the actual path of the folder you want to inspect
folder_path = '/media/tanjim/Tanjim/python/tools/huntAPI/wordlist'

file_list = get_all_files_recursively(folder_path)

listOfWords = []

# with open('/media/tanjim/Tanjim/python/tools/huntAPI/wordlist/all_words.txt', 'rb') as f:
#     words = f.read().decode('utf-8')
#     words = words.split()
#     for word in words:
#         listOfWords.append(word)

# print(listOfWords[:50])

print(f"Got total {len(file_list)} files. Starts reading:")
for file in file_list:
    print("Reading File: ", file)
    with open(file, 'rb') as f:
        try:
            # Decode bytes to string using utf-8
            words = f.read().decode('utf-8')
            
            # Split the content into words assuming space as a separator
            words = words.split()
            
            # Add unique words to the list
            listOfWords.extend(word for word in words if word not in listOfWords)
        except UnicodeDecodeError:
            print(f"Error decoding file: {file}")

for word in listOfWords:
    with open('/media/tanjim/Tanjim/python/tools/huntAPI/wordlist/all_words.txt', 'a') as f:
        f.write(word)
        f.write("\n")
