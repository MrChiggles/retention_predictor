import numpy as np
import pandas as pd

def get_data():
    dataSrc = pd.read_csv('retention_data.csv')

    data = dataSrc.as_matrix()

    departmentData = data[:, 7]
    salaryData = data[:, 8]

    department_types = []
    salary_types = []

    sample_size = len(departmentData)

    # get all label types
    for i in range(sample_size):

        if departmentData[i] not in department_types:
            department_types.append(departmentData[i])

        if salaryData[i] not in salary_types:
            salary_types.append(salaryData[i])

    print("department_types", department_types)
    print("salary_types", salary_types)

    print("# departments", len(department_types))
    print("# salary types", len(salary_types))
    print()

    data[:, 0] = normalizeData(data[:, 0])
    data[:, 1] = normalizeData(data[:, 1])
    data[:, 2] = normalizeData(data[:, 2])
    data[:, 3] = normalizeData(data[:, 3])
    data[:, 4] = normalizeData(data[:, 4])

    Xdata = data[:, :-1]
    Y = data[:, -1]

    d, l = Xdata.shape

    l += len(salary_types)
    l += len(department_types)

    X = np.zeros((d, l), dtype=np.float32)

    # for i in range(len(salary_types)):
    #     if data[i, 5]


def normalizeData(args):
    return (args - args.mean()) / args.std()

get_data()