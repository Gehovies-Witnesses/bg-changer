# Desktop Background Changer
import os
from shutil import copyfile
from ctypes import windll

#get Windows username
username = os.getlogin()
print(username)

# Hide the users taskbar to scare the shit out of them...
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
windll.user32.ShowWindow(h, 9)

# define location of directories to modify
themes_dir = "C:\\Users\\"+username+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes"
cached_dir = themes_dir+"\\CachedFiles"
new_file = "C:\\Users\\"+username+"\\Desktop\\bg.jpg"
if os.path.exists(new_file):
  pass
else:
  new_file = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}\\bg.jp*"

transcoded_wp_file_path = themes_dir+"\\TranscodedWallpaper"

cached_wp_file = [f for f in os.listdir(cached_dir)][0]
cached_wp_file_path = cached_dir+"\\"+cached_wp_file


#copy new background to directories
copyfile(new_file, transcoded_wp_file_path)
copyfile(new_file, cached_wp_file_path)
  

  
