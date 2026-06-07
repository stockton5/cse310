

from pathlib import Path
import pandas as pd

DATA_FILE = "rental.xls"
OUTPUT_FILE = "rental_results.csv"
TOP_AMOUNT = 10


COLUMNS = [
    "City", "Year", "Population", "Enrollment", "Rent",
    "Rental_Housing", "Total_Housing", "Average_Income",
    "Log_Enrollment", "Log_Population", "Log_Rent",
    "Log_Total_Housing", "Log_Rental_Housing", "Log_Average_Income",
    "Change_Log_Enrollment", "Change_Log_Population", "Change_Log_Rent",
    "Change_Log_Total_Housing", "Change_Log_Rental_Housing",
    "Change_Log_Average_Income", "Percent_Students",
    "Change_Percent_Students", "Is_1990",
]


def print_section(title):
    print("\n" + title)
    print("=" * len(title))


def load_data():
    file_path = Path(DATA_FILE)
    if not file_path.exists():
        raise FileNotFoundError("Put rental.xls in the same folder as this program.")
    try:
        data = pd.read_excel(file_path, sheet_name="RENTAL")
    except ImportError:
        print("This .xls file needs xlrd. Run: pip install xlrd")
        raise
    data.columns = COLUMNS
    return data


def clean_data(data):
    keep = [
        "City", "Year", "Population", "Enrollment", "Rent",
        "Average_Income", "Percent_Students",
    ]
    clean = data[keep].copy()
    for column in keep:
        clean[column] = pd.to_numeric(clean[column], errors="coerce")
    clean = clean.dropna()
    clean["City"] = clean["City"].astype(int)
    clean["Year"] = clean["Year"].astype(int)
    clean["Annual_Rent"] = clean["Rent"] * 12
    clean["Rent_Income_Percent"] = clean["Annual_Rent"] / clean["Average_Income"] * 100
    return clean


def show_summary(data):
    print_section("Dataset Summary")
    print(f"Rows: {len(data)}")
    print(f"Cities: {data['City'].nunique()}")
    print(f"Years: {sorted(data['Year'].unique())}")
    print(f"Average monthly rent: ${data['Rent'].mean():,.2f}")
    print(f"Average yearly income: ${data['Average_Income'].mean():,.2f}")


def question_one(data):
    print_section("Question 1")
    print("In 1990, which cities had the highest rent compared to income?")
    year_1990 = data[data["Year"] == 90]
    answer = year_1990.sort_values("Rent_Income_Percent", ascending=False)
    answer = answer.head(TOP_AMOUNT)
    answer = answer[["City", "Rent", "Annual_Rent", "Average_Income", "Rent_Income_Percent"]]
    print(answer.to_string(index=False))
    top = answer.iloc[0]
    print(f"\nAnswer: City {int(top['City'])} had the highest rent burden.")
    print(f"Annual rent was {top['Rent_Income_Percent']:.2f}% of average income.")
    return answer


def question_two(data):
    print_section("Question 2")
    print("From 1980 to 1990, which cities had the largest rent increase?")
    two_years = data[data["Year"].isin([80, 90])]
    rent_table = two_years.pivot(index="City", columns="Year", values="Rent")
    student_table = two_years.pivot(index="City", columns="Year", values="Percent_Students")
    answer = pd.DataFrame()
    answer["Rent_1980"] = rent_table[80]
    answer["Rent_1990"] = rent_table[90]
    answer["Rent_Increase"] = answer["Rent_1990"] - answer["Rent_1980"]
    answer["Rent_Increase_Percent"] = answer["Rent_Increase"] / answer["Rent_1980"] * 100
    answer["Student_Percent_Change"] = student_table[90] - student_table[80]
    answer = answer.reset_index().sort_values("Rent_Increase", ascending=False)
    answer = answer.head(TOP_AMOUNT)
    print(answer.to_string(index=False))
    top = answer.iloc[0]
    print(f"\nAnswer: City {int(top['City'])} had the largest rent increase.")
    print(f"Rent increased by ${top['Rent_Increase']:,.0f} per month.")
    return answer


def grouped_analysis(data):
    print_section("Grouped Analysis by Year")
    grouped = data.groupby("Year").agg({
        "Rent": "mean",
        "Average_Income": "mean",
        "Percent_Students": "mean",
    })
    print(grouped.to_string())


def save_results(answer_1, answer_2):
    answer_1 = answer_1.copy()
    answer_2 = answer_2.copy()
    answer_1.insert(0, "Question", "Highest rent compared to income")
    answer_2.insert(0, "Question", "Largest rent increase")
    combined = pd.concat([answer_1, answer_2], ignore_index=True, sort=False)
    combined.to_csv(OUTPUT_FILE, index=False)
    print_section("Saved Results")
    print(f"Results saved to {OUTPUT_FILE}")


def main():
    raw = load_data()
    clean = clean_data(raw)
    show_summary(clean)
    answer_1 = question_one(clean)
    answer_2 = question_two(clean)
    grouped_analysis(clean)
    save_results(answer_1, answer_2)


if __name__ == "__main__":
    main()
