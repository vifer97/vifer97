def myFunc(e):
#funkciju definīcija 
    return e['year'] 
cars = [ 
{'car':'Volvo', 'year': 2015}, 
{'car': 'Toyota', 'year': 2020}, 
{'car': 'BMW', 'year': 2019}, 
{'car': 'VW', 'year': 2021},
{'car': 'Hyundai', 'year': 2021} 
] 
#vārdnīca
cars.sort(key=myFunc)
#vārdnīca tiek sakārtota pēc atslēgas
print(cars)
#kods drukā rezultātu