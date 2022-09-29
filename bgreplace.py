# Desktop Background Changer
import os
from shutil import copyfile

#get Windows username
username = os.getlogin()
print(username)

# define location of directories to modify
themes_dir = "C:\\Users\\"+username+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes"
cached_dir = themes_dir+"\\CachedFiles"
new_file = "C:\\Users\\"+username+"\\Desktop\\bg.jpg"
transcoded_wp_file_path = themes_dir+"\\TranscodedWallpaper"

cached_wp_file = [f for f in os.listdir(cached_dir)][0]
cached_wp_file_path = cached_dir+"\\"+cached_wp_file


#remove default files
#os.remove(transcoded_wp_file_path)
#os.remove(cached_wp_file_path)

#copy new background to directories
copyfile(new_file, transcoded_wp_file_path)
copyfile(new_file, cached_wp_file_path)
  

  
