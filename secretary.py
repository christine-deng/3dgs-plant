import subprocess
import sys
import html_rebuild
import time

URL = "https://github.com/christine-deng/3dgs-plant.git"
DEFAULT_COMMIT_MSG = "Update documentation"

def remote_exists():
    result = subprocess.run(['git', 'remote'], capture_output=True, text=True)
    return 'origin' in result.stdout.split()

def set_remote(url):
    if remote_exists():
        print("Remote 'origin' exists. Updating URL...")
        subprocess.run(['git', 'remote', 'set-url', 'origin', url], check=True)
    else:
        print("Remote 'origin' does not exist. Adding remote...")
        subprocess.run(['git', 'remote', 'add', 'origin', url], check=True)

def run_git_commands(commit_message, url):
    try:
        set_remote(url)
        
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'master'], check=True)  # master branch
        
        print("Hooray! You pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    html_rebuild.build_html()
    html_rebuild.copy_html()
    html_rebuild.clean_build()
    time.sleep(2)
    commit_msg = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMIT_MSG
    run_git_commands(commit_msg, URL)
