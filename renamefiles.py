import os
from os import path
import shutil

source_path = r"C:\Users\onyeo\Pictures\Trial\BodyCamfolder"
destination_path = r"C:\Users\onyeo\Pictures\Trial\Destination"

def main():
    for count, filename in enumerate(os.listdir(source_path)):
        dst =  "Frame_" + str(count) + ".jpg"

        # rename all the files
        os.rename(os.path.join(source_path, filename),  os.path.join(destination_path, dst))

# Driver Code
if __name__ == '__main__':
    main()