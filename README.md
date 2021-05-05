# oistyle - the OIS styling library


## Why oistyle?
To standardize OIS styling across programming languages and frameworks. Our MS Office stack has great templates for styling, but for programming languages such as python, R, and javascript, no _common_ templates exist. But, if you've ever had to make publication-ready visualizations and you were too proud to copy your data to Excel, chances are that you've fiddled around with OIS styling yourself. 

This repo aims to bring together all these separate styling efforts. The goal is to provide importable templates for most if not all of the programming languages and visualization libraries we use at OIS, and that these templates all use the same source for basic styling. 

Here's how it works: this repo provides the styling basics and a framework so that the templates are installable as a library in various languages, and we rely on contributors to add templates for new visualisation tools. So if you have a template lying around: make a pull request! Also read the instructions for contributing below. 

In this MVP, we only support styling for the `plotly` library in python, R, and javascript. 

## Usage

### Python
In your preferred environment, run 

`pip install git+https://github.com/jbosga-ams/oistyle.git`

You can now import from the `oistyle.python` namespace like so:

`from oistyle.python.plotly import colors, line_chart_template`

See `src/examples/python_plotly.ipynb` for specific `plotly` usage and examples. 

## Contributing



## To do

MVP: 
- R
- js
- pull request van aram/bas?

Inhoud: 
- R markdown?
- More examples
- axis line vs gridline formatting
- Percentage mark at right position
