
-- EXERCISE XP --

-- Table for companies
CREATE TABLE companies (
    company_name TEXT,
    company_city TEXT,
    company_state TEXT,
    company_type TEXT,
    const_site_category TEXT
);

-- Table for employees
CREATE TABLE employees (
    comp_code_emp TEXT,
    employee_code_emp INTEGER,
    employee_name_emp TEXT,
    "GEN(M_F)" TEXT, 
    age INTEGER
);

-- Table for functions
CREATE TABLE functions (
    function_code INTEGER,
    "function" TEXT, 
    function_group TEXT
);

-- Table for salaries
CREATE TABLE salaries (
    comp_code TEXT,
    comp_name TEXT,
    employee_id INTEGER,
    employee_name TEXT,
    "date" TEXT,
    func_code INTEGER,
    func TEXT,
    salary TEXT 
);

SELECT 
    (SELECT COUNT(*) FROM employees) as emp_count,
    (SELECT COUNT(*) FROM functions) as func_count,
    (SELECT COUNT(*) FROM salaries) as sal_count;


-- EXERCISE 1: Building a Comprehensive Dataset for Employee Analysis

-- Create the final cleaned table 'df_employee'

CREATE TABLE df_employee AS
SELECT
    -- Create unique identifier 
    CAST(s.employee_id AS TEXT) || '_' || TO_CHAR(TO_DATE(s."date", 'DD/MM/YYYY'), 'YYYY-MM-DD') AS id,
    
    -- Convert 'date' from TEXT to actual DATE type
    TO_DATE(s."date", 'DD/MM/YYYY') AS month_year,
    
    s.employee_id,
    s.employee_name,
    e."GEN(M_F)" AS gender,
    e.age,
    
    -- Clean Salary: Replace ',' with '.' and convert to NUMERIC
    CAST(REPLACE(s.salary, ',', '.') AS NUMERIC) AS salary,
    
    f.function_group,
    c.company_name,
    
    -- Cleaning: 
    CASE WHEN c.company_city = 'Goianiaa' THEN 'Goiania' ELSE c.company_city END AS company_city,
    CASE WHEN c.company_state = 'GOIAS' THEN 'Goias' ELSE c.company_state END AS company_state,
    CASE WHEN c.company_type = 'Construction Sites' OR c.company_type = 'Construction Site s' 
         THEN 'Construction Site' ELSE c.company_type END AS company_type,
    CASE WHEN c.const_site_category = 'Commerciall' THEN 'Commercial' ELSE c.const_site_category END AS const_site_category

FROM salaries s
LEFT JOIN companies c ON s.comp_name = c.company_name
LEFT JOIN functions f ON s.func_code = f.function_code
LEFT JOIN employees e ON s.employee_id = e.employee_code_emp;


-- EXERCISE 2: Cleaning Data for Consistency and Quality

-- 1
SELECT * FROM df_employee LIMIT 10;

-- 2. Removing unwanted hidden spaces from all text columns:
UPDATE df_employee
SET id = TRIM(id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);

-- Standardize Gender 
UPDATE df_employee
SET gender = CASE 
                WHEN gender = 'M' THEN 'Male'
                WHEN gender = 'F' THEN 'Female'
                ELSE gender 
             END;

-- Check:
SELECT DISTINCT gender FROM df_employee;

-- 3. Check for NULL values and empty values:

SELECT *
FROM df_employee
WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR gender IS NULL
   OR age IS NULL
   OR salary IS NULL
   OR function_group IS NULL
   OR company_name IS NULL
   OR company_city IS NULL
   OR company_state IS NULL
   OR company_type IS NULL
   OR const_site_category IS NULL;

-- Check for 'Empty' values 

SELECT *
FROM df_employee
WHERE id = ''
   OR employee_name = ''
   OR gender = ''
   OR function_group = ''
   OR company_name = ''
   OR company_city = ''
   OR company_state = ''
   OR company_type = ''
   OR const_site_category = ''
   OR salary::text = '' 
   OR age::text = '';

-- 4. Delete rows of the detected missing values:

-- Delete rows where salary is just a space:
DELETE FROM df_employee
WHERE salary::text = ' ';

-- Delete rows where const_site_category is just a space:
DELETE FROM df_employee
WHERE const_site_category = ' ';

-- Verify row count:
SELECT COUNT(*) FROM df_employee;

-- EXERCISE 3: Calculating Current Employee Counts by Company

-- How many employees do the companies have today?

SELECT COUNT(DISTINCT employee_id) AS total_employees_today
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee); -- 676

-- Group them by company:

SELECT company_name, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name
ORDER BY employee_count DESC;

-- EXERCISE 4: Analyzing Employee Distribution by City and Over time:

-- What is the total number of employees each city? Add a percentage column:

SELECT 
    company_city, 
    COUNT(employee_id) AS employee_count,
    --Percentage of the total:
    ROUND(COUNT(employee_id) * 100.0 / SUM(COUNT(employee_id)) OVER (), 2) AS percentage
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_city
ORDER BY employee_count DESC;

-- What is the total number of employees each month?

SELECT 
    month_year, 
    COUNT(DISTINCT employee_id) AS total_employees
FROM df_employee
GROUP BY month_year
ORDER BY month_year ASC;

-- What is the average number of employees each month?

WITH MonthlyCounts AS (
    SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)
SELECT ROUND(AVG(employee_count), 0) AS avg_employees_per_month
FROM MonthlyCounts;

-- EXERCISE 5: Analyzing Employment Trends and Salary Metrics

-- What is the minimum and maximum number of employees throughout all the months? In which months were they?

WITH monthly_counts AS (
    SELECT month_year, COUNT(DISTINCT employee_id) AS total_employees
    FROM df_employee
    GROUP BY month_year
)
SELECT month_year, total_employees, 
       CASE 
           WHEN total_employees = (SELECT MIN(total_employees) FROM monthly_counts) THEN 'Minimum'
           WHEN total_employees = (SELECT MAX(total_employees) FROM monthly_counts) THEN 'Maximum'
       END AS record_type
FROM monthly_counts
WHERE total_employees = (SELECT MIN(total_employees) FROM monthly_counts)
   OR total_employees = (SELECT MAX(total_employees) FROM monthly_counts)
ORDER BY total_employees;

-- What is the monthly average number of employees by function group?

WITH function_monthly_counts AS (
    SELECT function_group, month_year, COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY function_group, month_year
)
SELECT function_group, ROUND(AVG(employee_count), 2) AS avg_monthly_employees
FROM function_monthly_counts
GROUP BY function_group
ORDER BY avg_monthly_employees DESC;

-- What is the annual average salary?

SELECT 
    EXTRACT(YEAR FROM month_year) AS year, 
    ROUND(AVG(salary), 2) AS average_salary
FROM df_employee
GROUP BY year
ORDER BY year;
