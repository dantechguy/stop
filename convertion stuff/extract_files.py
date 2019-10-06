# converter - provide a .sb3 file
import os
import zipfile

def extract_files_and_create_temp_folder(sb3Url):

  temp_folder_url = '{0}/{1}'.format(os.path.dirname(sb3Url), prefs.temp_folder_name)

  if os.path.exists(temp_folder_url):
    print('FAILED: \'{0}\' folder already exists. Please delete or rename this to continue.'.format(temp_folder_name))
    exit()

  unzip(sb3Url, temp_folder_url)


def unzip(start, finish):
  with zipfile.ZipFile(start, "r") as zip_ref:
      zip_ref.extractall(finish)
