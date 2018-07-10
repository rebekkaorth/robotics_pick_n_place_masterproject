import os
import sys
import json
import urllib
from urllib.request import urlopen

"""
[1] Berk Calli, Aaron Walsman, Arjun Singh, Siddhartha Srinivasa, Pieter Abbeel, and Aaron M. Dollar, Benchmarking in 
    Manipulation Research: The YCB Object and Model Set and Benchmarking Protocols, IEEE Robotics and Automation 
    Magazine, pp. 36 – 52, Sept. 2015.

[2] Berk Calli, Arjun Singh, James Bruce, Aaron Walsman, Kurt Konolige, Siddhartha Srinivasa, Pieter Abbeel, 
    Aaron M Dollar, Yale-CMU-Berkeley dataset for robotic manipulation research, The International Journal of 
    Robotics Research, vol. 36, Issue 3, pp. 261 – 268, April 2017.

[3] Arjun Singh, James Sha, Karthik S. Narayan, Tudor Achim, and Pieter Abbeel, BigBIRD: A Large-Scale 3D Database 
    of Object Instances, in International Conference on Robotics and Automation, 2014.

"""

output_directory = "./ycb"

# You can either set this to "all" or a list of the objects that you'd like to
# download.
# objects_to_download = "all"
"""
objects_to_download = ["001_chips_can", "002_master_chef_can", "003_cracker_box", "004_sugar_box",
                       "005_tomato_soup_can", "006_mustard_bottle", "007_tuna_fish_can", "008_pudding_box",
                       "009_gelatin_box", "010_potted_meat_can", "011_banana", "012_strawberry", "013_apple",
                       "014_lemon", "015_peach", "016_pear", "017_orange", "018_pulm", "019_pitcher_base",
                       "021_bleach_cleanser", "022_windex_bottle", "023_wine_glass", "024_bowl", "025_mug",
                       "026_sponge", "027_skillet", "029_plate", "030_fork"
                       ]
                       """
objects_to_download = ["002_master_chef_can"]

# You can edit this list to only download certain kinds of files.
# 'berkeley_rgbd' contains all of the depth maps and images from the Carmines.
# 'berkeley_rgb_highres' contains all of the high-res images from the Canon cameras.
# 'berkeley_processed' contains all of the segmented point clouds and textured meshes.
# 'google_16k' contains google meshes with 16k vertices.
# 'google_64k' contains google meshes with 64k vertices.
# 'google_512k' contains google meshes with 512k vertices.
# See the website for more details.
# files_to_download = ["berkeley_rgbd", "berkeley_rgb_highres", "berkeley_processed", "google_16k", "google_64k", "google_512k"]
files_to_download = ["berkeley_processed"]

# Extract all files from the downloaded .tgz, and remove .tgz files.
# If false, will just download all .tgz files to output_directory
extract = True

base_url = "http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/data/"
# http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/data/berkeley/001_chips_can/001_chips_can_berkeley_rgbd.tgz
objects_url = base_url + "objects.json"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)


def fetch_objects(url):
    response = urlopen(url)
    html = response.read()
    objects = json.loads(html)
    return objects["objects"]


def download_file(url, filename):
    u = urlopen(url)
    f = open(filename, 'wb')
    meta = u.info()
    file_size = 1  # int(meta.getheaders("Content-Length")[0])
    print("Downloading: %s (%s MB)" % (filename, file_size/1000000.0))

    file_size_dl = 0
    block_sz = 65536
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl/1000000.0, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)
    f.close()


def tgz_url(object, type):
    if type in ["berkeley_rgbd", "berkeley_rgb_highres"]:
        return base_url + "berkeley/{object}/{object}_{type}.tgz".format(object=object, type=type)
    elif type in ["berkeley_processed"]:
        return base_url + "berkeley/{object}/{object}_berkeley_meshes.tgz".format(object=object, type=type)
    else:
        return base_url + "google/{object}_{type}.tgz".format(object=object, type=type)


def extract_tgz(filename, dir):
    tar_command = "tar -xzf {filename} -C {dir}".format(filename=filename, dir=dir)
    os.system(tar_command)
    os.remove(filename)


def check_url(url):
    try:
        request = urllib.request.Request(url).full_url
        print(request)
        request.get_method = lambda: 'HEAD'
        response = urlopen(request)

        return True
    except Exception as e:
        return False


def download_files():

    objects = objects_to_download

    for object in objects:
        if objects_to_download == "all" or object in objects_to_download:
            for file_type in files_to_download:
                url = tgz_url(object, file_type)
                # if not check_url(url):
                    # continue
                filename = "{path}/{object}_{file_type}.tgz".format(path=output_directory,
                                                                    object=object,
                                                                    file_type=file_type)
                print(filename)
                download_file(url, filename)
                if extract:
                    extract_tgz(filename, output_directory)
