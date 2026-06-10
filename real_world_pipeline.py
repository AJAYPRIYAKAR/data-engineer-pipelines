from sample_data import data


def validate(emp):
    name = emp.get("name")
    salary = emp.get("salary")
    exp = emp.get("exp")
    dept = emp.get("dept")

    if not name or salary is None or exp is None or not dept:
        return False

    try:
        salary = int(salary)
        exp = int(exp)
    except:
        return False

    return salary > 0 and exp >= 0


def transform(emp):
    salary = int(emp["salary"])
    exp = int(emp["exp"])

    new = emp.copy()
    new["salary"] = salary

    if salary > 70000:
        new["level"] = "A"
    elif salary > 50000:
        new["level"] = "B"
    else:
        new["level"] = "C"

    if new["level"] == "A":
        new["bonus"] = 10000
    elif new["level"] == "B":
        new["bonus"] = 5000
    else:
        new["bonus"] = 2000

    if exp >= 5:
        new["exp_level"] = "Senior"
    elif exp >= 3:
        new["exp_level"] = "Mid"
    else:
        new["exp_level"] = "Junior"

    return new


def pipeline(data):
    result = []

    metrics = {
        "count": 0,
        "total_salary": 0,
        "total_bonus": 0,
        "A_count": 0
    }

    for emp in data:
        if not emp:
            continue

        if not validate(emp):
            continue

        new = transform(emp)
        result.append(new)

        metrics["count"] += 1
        metrics["total_salary"] += new["salary"]
        metrics["total_bonus"] += new["bonus"]

        if new["level"] == "A":
            metrics["A_count"] += 1

    return {
        "data": result,
        "metrics": metrics
    }


if __name__ == "__main__":
    output = pipeline(data)
    print(output)
