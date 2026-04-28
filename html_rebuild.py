import subprocess
import shutil
import os

def build_html():
    print("Building HTML documentation...")
    subprocess.run(r'docs\make.bat html', shell=True, check=True)


def copy_html():
    sanfran = os.path.join('docs', '_build', 'html')
    franfran = 'docs'
    print(f"Copying files from {sanfran} to {franfran} ...")
    
    for item in os.listdir(sanfran):
        s = os.path.join(sanfran, item)
        d = os.path.join(franfran, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

def clean_build():
    build_dir = os.path.join('docs', '_build')
    if os.path.exists(build_dir):
        print(f"Removing build folder {build_dir} ...")
        shutil.rmtree(build_dir)

if __name__ == '__main__':
    build_html()
    copy_html()
    clean_build()
    print("Done! Docs are ready for git commit.")
