# -*- coding: utf-8 -*- 
import json
import os
import string

from git import Repo
from pprint  import pprint

dev_repo_file="/vagrant/shell_build_scripts/dev_repos.json"
cpsproject_path='/home/vagrant/cpswt'

with open(dev_repo_file) as json_data:

    dev_repo = json.load(json_data)
    gituser = dev_repo['gituser']
    repsite = dev_repo['repo_site']
    cmd = "ssh-keyscan " + repsite + " >> /home/vagrant/.ssh/known_hosts"
    os.system(cmd)
    
    for i in dev_repo['git_repos']:
        #print(i['directory'])
        #print(i['url'])
        repo_directory = i['directory']
        repo_url = i['url']
        new_repo_url = string.replace(repo_url, 'gituser', gituser)
        #print(new_repo_url)
        repo_path = os.path.join(cpsproject_path, repo_directory)
        #print repo_path
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        os.chdir(repo_path)
        Repo.clone_from(new_repo_url, repo_path)


