# Data Engineer Pipeline Project

## Overview
This project is a simple data pipeline built using Python to process employee data.  
It handles missing values, incorrect types, and invalid records.

---

## What this project does
- Validates input data  
- Removes invalid records  
- Converts values safely  
- Applies simple business logic  
- Calculates total salary  

---

## How the pipeline works
1. Read input  
2. Validate data  
3. Convert salary  
4. Skip invalid records  
5. Add grade  
6. Calculate total  

---

## Example Input

```python
data = [
    {"name": "Ajay", "salary": "50000"},
    {"name": None, "salary": 20000}
]
```

---

## Example Output

```python
{
  "data": [
    {"name": "Ajay", "salary": 50000, "grade": "B"}
  ],
  "total": 50000
}
```

---

## Why I built this
This is part of my learning in data engineering.  
The focus is to build strong pipeline logic before using tools.

---

## Next steps
- Improve performance  
- Use Pandas  
- Add SQL  

---

## Notes
Code is simple and easy to understand.
