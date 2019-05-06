# converter - provide a .sb3 file
import os
import zipfile

def extractFilesAndCreateTempFolder(sb3Url):

  tempFolderName = '.temp'
  tempFolderUrl = '{0}/{1}'.format(os.path.dirname(sb3Url), tempFolderName)

  if os.path.exists(tempFolderUrl):
    print('FAILED: \'.temp\' folder already exists. Please delete or rename this to continue.')
    exit()

  unzip(sb3Url, tempFolderUrl)


def unzip(start, finish):
  with zipfile.ZipFile(start, "r") as zip_ref:
      zip_ref.extractall(finish)
