# Opensource-UW Webpage With Flask
These are the source codes for the webpage of the club, "OpenSource-UW".<br>
We developed the website using bootstrap and Flask.<br>
If you want to contact us, please email to us (openuw@uw.edu).

# Deployment Instructions: 

1. Clone or Fork this directory

2. Install Flask by typing this into your command line tool (Git Bash or Mac Terminal): 
```python
    pip install Flask
```
3. In order to run this locally, type this into your command line tool:
```python
    FLASK_APP=opensource.py flask run
```
4. Now go to http://127.0.0.1:5000/ where the webpage is now up and running!

# Editing the website

This website differes from most websites that you may have seen because this uses flask. Flask is a microframework that allows us to use python to make certain aspects of deploying and maintaining a website easier. 

Here is the tree for the entire app. 
![treebois](http://puu.sh/zwqgM/e7e725e6e7.png)

For editing the webpages, you will have to edit the various HTML files located in the "templates" section. 

Once you have saved the edited HTML files, you will be able to see your changes in real time and not have to type everything over and over again!

Have Questions? <br>
Let us know by posting an issue!