import paramiko
import getpass
import os

import tkinter as tk
from tkinter import simpledialog

def prompt_password():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("SSH Login", "Enter SSH Password:", show="*")
from tqdm import tqdm

def sftp_get_with_progress(sftp, remote_path, local_path):
    file_size = sftp.stat(remote_path).st_size
    with tqdm(total=file_size, unit='B', unit_scale=True, desc=os.path.basename(local_path)) as pbar:
        def callback(transferred, total):
            pbar.update(transferred - pbar.n)
        sftp.get(remote_path, local_path, callback=callback)

def main():
    hostname = "geussnow01"
    username = "bav"
    password = prompt_password()
    
    remote_base = "/home/bav/PROMICE-AWS-diagnostic/L3_test/sites"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    sftp = ssh.open_sftp()
    for res in ['month','day','hour']:
        local_base = f"../aws-l3-dev/csv/{res}"
        from pathlib import Path
    
        local_base = Path(local_base).resolve(strict=False)
        local_base.mkdir(parents=True, exist_ok=True)
        
        sftp.chdir(remote_base)
        sites = [d for d in sftp.listdir() if sftp.stat(f"{remote_base}/{d}").st_mode & 0o040000]
    
        os.makedirs(local_base, exist_ok=True)
    
        for site in sites:
                remote_file = f"{remote_base}/{site}/{site}_{res}.csv"
                local_file = os.path.join(local_base, f"{site}_{res}.csv")
                try:
                    sftp_get_with_progress(sftp, remote_file, local_file)
                except Exception as e:
                    print(f"Failed: {site} ({e})")
    
    sftp.close()
    ssh.close()
