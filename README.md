pyROOT_files
============
has some useful pyroot files

# Included in repository 
    Combo_plot.py 
    
    1. simple plotting program, reads in .root file, saves to specified directory as pdfs and pngs

    root_file_reader.py

    1. takes input .root file, outputs to text file, 
    first level directories and files/subdirectories with TKey type for each file/subdirectory.
    includes parser for input file name

# Setup Combo_plot.py
    1. with editor, change file_name and dir_path to suit interests
    
    1. run as python file
    ```
    python Combo_plot.py
    ```

# Setup root_file_reader.py
    1. change name of output file if needed
    ```
    f=open("directories.txt", "w+")
    ```

    1. run with python including parser information for input file name
    ```
    python root_file_reader.py -i [file_name.root]

    note: the output file will by default be placed in the directory the function is being called from
