import os
import sys
import winshell
from win32com.client import Dispatch

def create_shortcut(name, target, working_dir=None, icon=None):
    shortcut_path = os.path.join(winshell.desktop(), f"{name}.lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = working_dir if working_dir else os.path.dirname(target)
    shortcut.IconLocation = icon if icon else target
    shortcut.save()
    print(f"Shortcut '{name}' created on the desktop.")

def main():
    print("TurboGuard - Desktop Shortcut Creator")
    while True:
        print("\nOptions:")
        print("1. Create File Shortcut")
        print("2. Create URL Shortcut")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter shortcut name: ")
            target = input("Enter full path to the file: ")
            working_dir = input("Enter working directory (leave blank for default): ") or None
            icon = input("Enter path to icon file (leave blank for default): ") or None
            create_shortcut(name, target, working_dir, icon)

        elif choice == '2':
            name = input("Enter shortcut name: ")
            url = input("Enter URL: ")
            create_shortcut(name, url)

        elif choice == '3':
            print("Exiting TurboGuard.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()