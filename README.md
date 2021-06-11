# SheCare
## Fuzzy Based Expert System for Detection of Breast Cancer
### _Built using Python ,MATLAB, Tkinter Framework_

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


> # Breast cancer 


Breast cancer constitutes as one of the fatal diseases in the world and about the major deaths among the female population is due to the prolonged time in the process of detection and reporting of the cancerous tissues in the affected part. The traditional pattern for detecting the disease is not rapid and requires time and special machined methods.

The raw dataset originally consisted of some missing values of attributes, the examples having missing attributes were removed to create a decision tree for the analysis of rule base. The derived rule base and the data base (membership functions) were fed into an inference engine which was based upon the Mamdani method. After fetching the results from the inference engine, defuzzification was carried. Defuzzification which is based upon the center of area most commonly known as centroid method was performed to obtain the single crisp output for the prediction of the sample.



## Features

-

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]



This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech
SheCare is built on top of the following technologies: 

- [Python](https://www.python.org) - Language used to create interfaces, models and connections with MATLAB Engine.
- [MATLAB](https://in.mathworks.com/products/matlab.html) - The computational and matehematics platfrom used to create fuzzy inference engine for fuzzification and defuzzification of inputs.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Package based on Py to create graphical user interface. 


## Installation

SheCare requires Python 3.9, MATLAB Fuzzy Toolbox and Jupyter to be installed on the system.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```




## License

MIT

**Free Software**




