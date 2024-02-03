import os, json, shutil

def check_if_exists(folder_name, path):
    return os.path.exists(os.path.join(path, folder_name))

def create_folder(folder_name, path):
    os.mkdir(os.path.join(path, folder_name))

def create_folder_for_new_dataset(ROOT_DIR, folder_name, path):
    os.mkdir(os.path.join(path, folder_name))
    landmarks = ['no_mans_land', 'vocal_cord', 'og_junction', 'body', 'antrum', 'pylorus', 'd1', 'd2', 'incisura', 'fundus']
    for landmark in landmarks:
        try:
            path_to_landmark_images_folder = os.path.join(path, folder_name, landmark)
            os.mkdir(path_to_landmark_images_folder)
        except:
            pass

    data = {
        'vocal_cord' : -1, 
        'og_junction' : -1, 
        'body' : -1, 
        'antrum' : -1, 
        'pylorus' : -1, 
        'd1' : -1, 
        'd2' : -1, 
        'incisura' : -1, 
        'fundus' : -1,
        'no_mans_land' : -1
    }
    with open(os.path.join(path, folder_name, "meta_data.json"), "w") as outfile:
        outfile.write(json.dumps(data, indent=4))

def get_first_level_folders_under_a_path(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def copy_file(source, destination):
    shutil.copy2(source, destination)

def count_the_number_of_folders(path):
    return len([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
