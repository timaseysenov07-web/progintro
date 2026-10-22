data =[2, 4, 4, 4, 5, 5, 7, 9]
def summary(data):
    prumer = sum(data) / len(data)
    median = data[len(data) // 2]
    std_dev = (sum((x - prumer)**2 for x in data) / len(data))**0.5
    min_data = min(data)
    max_data = max(data)
    return {
        "mean": prumer,
        "median": median,
        "standard_deviation": std_dev,
        "min": min_data,
        "max": max_data
    }
print (summary(data))