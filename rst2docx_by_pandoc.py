import os


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print(files)
        
        for file in files:
            if os.path.splitext(file)[1] == ".rst":
                os.chdir(root)
                print(file," to ",file[:-4]+".docx")
                os.popen("pandoc " + file + " -o " + os.path.splitext(file)[0]+".docx").readlines()

if __name__ == "__main__":
    get_file_name(os.path.abspath(os.getcwd()))
