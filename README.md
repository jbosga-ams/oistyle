# oistyle


## How it works:

- alles in 1 repo op GitHub
- toplevel heeft een json met de algemene styling erin
- folders per taal (R, python, js)
- files per framework in de juiste folders (bv. plotly.py in de folder python)
- templates in files, de files importeren toplevel styling json
- toplevel heeft zowel setup.py als package.json etc
- repo is direct te installeren als library via npm en pip via github, zie https://stackoverflow.com/questions/17509669/how-to-install-an-npm-package-from-github-directly. Dit werkt niet via Gitlab, vandaar Github.
- importeer het juiste template, bv voor python plotly: from oistyle.python.plotly import template


## To do

- R markdown?
- More examples
- axis line vs gridline formatting
- Percentage mark at right position
