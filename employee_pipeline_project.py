from sample_data import data


def employee_pipeline(data):

    result = []
    total_salary = 0
    count = 0
    high_salary_count = 0

    for emp in data:

        name = emp.get("name")
        salary = emp.get("salary")

        # validation
        if not name or salary is None:
            continue

        try:
            salary = int(salary)
        except:
            continue

        if salary <= 0:
            continue

        new = emp.copy()
        new["salary"] = salary

        # transformation
        if salary > 60000:
            new["level"] = "High"
            high_salary_count += 1
        else:
            new["level"] = "Normal"

        result.append(new)
        total_salary += salary
        count += 1

    return {
        "processed_data": result,
        "metrics": {
            "total_employees": count,
            "total_salary": total_salary,
            "high_salary_count": high_salary_count
        }
    }


if __name__ == "__main__":
    output = employee_pipeline(data)
    print(output)
``
