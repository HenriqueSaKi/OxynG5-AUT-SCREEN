<h1><div align='center'>Automating Work Process</div></h1>
<div align='center'>
    <img src="http://img.shields.io/static/v1?label=python%20&message=3.8.3&color=yellow&logo=python"/>
    <img src="http://img.shields.io/static/v1?label=VS Code%20&message=1.47.3&color=blue&logo=visual-studio-code"/>
    <img src="http://img.shields.io/static/v1?label=status%20&message=concluded&color=-green"/>
    
</div>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using Python, I created this program capable of setup some webpages by itself. It helps me saving 15 minutes of my daily routine at work.

## Summary :pushpin:
- Frameworks
- Requiriments
- Installation Guide
- Links
- Run Application

## Frameworks :computer: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To be succeeded in this project I had to use some Python frameworks, like:
- Datetime
  - Timedelta
- Pyautogui
- Selenium
  - ActionChains
  - Expected_Conditions
  - Webdriver
  - WebDriverWait
- Time
- OS

##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Observation: Don't worry about installation, because it's going to be presented in the following topics.

## Requiriments :memo:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To run the program is important to have these programs and frameworks installed in your machine.
#### Program
- Python 3.8.3
- Visual Studio Code 1.47
#### Libraries
- Datetime
- Pyautogui
- Selenium

## Installation Guide :book:
- Programs:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accessing Python or Visual Studio Code website, you can easily download it's executable file and install.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Would you like to install it in another OS? Click [here](https://code.visualstudio.com/docs/setup/setup-overview) for install Visual Studio Code and [here](https://www.python.org/downloads/) for Python.
</br>

- Frameworks:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The following steps will present the basic form about how to install all libraries included in it's project in your Windows OS.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1- Press ```win``` + ```r```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2- Access your current path(where your scripts are installed) using the command ```cd <current path>```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3- Inside your current path, execute the command ```pip install -r requirements.txt```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4- Press ```enter``` and wait installation process


## Links :link:
#### Program
- [Python 3.8.3](https://www.python.org/)
- [Visual Studio Code 1.47](https://code.visualstudio.com/)
#### Libraries
- [Datetime](https://docs.python.org/3/library/datetime.html#)
- [Pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- [Selenium](https://selenium-python.readthedocs.io/)

## Run Application :arrow_forward: 
<div align="center">
    <img src="/Readme-Images/setup.gif" width="480" height="270">
</div>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First of all, the program have to have a account configured into each <b>"TelaX.py"</b>. So, you'll need to modify the code, like represented below in rows highlighted with the <u>breakpoint</u>:
</br>
<div align="center">
    <img src="/Readme-Images/login.PNG" width="526.5" height="188">
</div></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After followed the steps until here, there are two ways to run the application: </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clicking on it and executing with "python", like the example below:</br>

<div align="center">
    <img src="/Readme-Images/selecting-python.png" width="520.5" height="219.5">
</div></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Or transforming main script into a standalone program. Bellow there are some steps explaining how do you can do it.</br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1- Press ```win``` + ```r```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2- Access your current path(where your scripts are installed) using the command ```cd <current path>```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3- Inside your current path, execute the command ```pyinstaller <main file.py> --onefile```</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4- Double click the program inside "dist" folder.</br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, you just have to wait the program execute its function.
</br></br>
Document developed in HTML5 and Markdown by Henrique S. Kisaki
