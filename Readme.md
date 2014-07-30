# pelican skeleton

## first clone the skeleton

git clone git@oxford.saperea.com:skel/pelican.git ~/scratch/pelican

## then use it to scaffold in the current directory

workon mrbob
mrbob -w ~/scratch/pelican/skel

## create a new virtual environment with the same name as the project path

mkvirtualenv $PROJECT_NAME

## install requirements in virtual environment

pip install fabric pelican mr.bob markdown webassets BeautifulSoup4

## install pelican theme

pelican-themes -s ~/Work/$PROJECT_NAME/theme
