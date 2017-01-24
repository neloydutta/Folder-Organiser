#  *** Folder Organiser :D ***
import os
import argparse
import json

type_map = {}

folder_location = "empty"

def get_foldername(fname):
    fname = fname.lower()
    if fname == "music":
        return "Music"
    elif fname == "vidoes":
        return "Videos"
    elif fname == "codes":
        return "Codes"
    elif fname == "documents":
        return "Documents"
    elif fname == "images":
        return "Images"
    elif fname == "compressed":
        return "Compressed"
    else:
        return None

def organise():
    esc_flag = "empty"
    for filename in os.listdir(folder_location):
        filelocation = os.path.join(folder_location, filename)
        if os.path.isfile(filelocation):
            file, ext = os.path.splitext(filename)
            if ext in type_map:
                folder = type_map[ext]
            else:
                folder = "UnIdentified"
            folderloc = os.path.join(folder_location, folder)
            if not os.path.exists(folderloc):
                os.makedirs(folderloc)
            i=1
            while True:
                try:
                    os.rename(filelocation, os.path.join(folderloc,filename))
                    break
                except:
                    filename1 = file + str(i) + ext
                    while True:
                        if os.path.exists(os.path.join(folderloc,filename1)):
                            i+=1
                            filename1 = file + str(i) + ext
                            continue
                        else:
                            break
                    if esc_flag == "empty":
                        print("File name, "+filename+", already exists is destination!\nDo you want to change its name to, "+filename1+", and move?(y/n/yforall/nforall)")
                        while True:
                            ip = raw_input()
                            if ip == "y" or ip == "n" or ip == "yforall" or ip == "nforall":
                                break
                            else:
                                print("Enter valid input! (y/n/yforall/nforall)")
                                continue
                    elif esc_flag == "yforall":
                        ip = "y"
                    else:
                        ip = "n"
                if ip == "yforall":
                    esc_flag = "yforall"
                    filename = filename1
                    continue
                elif ip == "nforall":
                    esc_flag = "nforall"
                    break
                elif ip == "y":
                    filename = filename1
                    continue
                else:
                    break

def update_typemap(ext, fname):
    fname = get_foldername(fname)
    if fname == None:
        print("Invalid type mentioned! Here are valid types to choose from:\nMusic, Videos, Documents, Images, Compressed and Codes.")
    else:
        if not ext.startswith("."):
            print("Invalid Extension!")
        else:
            if ext not in type_map.keys():
                type_map[ext] = fname
                print("Category of "+ext+" updated to "+fname)
            elif ext in type_map.keys() and fname != type_map[ext]:
                print("Category of "+ext+" updated from "+type_map[ext]+" to "+fname)
            else:
                print("Category of "+ext+" updated to "+fname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Folder Organiser')
    parser.add_argument("-l", "--location", help="Location of Folder to be organised! '[-l|--location] <location>'", default="empty")
    parser.add_argument("-a", "--addtype", nargs=2, help="Add new unknown type! '[-a|--addtype] <.extension><space><type>'", default="empty")
    args = parser.parse_args()

    with open('typemap.json') as json_data:
        type_map = json.load(json_data)

    if args.addtype != "empty":
        update_typemap(args.addtype[0], args.addtype[1])

    if args.location != "empty":
        folder_location = args.location
        if not os.path.exists(folder_location):
            print("Invalid location!")
        else:
            organise()

    with open('typemap.json', 'w') as outfile:
        json.dump(type_map, outfile)