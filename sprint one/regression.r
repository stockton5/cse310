# Housing OLS Regression Program
# Works with .csv or .xlsx files
# PROGRAMMMM
#1.  Packages

#create list
packages <- list("readxl", "car", "lmtest", "tseries")

#load packages
for (pkg in packages) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg)
    library(pkg, character.only = TRUE)
  }
}


# 2. Basic Program Info


program_name <- "Housing Regression Program"     # character
version <- 1.0                                   # numeric
test_count <- 5                                  # integer/numeric
run_tests <- TRUE                                # logical
test_names <- c("Summary", "VIF", "Breusch-Pagan", "Jarque-Bera", "Durbin-Watson") # vector

program_info <- list(
  name = program_name,
  version = version,
  tests = test_names
)

cat("\nWelcome to the", program_info$name, "\n")
cat("Version:", program_info$version, "\n\n")

cat("Diagnostic tests included:\n")
for (test in program_info$tests) {
  cat("-", test, "\n")
}


# 3. Load Data


file_path <- readline("\nEnter file name, such as housing_data.xlsx or housing_data.csv: ")

if (grepl(".xlsx$", file_path)) {
  housing_df <- as.data.frame(read_excel(file_path))
} else if (grepl(".csv$", file_path)) {
  housing_df <- read.csv(file_path)
} else {
  stop("File must be .xlsx or .csv")
}

housing_df <- na.omit(housing_df)

cat("\nData loaded successfully.\n")
cat("Rows:", nrow(housing_df), "\n")
cat("Columns:", ncol(housing_df), "\n\n")

cat("Column names:\n")
print(names(housing_df))


# 4. Choose Regression Variables


dependent <- readline("\nEnter dependent variable, for example Sale_Price: ")

independent_input <- readline("Enter independent variables separated by commas, or press Enter for all others: ")

if (independent_input == "") {
  independents <- names(housing_df)[names(housing_df) != dependent]
} else {
  independents <- trimws(strsplit(independent_input, ",")[[1]])
}

formula_text <- paste(dependent, "~", paste(independents, collapse = " + "))
reg_formula <- as.formula(formula_text)

cat("\nRegression formula:\n")
print(reg_formula)

# 5. Run OLS Regression


model <- lm(reg_formula, data = housing_df)

cat("\nOLS Regression Results:\n")
print(summary(model))


# 6. Five Diagnostic Tests


cat("\nDiagnostic Test 1: Model Summary\n")
model_summary <- summary(model)
cat("R-squared:", model_summary$r.squared, "\n")
cat("Adjusted R-squared:", model_summary$adj.r.squared, "\n")

cat("\nDiagnostic Test 2: VIF Multicollinearity Test\n")
tryCatch(
  print(vif(model)),
  error = function(e) cat("VIF could not be calculated for this model.\n")
)

cat("\nDiagnostic Test 3: Breusch-Pagan Heteroskedasticity Test\n")
print(bptest(model))

cat("\nDiagnostic Test 4: Jarque-Bera Normality Test\n")
print(jarque.bera.test(residuals(model)))

cat("\nDiagnostic Test 5: Durbin-Watson Autocorrelation Test\n")
print(dwtest(model))

# 7. Loop Through Variables


cat("\nTesting each independent variable by itself:\n")

results <- data.frame(
  Variable = character(),
  Adjusted_R2 = numeric(),
  stringsAsFactors = FALSE
)

for (var in independents) {
  single_formula <- as.formula(paste(dependent, "~", var))
  single_model <- lm(single_formula, data = housing_df)
  adj_r2 <- summary(single_model)$adj.r.squared
  
  results <- rbind(
    results,
    data.frame(Variable = var, Adjusted_R2 = adj_r2)
  )
}

results <- results[order(-results$Adjusted_R2), ]

cat("\nBest variables ranked by Adjusted R-squared:\n")
print(results)

cat("\nProgram complete.\n")