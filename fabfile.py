from fabric.api import local


def myfunct():
	local("cd /home/karunakar/python/scripts/github-devops && mkdir devops dev1 dev2")
	local("cd /home/karunakar/python/scripts/github-devops && git add . && git commit -m 'firstcommit'")
	local("cd /home/karunakar/python/scripts/github-devops && git push origin  master")
  
