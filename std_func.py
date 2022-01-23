  
def get_n(dataset):
    return len(dataset)

def mean(dataset):
    return sum(dataset)/get_n(dataset)

def var(dataset):
    count = sum([value - x_mean(dataset) for value in dataset])

def XY(dataset_x, dataset_y):
    return sum([tupla[0] * tupla[1] for tupla in zip(dataset_x, dataset_y)])

def cov(dataset_x, dataset_y):
    return (XY(dataset_x, dataset_y) / get_n(dataset_x)) - (mean(dataset-x) * mean(dataset_y)) 

def rxy(dataset_x, dataset_y):
    return cov(dataset_x, dataset_y) / ( (var(dataset_x) ** 0.5)* (var(dataset_y) ** 0.5 ) )

def B(dataset_x, dataset_y):
    return rxy(dataset_x, dataset_y) / ((var(dataset_y)**0.5)/(var(dataset_x)**0.5))

def B0(dataset_x,dataset_y):
    return mean(dataset_y) - (B(dataset_x, dataset_y) * mean(dataset_x))