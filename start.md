# install miniconda with python3.8@windows
https://docs.conda.io/en/latest/miniconda.html#installing

https://docs.conda.io/projects/conda/en/latest/commands.html

conda update conda

python -m venv .venv

.\.venv\Scripts\activate.bat

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