import datetime

class Person:
    def __init__(self, first_name, last_name, sex, address, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.address = address
        self.birth_date = birth_date
    
    def __hash__(self):
        return hash(frozenset(self.__dict__.iteritems()))

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def age_in_days_at_date(self, date):  
        age = (date - datetime.datetime.strptime(self.birth_date, '%d.%m.%Y').date()).days
        return age
        
    # for unittesting current_age method
    def age_at_date(self, date):    
        return self.age_in_days_at_date(date)/365
    
    #for creating youngest_person method
    def age_in_days(self):
        return self.age_in_days_at_date(datetime.date.today())
    
    def current_age (self):
        current_date = datetime.date.today()
        return self.age_at_date(current_date)
        
    def to_text_line(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.sex + ', ' + self.address + ', ' + self.birth_date
    

    def __repr__(self):
        return repr((self.first_name, self.last_name, self.sex, self.address, self.birth_date))

class AddressBook:
    def __init__(self):
        self.persons = []
        self.parents = {}

    def add_person(self, person):
        self.persons.append(person)

    def search_person(self, name): #returns a list of persons
        y = []
        for person in self.persons:
            if name == person.first_name or name == person.last_name:
                y.append(person)
        return y
        
    @staticmethod
    def person_from_text_line(line):
        stripped_line = line.strip()
        person_info = stripped_line.split(',')
        person_info_name = person_info[0].split(' ')
        person_info_fname = person_info_name[0]              
        person_info_name_lname = person_info_name[1]
        person_info_sex = person_info[1].strip()
        person_info_birthdate = person_info[-1].strip()
        person_info_address = ','.join(person_info[2:-1]).strip()
        return Person(person_info_fname, person_info_name_lname, person_info_sex, person_info_address, person_info_birthdate)
        
    def load_from_file (self, file_name):
        address_book_file = open(file_name)
        for line in address_book_file:
            self.add_person(cls.person_from_text_line(line))
        address_book_file.close()
        
    def write_to_file(self, file_name):
        address_book_file = open(file_name, 'w') #it is necessary to write a line for every person object
        for person in self.persons:
            address_book_file.write(person.to_text_line() + '\n')
        address_book_file.close()
    
    def youngest_person(self):
        if len(self.persons) == 0:
            return None
        sorted_age = sorted(self.persons, key = lambda person: person.age_in_days(), reverse=False)
        return sorted_age[0]

    def average_age(self):
        age_list = []
        for person in self.persons:
            age_list.append(person.current_age())
        # age_list = [p.current_age() for p in self.persons]
        if len(age_list) == 0:
            raise ValueError ("Can't divide by zero! You must have at least one contact in your address book!")
        age_mean = float(sum(age_list))/len(age_list)
        return age_mean

    def get_all_persons(self):
        return self.persons
    
    #parents is a dictionary
    #parent is the key and child is the value
    def add_relationship_child(self, parent, child):
        self.parents.setdefault(parent, []).append(child)

    def find_children(self, parent):
        return self.parents.get(parent, [])

    def find_grandchildren(self, grandparent):
        grandchildren = []
        for parent in self.find_children(grandparent):
            grandchildren += self.find_children(parent)
        return grandchildren

    def find_siblings(self, person):
        for parent, children in self.parents.items():
			if person in children:
				siblings = list(children)
				siblings.remove(person)
				return siblings
        return []
        
    def find_parents(self, person):
        parents_lst = []
        for parent, children in self.parents.items():
            if person in children:
                parents_lst.append(parent)
        return parents_lst
    
    def find_mother(self, person):
        for parent in self.find_parents(person):
            if parent.sex == 'F':
                return parent
        return None
        
    def find_father(self, person):
        for parent in self.find_parents(person):
            if parent.sex == 'M':
                return parent
        return None
        
    def find_cousins(self, person):
        parents = self.find_parents(person)
        if parents == []:
            return []
        uncles_and_aunts = []
        for p in parents:
            uncles_and_aunts += self.find_siblings(p)
        cousins = []
        for i in uncles_and_aunts:
            cousins += self.find_children(i)
        return cousins

    def find_uncles_with_gender(self, person, sex):
        parents = self.find_parents(person)
        if parents == []:
            return []
        uncles_and_aunts = []
        for p in parents:
            uncles_and_aunts += self.find_siblings(p)
        uncles = []
        for u in uncles_and_aunts:
            if u.sex == sex:
                uncles.append(u)
        return uncles
    
    def find_uncles(self, person):
        return self.find_uncles_with_gender(person, 'M')
        
    def find_aunts(self, person):
        return self.find_uncles_with_gender(person, 'F')

    
    def __repr__(self):
        return '%s' % self.persons

