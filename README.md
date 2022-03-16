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