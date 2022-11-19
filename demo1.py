import os
for root, dirs, files in os.walk('/Users/[username]/Desktop'):
    for file in files:
        if file.endswith('.docx'):
            print(os.path.join(root, file))
