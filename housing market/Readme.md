


As a retail investor, I wanted to practice using Python to analyze data from a real spreadsheet. This project helped me learn how to load data, clean it, sort it, filter it, group it, and save new results.

The data set I analyzed is a rental housing data set from an Excel file called rental.xls. The data includes cities, years, population, college enrollment, rent, housing information, average income, and percent of students. I used the main RENTAL sheet from the Excel file.

Data Source: Rental Data Set

The purpose of this software is to answer questions about rent, income, and how rent changed over time. The program looks at rental costs in different cities and compares them with average income.

Demo Video: https://youtu.be/bSrAtWa2DeQ

Data Analysis Results

Question 1: In 1990, which cities had the highest rent compared to income?

Answer: The program found the top cities where annual rent was the highest percentage of average income. It filtered the data to 1990, calculated annual rent, calculated rent as a percent of income, and sorted the results from highest to lowest.

Question 2: From 1980 to 1990, which cities had the largest rent increase?

Answer: The program compared rent from 1980 and 1990 for each city. It found the cities with the largest monthly rent increases and sorted them from highest to lowest.

The program also grouped the data by year to show the average rent, average income, and average percent of students for each year.

Development Environment

I used Visual Studio Code to write and run the program. I also used the VS Code terminal to test the program and view the output.

The program was written in Python. I used the pandas library to read the Excel file, clean the data, filter rows, sort values, group data, and save the results to a CSV file. I also used the pathlib library to work with file paths.

Useful Websites
Pandas Documentation
Python Documentation
Markdown Guide
Pandas read_excel
Future Work
Add charts to make the results easier to understand.
Let the user choose which year to analyze.
Add more questions using population and enrollment data.
Improve the CSV output file.
Add better error messages if the Excel file is missing.

The program does not handle errors very well and has a lot of bugs because it is the first file I have written with pandas. The file could be improved in many ways such as prompting the user for questions or updates to the question. 