def advanced_pipeline(data):

    result = []
    total_salary = 0
    high_count = 0

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
            new["category"] = "High"
            high_count += 1
        else:
            new["category"] = "Low"

        result.append(new)
        total_salary += salary

    return {
        "data": result,
        "total_salary": total_salary,
        "high_count": high_count
    }
