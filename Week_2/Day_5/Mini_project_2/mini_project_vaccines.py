# ========================
# Mini Project: Vaccines
# ========================
#Your goal is to create a program to help a city with the vaccination of its citizens.
#

class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
    
    def add_family_member(self, person):
        self.family += [person]
        person.family += [self]


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person: Human):
        if person.age > 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans = self.humans + [person]

    def find_in_queue(self, person):
        for index in range(len(self.humans)):
            if self.humans[index].id_number == person.id_number:
                return index

    def swap(self, person1, person2):
        index_1 = self.find_in_queue(person1)
        index_2 = self.find_in_queue(person2)
        if index_1 is not None and index_2 is not None:
            self.humans[index_1], self.humans[index_2] = self.humans[index_2], self.humans[index_1]

    def get_next(self):
        if not self.humans:
            return None
        next_person = self.humans[0]
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type):
        if not self.humans:
            return None
        
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return person
        return None

    def sort_by_age(self):
        n = len(self.humans)
        for i in range(n):
            for j in range(0, n - i - 1):
                h1 = self.humans[j]
                h2 = self.humans[j+1]
                if (not h1.priority and h2.priority) or \
                   (h1.priority == h2.priority and h1.age < h2.age):
                    self.humans[j], self.humans[j+1] = self.humans[j+1], self.humans[j]

    def rearrange_queue(self):
        i = 0
        while i < len(self.humans) - 1:
            current = self.humans[i]
            next_person = self.humans[i+1]
            is_family = False
            for member in current.family:
                if member.id_number == next_person.id_number:
                    is_family = True
                    break
            
            if is_family:
                for k in range(i + 2, len(self.humans)):
                    potential_swap = self.humans[k]
                    is_k_family = False
                    for m in current.family:
                        if m.id_number == potential_swap.id_number:
                            is_k_family = True
                            break
                    
                    if not is_k_family:
                        self.humans[i+1], self.humans[k] = self.humans[k], self.humans[i+1]
                        break
            i += 1
        
