import test106 as test

### PROBLEM 1.
# We have provided test cases for the first function, as an example. 
# Write at least two test cases each for the next three functions

def letter_freqs(word_list):
    letter_freq_dict = {}
    for w in word_list:
        for l in w:
            if l not in letter_freq_dict:
                letter_freq_dict[l] = 1
            else:
                letter_freq_dict[l] = letter_freq_dict[l] + 1
    return letter_freq_dict

test.testEqual(type(letter_freqs(["hello", "goodbye"])), type({}))
test.testEqual(letter_freqs(["good", "bad", "indifferent"]), {'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1})
test.testEqual(letter_freqs(["good"]), {'g':1, 'o':2, 'd':1})
test.testEqual(letter_freqs([]), {})
    
def key_with_biggest_value(diction):    
    most_freq_letter = diction.keys()[0]
    for item in diction.keys():
        if diction[item] > diction[most_freq_letter]:
            most_freq_letter = item
    return most_freq_letter

test.testEqual(key_with_biggest_value({'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1}), 'd') 
test.testEqual(key_with_biggest_value({'a': 1}), 'a') 
test.testEqual(key_with_biggest_value({'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 3, 'i': 2, 'o': 2, 'n': 3, 'r': 1, 't': 1}), 'd')
    
def most_frequest_letter(word_list):
    return key_with_biggest_value(letter_freqs(word_list))

test.testEqual(most_frequest_letter('hello world'), 'l') 
test.testEqual(most_frequest_letter('hey'), 'y') 
test.testEqual(most_frequest_letter('test cases'), 's')

def popular_keys(diction):
    pop_keys = []
    for k in diction:
        if diction[k] > 3:
            pop_keys.append(k)
    return pop_keys

test.testEqual(popular_keys({'a': 1, 'b': 1, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1}), []) 
test.testEqual(popular_keys({'a': 4, 'b': 5, 'e': 10, 'd': 3, 'g': 1, 'f': 2, 'i': 2, 'o': 2, 'n': 2, 'r': 1, 't': 1}), ['a', 'b', 'e'])

### PROBLEM 2. 
#Define test cases for the Car class below that will make you confident that all three of the methods 
# are operating correctly. 
#For each of your tests, include a comment stating whether it's a return-value test or a side-effect test. 

# (Note: we never showed any examples in class of explicitly calling the __str__ method, but you can. 
    # If x is an instance of the class Car, x.__str__() can be invoked just as x.move_forward() can. 
    # Indeed, __init__ can also be invoked this way, too, but in practice you would not want do it; 
    # __init__ gets called automatically when a new instance is created, and that's normally the only 
    # time it gets called.)
    
class Car:
    def __init__(self,color,wheels=4,size="compact",make=None):
        self.color = color
        self.wheels = wheels
        self.size = size
        self.make = make
        self.wheels_with_uhaul = wheels + 4
        self.dist_from_origin = 0.0

    def __str__(self):
        s = "A %s car:\n" % (self.color)
        if self.make:
            s = s + "Make: %s\n" % (str(self.make))
        s = s + "Has %d wheels\n" % (self.wheels)
        s = s + "Current distance from origin: %.02f miles" % (self.dist_from_origin)
        return s

    def move_forward(self,miles=1):
        self.dist_from_origin = self.dist_from_origin + miles
        return "Moved forward %.02f miles" % (miles)

## Testing init method (side-effect test)
car = Car('red') 
test.testEqual(car.color, 'red') 
test.testEqual(car.wheels, 4) 
test.testEqual(car.size, 'compact') 
test.testEqual(car.make, None) 
test.testEqual(car.wheels_with_uhaul, 8) 
test.testEqual(car.dist_from_origin, 0.0) 

new_car = Car('red', wheels = 2, size = "SUV", make = 'Ford') 
test.testEqual(new_car.color, 'red') 
test.testEqual(new_car.wheels, 2) 
test.testEqual(new_car.size, 'SUV')
test.testEqual(new_car.make, 'Ford') 
test.testEqual(new_car.wheels_with_uhaul, 6) 
test.testEqual(new_car.dist_from_origin, 0.0) 

## Testing str method. (return value test) 
car3 = Car('red') 
car4 = Car('blue', make = 'Ford') 
car4.move_forward(miles = 5) 
test.testEqual(car3.__str__(), "A red car:\n" + "Has 4 wheels\n" + "Current distance from origin: 0.00 miles") 
test.testEqual(car4.__str__(), "A blue car:\n" + "Make: Ford\n" + "Has 4 wheels\n" + "Current distance from origin: 5.00 miles") 

## Testing move_forward (side effect test) 
car1 = Car('red') 
car1.move_forward() 
test.testEqual(car1.dist_from_origin, 1.0) 
car2 = Car('blue') 
car2.move_forward(5) 
test.testEqual(car2.dist_from_origin, 5.0)