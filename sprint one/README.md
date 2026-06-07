# Overview

For this project, I wanted to improve my understanding of the R programming language by creating a useful data analysis program. The software I wrote is a housing regression program that can load housing data from either an Excel file or a CSV file and allow the user to run an OLS regression model.

The program demonstrates several important R programming concepts, including variables, lists, vectors, logical values, numeric values, data frames, loops, functions, and conditional statements. It also uses R libraries to read data files and run regression diagnostics.

My purpose for writing this software was to learn how R can be used for statistical analysis and data science.

(https://youtu.be/fkuF9PJj9kY)

# Development Environment

I developed this software using Visual Studio Code. I used Git and GitHub to manage the project files and upload the finished program to a repository.

The programming language used for this project was R. The program uses several R libraries, including:

- `readxl` for reading Excel files
- `car` for regression diagnostic tools such as VIF
- `lmtest` for statistical tests
- `tseries` for additional diagnostic testing

The program was written to work with both `.xlsx` and `.csv` files so that the user can use either Excel data or standard CSV data.

# Useful Websites

- [R Documentation](https://www.r-project.org/)
- [readxl Package Documentation](https://readxl.tidyverse.org/)
- [car Package Documentation](https://cran.r-project.org/web/packages/car/index.html)
- [lmtest Package Documentation](https://cran.r-project.org/web/packages/lmtest/index.html)
- [W3Schools R Tutorial](https://www.w3schools.com/r/)

# Future Work

- Add better error handling if the user enters a variable name that does not exist in the dataset.
- Add more regression diagnostic tests and clearer explanations of what each test means.
- Create graphs or charts to help visualize the regression results and model diagnostics.
- Make the program easier to use by adding a menu system with numbered options.
- Add the ability to automatically compare multiple regression models and recommend the best one.
