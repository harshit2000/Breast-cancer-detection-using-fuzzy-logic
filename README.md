# SheCare
## Fuzzy Based Expert System for Detection of Breast Cancer
### _Built using Python ,MATLAB, Tkinter Framework_

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Made with MATLAB](https://img.shields.io/badge/Built%20With-MATLAB-blue?style=for-the-badge&logo=appveyor)](https://in.mathworks.com/?s_tid=gn_logo)


[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kdziARCjrVUgYILNEDWGcxMoEQVpXybS?usp=sharing)


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


> # About the Project / Research


Breast cancer constitutes as one of the fatal diseases in the world and about the major deaths among the female population is due to the prolonged time in the process of detection and reporting of the cancerous tissues in the affected part. The traditional pattern for detecting the disease is not rapid and requires time and special machined methods.

The raw dataset originally consisted of some missing values of attributes, the examples having missing attributes were removed to create a decision tree for the analysis of rule base. The derived rule base and the data base (membership functions) were fed into an inference engine which was based upon the Mamdani method. After fetching the results from the inference engine, defuzzification was carried. Defuzzification which is based upon the center of area most commonly known as centroid method was performed to obtain the single crisp output for the prediction of the sample. 

## Demo

https://user-images.githubusercontent.com/43119465/121770619-efda0b80-cb87-11eb-8dfb-4a6282dbbe85.mp4

## Features

- Compact and fast
- Cloud processing capabilities
- Precision ready values
- Lightweight application and easy to containerise

> # Flow of the Process
> ![flow](https://user-images.githubusercontent.com/43119465/121770749-d2f20800-cb88-11eb-9de1-03b7d9076f15.png)

Kindly refer to Fuzzy Logics and Mamdani Method for FIS to learn more about the project.


## Tech
SheCare is built on top of the following technologies: 

- [Python](https://www.python.org) - Language used to create interfaces, models and connections with MATLAB Engine.
- [MATLAB](https://in.mathworks.com/products/matlab.html) - The computational and matehematics platfrom used to create fuzzy inference engine for fuzzification and defuzzification of inputs.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Package based on Py to create graphical user interface. 


> ## Installation

SheCare requires Python 3.9, MATLAB Fuzzy Toolbox and Jupyter to be installed on the system.


```sh
Open the GUI Folder and install the dependencies
cd "matlabroot\extern\engines\python"
python setup.py install

```
Or
```sh
cd "c:\Program Files\MATLAB\R2019b\extern\engines\python" 
python setup.py install --prefix="c:\work\matlab19bPy36"
```
- Set up the MATLAB Toolbox with your account
- Update the main.ipnyb on your local system and run all the cells

The windows application is ready to be installed with the .exe file in GUI folder. Install and run. If the engine is running on your local system with correct endpoints, correct output will be generated in the window.

## License
MIT

_This project is not OPEN SOURCED. Copying or stealing any part of the code or reproducing the files at another place without the prior knowledge of the owner can lead to strict actions/jurisdiction as part of the license. Kindly avoid this._

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)  By Team Genesis









