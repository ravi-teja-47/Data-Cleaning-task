# 🧹 Task 1: Data Cleaning and Preprocessing

### 📊 Internship Task - Data Analyst Role

## 📁 Dataset Used

**Mall Customer Segmentation Data**  
Source: [Kaggle Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

This dataset contains information about customers of a mall, including:

- Customer ID
- Gender
- Age
- Annual Income (in thousands of dollars)
- Spending Score (1–100)

---

## 🧼 Objective

To clean and preprocess the dataset for further analysis or modeling.  
Focus was on removing inconsistencies, handling missing/duplicate data, and formatting.

---

## 🔧 Tools Used

- **Language:** vs code
- **Libraries:** pandas
- **Environment:** Local machine

---

## ✅ Cleaning Steps Performed

1. **Loaded the dataset** using `pandas.read_csv()`.
2. **Renamed columns** to lowercase and underscore format for consistency.
3. **Converted all values** in the 'gender' column to lowercase to ensure consistency (e.g., 'Male' → 'male').
4. **Removed duplicates** from the dataset
5. **Converted the 'age' column** to integer type to ensure correct data type for numerical analysis.
6. **Saved the cleaned DataFrame** to a new CSV file without including the index column.
