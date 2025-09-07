import pandas as pan

dataset = {
    'cars' : ['Tesla', 'Rivian', 'Lucid'],
    'passings' : [9,4,1]
}

my_dataset = pan.DataFrame(dataset)
print(my_dataset)