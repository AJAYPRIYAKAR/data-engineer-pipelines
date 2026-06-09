from sample_data import data


def validate(emp):
    name = emp.get("name")
    salary = emp.get("salary")

    if not name or salary is None:
        return False

    try:
        salary = int(salary)
    except:
        return False

    return salary > 0


def pipeline(data):
    result = []
    total = 0

    for emp in data:
        if not emp:
