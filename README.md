## install Flask
pip3 install Flask

## cli commands

```
touch run.py        <-- preferred for this project
```
    or

```
touch app.py
```


(naming conventions)


## more cli commands
python3 01*/01*/run.py

## how to jinja 
{{ url_for('index') }}

## PEP8 compliant
2 blank lines separate each function

## error messages very helpful in flask
look for your code half way down page 
for file and line number of error

## key shortcut
ctrl shift k
delete line of code

## NB
{{ url_for('careers') }}
{{means outut to screen or}}

{{ url_for('index') }}
in this case 

```
            <li><a href="{{ url_for('index') }}">Home</a></li>
```

href


the 
    {% block content %}
{%}
are for control flow of statements
    - e.g. for loop
    - if statement
    - or this block element

    {% extends "base.html" %}
    {% block content %}
        <h1>Home Page</h1>
    {% endblock %}


## url for Bootstrap
wget https://github.com/StartBootstrap/startbootstrap-clean-blog/archive/refs/tags/v5.0.10.zip

## bootstrap template
https://startbootstrap.com/themes
https://startbootstrap.com/theme/clean-blog
https://github.com/startbootstrap/startbootstrap-clean-blog/archive/gh-pages.zip

this last one is the save as on the download link


updated command:
wget https://github.com/StartBootstrap/startbootstrap-clean-blog/archive/refs/tags/v5.0.10.zip

## cli commands
mkdir static
cd static
wget https://github.com/StartBootstrap/startbootstrap-clean-blog/archive/refs/tags/v5.0.10.zip
ls
unzip v5.0.10.zip
cd -
<!-- last command takes us back to previous directory -->

note static files and folders are already in 02*/01*
however, wget command necessary above

## start again

```
pip3 install Flask
```

```
python3 02*/02*/run.py
```

click open browser in poup


## amp-what.com
https://www.amp-what.com/

## see flask / using if
for left right alternating display

## jinja templates
https://jinja.palletsprojects.com/en/3.0.x/

- Template Designer Documentation
    - List of Builtin Filters

## to conform code to template
highlight code
right click
click format selection 


## install heroku plugin
heroku login -i

## heroku
heroku apps

## optional
heroku apps:rename <<new-name>> --<<app-being-referenced>>
                                    where app is cloud project

## note
every heroku app comes with its own url
    - link to submit
as well as its own
git url

## docs
https://devcenter.heroku.com/articles/heroku-cli

## create app
heroku create

## next
if necessary not already linked to git:
git init
not needed

git add -A
same as
git add .


git commit -m "Message"

if type
git remote -v
gives verbose output about the remotes that I have

## push
git push -u heroku master


## command line output
remote:  !     No default language could be detected for this app.


remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !       Push rejected

## note
Github recently changed the name of its default branch from master to main
As a result, the command git push -u heroku master 

 will throw the following error:

error: src refspec master does not match

To solve this issue, please use the this command instead: git push -u heroku main

