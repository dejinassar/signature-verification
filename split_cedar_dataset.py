import os
import shutil
from sklearn.model_selection import train_test_split

original_genuine = 'signatures/full_org/'   
original_forgery = 'signatures/full_forg/' 

# Target folders
train_genuine = 'data/train/genuine'
val_genuine = 'data/val/genuine'
test_genuine = 'data/test/genuine'

train_forgery = 'data/train/forgery'
val_forgery = 'data/val/forgery'
test_forgery = 'data/test/forgery'

def split_and_copy(src_folder, train_folder, val_folder, test_folder, test_size=0.3, val_ratio=0.5):
    files = os.listdir(src_folder)
    train_files, temp_files = train_test_split(files, test_size=test_size, random_state=42)
    val_files, test_files = train_test_split(temp_files, test_size=val_ratio, random_state=42)
    
    for f in train_files:
        shutil.copy(os.path.join(src_folder, f), train_folder)
    for f in val_files:
        shutil.copy(os.path.join(src_folder, f), val_folder)
    for f in test_files:
        shutil.copy(os.path.join(src_folder, f), test_folder)

# Split genuine and forgery
split_and_copy(original_genuine, train_genuine, val_genuine, test_genuine)
split_and_copy(original_forgery, train_forgery, val_forgery, test_forgery)

print("Data split complete!")
