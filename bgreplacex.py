# Desktop Background Changer
import os
from shutil import copyfile

#get Windows username
username = os.getlogin()
print(username)

# define location of directories to modify
themes_dir = "C:\\Users\\"+username+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes"
cached_dir = themes_dir+"\\CachedFiles"
new_file = "C:\\Users\\"+username+"\\Desktop\\bgx.jpg"
if os.path.exists(new_file):
  pass
else:
  new_file = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}\\bgx.jp*"

transcoded_wp_file_path = themes_dir+"\\TranscodedWallpaper"

cached_wp_file = [f for f in os.listdir(cached_dir)][0]
cached_wp_file_path = cached_dir+"\\"+cached_wp_file


#copy new background to directories
copyfile(new_file, transcoded_wp_file_path)
copyfile(new_file, cached_wp_file_path)
  

  
