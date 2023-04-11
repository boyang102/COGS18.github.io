#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - CL1 due Fri (tomorrow) at 11:59 PM (typically labs due Wednesdays)
# - Pre-course survey "due" (for EC) Fri (tomorrow) at 11:59 PM
# 
# Notes:
# 1. Remeber to click the link on Canvas/the course website to get each day's notes on datahub
# 2. Sign up/login to ClassQuestion: https://classquestion.com/students (Course code: FBXTD)
# 3. Due dates will be 11:59 PM this quarter
# 

# 4. syllabus has been updated
# - coding lab staff
# - due date times
# - clear that one CL will be dropped
# - OHs begin week 2 (we'll finalize days/times/locations this week)

# # Tools
# 
# - Python
# - datahub
# - Jupyter Notebooks
# - Anaconda
# - Academic Integrity

# This notebook will guide through the tools you will need for class materials and assignments, and how to get them. 

# #### Class Question #1
# 
# **How excited are you for COGS 18?**
# 
# - A. Super excited!  
# - B. The most excited!  
# - C. Couldn't be more excited!  
# - D. I love the smell of programming in the morning!  

# ### Prerequisites
# 
# This course and associated materials do not presume any prior knowledge of Python, or programming in general. 
# 
# To work with the course materials, you will need make sure you have access to the tools tools described here on datahub. 
# 
# It will be helpful for the final project if they are also installed on the computer you will be using. 
# 
# None of the materials are computationally heavy. 

# ### What do you need?
# 
# - **Required**: Access to datahub 
#     - Python (datahub uses python v3.9)
#     - Jupyter Notebooks
# 

# <center><img src="img/python.png" width="450px"></center>

# <div class="alert alert-success">
# Python is a programming language, whose development is led by the Python Software Foundation (PSF). 
# </div>
# 
# <div class="alert alert-info">
# The official Python organization website is available <a href="https://www.python.org" class="alert-link">here</a>.
# </div>

# ## Python
# 
# - Versions: there are different versions of Python.
#     - We will be using 3.9 on datahub (>3.6 required)
# - Packages: Python includes a "base set" of code (the standard library), and an extensive ecosystem of third party packages
#     - In this course, we will largely focus on the standard library
#     - For access to other packages when we need them, we will use Anaconda

# <center><img src="img/jupyter.png" width="300px"></center>

# <div class="alert alert-success">
# Jupyter notebooks are a way to intermix code, outputs and plain text. 
# They run in a web browser, and connect to a kernel to be able to execute code. 
# </div>
# 
# <div class="alert alert-info">
# The official Jupyter website is available 
# <a href="http://jupyter.org" class="alert-link">here</a>.
# </div>

# ## JupyterHub
# 
# <div class="alert alert-success">
# JupyterHub allows Jupyter notebooks to be shared across multiple users.
# </div>
# 
# <div class="alert alert-info">
# The official JupyterHub website is available 
# <a href="https://jupyterhub.readthedocs.io/en/stable/" class="alert-link">here</a>.
# </div>
# 

# ### Datahub
# 
# UCSD hosts its version of JupyterHub and calls it datahub. This is what you'll be using in class.
# 
# It is available here: http://datahub.ucsd.edu

# <center><img src="img/datahub.png" width="800px"></center>

# ### When to use Datahub?
# 
# - Course Lecture Slides
# - CodingLabs
# - Assignments
# - Final Project/Exam

# #### Lecture Slides:
# 
# Once you've logged into datahub, click on the the following link: https://datahub.ucsd.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCOGS18%2FLectureNotes-COGS18&urlpath=tree%2FLectureNotes-COGS18%2F&branch=main
# 
# (This link is also on the Canvas home page.)

# #### CodingLabs & Assignments:
# - Fetch & complete on datahub
# - do not change file names
# - do not copy cells provided
# - adding cells *is* allowed!
# - `print()` statements encouraged

# - For Submission:
#     - Before you click submit, make sure it's the thing you want to submit
#     - You ***must click submit***.
# 
#     - Always check that the CodingLab/Assignment/Exam shows up under "submitted assignments"
#     - You can submit as many times as you want
#     - We only have access to your most recent submission
#     - If you submit past the deadline, we will only have access to your late submission

# ### A note about: Timezones
# 
# - Due Dates are in UTC
# - All deadlines are 11:59 PM PST/PDT
# 
# ![Timezones](img/Timezones.png)
# 
# TimeZones: https://www.timeanddate.com/time/map/

# ## Jupyter Notebooks
# 
# - Markdown
# - code cells

# <div class="alert alert-success">
# Jupyter notebooks are a way to combine executable code, code outputs, and text into one connected file.
# </div>
# 
# <div class="alert alert-info">
# The official documentation from project Jupyter is available 
# <a href="https://jupyter-notebook.readthedocs.io/en/stable/" class="alert-link">here</a>
# and they also have some example notebooks 
# <a href="https://github.com/jupyter/notebook/tree/master/docs/source/examples/Notebook" class="alert-link">here</a>
# .
# </div>

# <div class="alert alert-info">
# For more useful information, check out Jupyter Notebooks 
# <a href="https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/" class="alert-link">tips & tricks</a>
# , and more information on how 
# <a href="http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html" class="alert-link">notebooks work</a>.
# </div>

# ### Menu Options & Shortcuts
# 
# To get a quick tour of the Jupyter user-interface, click on the 'Help' menu, then click 'User Interface Tour'.
# 
# There are also a large number of useful keyboard shortcuts. Click on the 'Help' menu, and then 'Keyboard Shortcuts' to see a list. 

# ### Cells

# <div class="alert alert-success">
#     The main organizational structure of the notebook are <b>cells</b>.
# </div>

# Cells are an independent 'unit'. When you click into a cell, you can 'run' it by clicking Shift + Enter, or by pressing the play (Run) button above. 
# 
# Cells come in different types for writing different things - mainly, text or code. 

# #### Markdown Cells
# 
# Cells, can be markdown (text), like this one.

# A brief note about Markdown. It's a way to specify all formatting within the text itself. 
# 
# For example, italicized text can be specified with an _underscore_ or *single asterisks*.
# 
# Bold text requires __two underccores__ or **two asterisks**.

# #### Class Question #2
# 
# **What does three underscores around text accomplish?**
# 
# - A) bold
# - B) italicize
# - C) bold + italicize
# - D) normal text
# - E) I'm lost

# you can write/edit your markdown text here to determine the answer to the question

# ### Markdown Headers
# 
# ## Headers are specified with a pound sign
# 
# ### The more pound signs, the smaller the header
# 
# #### But it's still larger
# 
# than just plain text.
# 

# Lists are also possible:
#     
# - item 1
# - item 2
# - item 3
# 
# 
# 1. numbered item
# 2. item 2
# 3. item 3

# #### Class Question #3
# 
# **What would happen if I specified a numbered list but put the same number before each list item?**
# 
# - A) the list would have the same number before each item
# - B) markdown would still format it with sequential numbers
# - C) markdown wouldn't know it was a list
# - D) normal text with everything on a single line
# - E) I'm lost

# test it out down here to see...
# 
# list item
# list item 
# list item

# #### Code Cells
# 
# Whenever you're writing code, you'll want to be sure the cell is set to be a code cell

# In[6]:


# Cell can also be code.
a = 1
b = 2


# In[7]:


# Cells can also have output, that gets printed out below the cell.
c = a - b
print(c)


# In[8]:


# If you execute a cell with just a variable name in it, it will also get printed
c


# #### Running Cells
# 
# - The numbers in the square brackets to the left of a cell show which cells have been run, and in what order.
#     - An asterisk (*) means that the cell is currently running
#     - You do not need to run cells in order! This is useful for flexibly testing and developing code. 

# ### Coding time
# 
# 
# Write code that outputs the value '6'

# In[11]:


## YOUR CODE HERE
c = 3 * b
c


# #### Class Question #4
# 
# **Which of the following best describes you?**
# 
# - A) I completed the task.
# - B) I tried but wasn't able to complete the task.
# - C) I am not sure where to start.

# ### Accessing Documentation

# <div class="alert alert-success">
# Jupyter has useful shortcuts. Add a single <code>?</code> after a function or class get a window with the documentation, or a double <code>??</code> to pull up the source code. 
# </div>

# In[12]:


# For example, execute this cell to see the documentation for the 'abs'
get_ipython().run_line_magic('pinfo', 'abs')


# ### Autocomplete

# <div class="alert alert-success">
# Jupyter also has 
# <a href="https://en.wikipedia.org/wiki/Command-line_completion" class="alert-link">tab complete</a>
# capacities, which can autocomplete what you are typing, and/or be used to explore what code is available. (<i>Note</i>: Some of this functionality is limited on datahub.)
# </div>

# In[ ]:


# Move your cursor to the end of the line, press tab, and a drop menu will appear showing all possible completions
ra 


# In[ ]:


# If there is only one option, tab-complete will auto-complete what you are typing
ran


# ### Installation
# 
# You only need access to datahub for this course, but for working on your projects and for downloading and opening the notebooks used in class, you may want to download anaconda onto your computer, which comes complete with conda, and Jupyter notebooks.

# <center><img src="img/anaconda.png" width="450px"></center>

# <div class="alert alert-success">
# Anaconda is an open-source distribution of Python, focused on scientific computing in Python. 
# </div>
# 
# <div class="alert alert-info">
# The anaconda website is 
# <a href="https://www.anaconda.com" class="alert-link">here</a>. 
# </div>

# ## The Anaconda Ecosystem
# 
# - Anaconda itself is a distribution - that is, a copy of the Python standard library, included a curated collection of external packages.
# - Conda is a package manager, allowing you to download, install, and manage other packages. 

# <div class="alert alert-info">
# Download anaconda from
# <a href="https://www.anaconda.com/download/" class="alert-link">here</a>.
# </div>

# ### Notes
# 
# - If you are on Mac, you have a native installation of Python. This native installation of Python may be older, will not include the extra packages that you will need for this class, and is best left untouched. 
#     - Downloading anaconda will install a separate, independent install of Python, leaving your native install untouched. 
# - Windows does not require Python natively and so it is not typically pre-installed. 

# In[ ]:


# You can check which python you are using, and what version it is.
#  Once you have installed anaconda, you should see you are using Python in your anaconda folder
#  Make sure that the version you have is 3.6 (or at least 3.X)
#  Note: these are command-line functions that may not work on windows
get_ipython().system('which python')
get_ipython().system('python --version')


# ### Web Browser

# <div class="alert alert-success">
# Jupyter notebooks display in a web browser. They are not hosted on the web, everything is happening locally. 
# </div>

# If you click on the url in the browser, you will notice it says 'localhost'. This means it is connected to something locally, on your computer. 
# 
# That local connection is to the 'kernel'. 

# ## Academic Integrity
# 
# We've had some issues in the past, so we're trying to be incredibly explicit this quarter so that we're all on the same page. (And, because this differs from some other courses.)

# <center><img src="img/academic_integrity.png" width="900px"></center>
# 
# Correction: It was for one exam; it was not constant. And it was 6/100 (which is 6% of the class!)

# *I came into this class knowing absolutely nothing about coding. Being in this position, I have made it my goal to go above and beyond in learning about programming languages that I am unfamiliar with because I personally like a challenge and I love learning new things.*
# 
# *Because coding does not come naturally to me, I plan WAY ahead of time as to when I need to sit down, uninterrupted, to really learn, make mistakes, and test out the code I write in assignments. For example, I plan DAYS ahead of time as to when I need to sit down and complete assignments. Again, because coding does not come naturally to me, I spend on average 2 hours more than the median hours/time spent listed. Not only do I spend hours completing assignments to the best of my ability, but I make sure to test out EACH AND EVERY PIECE of code I wrote in these assignments to make sure my code is “spitting out” what I am expecting, and to show you and the TAs what I was trying to do just in case I get something wrong (because showing work for some points is better than showing no work for 0 points, you know?)* 
# 
# *Each student has their method, and planning out WHEN to work and HOW LONG to work on assignments is my method; I just think it is a shame that students resort to cheating when things get tough or they are too lazy to actually learn, because again, that is unfair to me as a student who dedicates time and energy to every assignment in this class.* 
# 
# \- Former COGS 18 Student

# The most important reminder: **you must have written, understand, and be able to explain any code you turn in as your own.**

# When *can* you work with others in COGS 18?
# - Coding Labs
# - Assignments

# Working with others is *different* than copying from others. It is *never* acceptable to just ask someone for their answers or their code. 
# 
# On Coding Labs & Assignments, it *is* OK to ask one another questions *about* what you're working on. It is OK to share screens and talk through your answers.
# 
# If you find yourself copying + pasting someone else's code (from a friend or from the Internet)...you're probably making a mistake.

# When can you NOT work with others?
# - Exams
# 
# Exams are the only time in this course we ask you to work on material completely on your own. 

# Exams assess *your* understanding after you've had plenty of practice (in lecture, on coding labs, and on assignments).
# 
# It's your time to show off what you know.

# Exams are open notes and open Google. 
# 
# You *can* search the Internet for help on concepts.
# 
# You are not allowed to ask anyone specific questions from the Exam or post the questions anywhere.

# Part of your first Coding Lab will help to make this all as clear as possible!
