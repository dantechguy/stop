# converter - provide a .sb3 file
import os
import zipfile

def extract_files_and_create_temp_folder(sb3Url, temp_folder_name):

  temp_folder_url = '{0}/{1}'.format(os.path.dirname(sb3Url), temp_folder_name)

  if os.path.exists(temp_folder_url):
    print('FAILED: \'.temp\' folder already exists. Please delete or rename this to continue.')
    exit()

  unzip(sb3Url, temp_folder_url)


def unzip(start, finish):
  with zipfile.ZipFile(start, "r") as zip_ref:
      zip_ref.extractall(finish)
