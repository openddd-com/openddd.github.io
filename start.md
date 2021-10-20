# install miniconda with python3.8@windows; 3.9
https://docs.conda.io/en/latest/miniconda.html#installing

https://docs.conda.io/projects/conda/en/latest/commands.html

conda update conda

python3 -m venv .venv

#windows
.\.venv\Scripts\activate
#linux
. .venv/bin/activate
python -m pip  install --upgrade pip
python -m pip install --upgrade setuptools wheel lektor
# refer
https://www.getlektor.com/docs

Then execute the quickstart command to create a new project
```
    lektor quickstart
```
# Running your Project
lektor server

# update the webpack files

lektor server -f webpack

# Accessing the Admin
http://127.0.0.1:5000/admin/

# Creating A Package and restart server

lektor dev new-plugin

lektor plugins list


# update image

https://resize.imageonline.co/

https://ps.gaoding.com/#/

# publish

git remote add upstream git@github.com:openddd-com/openddd.github.io.git

git fetch upstream

git rebase upstream/lektor

# refer
https://www.getlektor.com/docs/
https://github.com/lektor/lektor-website
https://docs.beeware.org/en/latest/

# node -i node-sass
npm config set registry https://registry.npm.taobao.org
npm install node-sass

