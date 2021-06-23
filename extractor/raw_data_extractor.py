import os
import csv

from pathlib import Path



def main():
    #print("Hello World")
    #file_names = os.listdir('data/box')
    path = Path('data/box')
    for child in path.iterdir():
        
        
        if child.is_file():
            file_name = child.name
            file_content = child.read_text()
            testsite_array = []
            with open(os.path.join(path,file_name), newline='') as my_file:
                reader = csv.reader(my_file)
                testsite_array = [row[-1] for row in reader]
                #testsite_array = my_file.readlines()
                #raw_content = ""
                #lst2 = [a + ' ' for a in testsite_array]
                #raw_content+= lst2
                #for eachLine in testsite_array:
                    # Split on last occurrence of delimiter
                    #comma_split_data= eachLine.rsplit(', ', 1)
                    #comma_split_data = eachLine.split(',')[-1]
                    #comma_split_data_with_tab_space = comma_split_data.replace("\n"," ")
                    #print(comma_split_data)
                    
                   
                print("")
                print("##### FOR FILE: "+file_name)
                print(*testsite_array)
                #print(lst2)   
                print("")
    
           # print(f"{child.name}:\n{child.read_text()}\n")

    #print(file_names)

main()    