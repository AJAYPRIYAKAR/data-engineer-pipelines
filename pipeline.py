from sample_data import data

def pipeline(data):
    result = []
    total = 0

    for emp in data:
        name = emp.get("name")
        salary = emp.get("salary")

        if not name or salary is None:
            continue

        try:
            salary = int(salary)
        except:
            continue

        if salary <= 0:
            continue

        new = emp.copy()

        if salary > 60000:
            new["grade"] = "A"
        else:
            new["grade"] = "B"

        result.append(new)
        total += salary

    return {"data": result, "total": total}

if __name__ == "__main__":
    output = pipeline(data)
    print(output)

