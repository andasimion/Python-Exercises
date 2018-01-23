import unittest
from family_tree import Person, AddressBook
import datetime

class TestFamilyTree(unittest.TestCase):
    
    def test_to_text_line(self):
        p = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        self.assertEqual(p.to_text_line(), 'Ana Popa, F, Corbului, nr 22, Teleorman, 02.01.1990')
        
    def test_current_age(self):
        p = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        self.assertEqual(p.age_at_date(datetime.datetime(year=2018, month=1, day=20).date()), 28)
        
    def test_get_all_persons_when_no_person_added(self):
        a = AddressBook()
        self.assertEqual(len(a.get_all_persons()), 0)
    
    # also tests the add_person method   
    def test_get_all_persons_when_one_person_added(self):
        a = AddressBook()
        pers = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        a.add_person(pers)
        self.assertEqual(len(a.get_all_persons()), 1)
        
    def test_search_person_for_a_person_that_is_not_in_address_book(self):
        a = AddressBook()
        pers_1 = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        pers_2 = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, CLuj-Napoca', '13.02.1976')
        a.add_person(pers_1)
        a.add_person(pers_2)
        self.assertEqual(a.search_person('Anca'), [])
        
    def test_search_person_for_a_person_that_is_in_address_book(self):
        a = AddressBook()
        pers_1 = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        pers_2 = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, CLuj-Napoca', '13.02.1976')
        a.add_person(pers_1)
        a.add_person(pers_2)
        self.assertEqual(a.search_person('Dorel'), [pers_2])
    
    def test_person_from_text_line(self):
        pers = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        text_line = "Ana Popa, F, Corbului, nr 22, Teleorman, 02.01.1990"
        self.assertEqual(AddressBook.person_from_text_line(text_line), pers)
        
    
    def test_youngest_person(self):
        a = AddressBook()
        pers_1 = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        pers_2 = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, CLuj-Napoca', '13.02.1976')
        pers_3 = Person ('Ioana', 'Albu', 'F', 'Malin, nr 10, Cluj-Napoca', '03.01.1990')
        a.add_person(pers_1)
        a.add_person(pers_2)
        a.add_person(pers_3)
        self.assertEqual(a.youngest_person(), pers_3)
        
    def test_youngest_person_on_empty_address_book(self):
        a = AddressBook()
        self.assertEqual(a.youngest_person(), None)
    
    def test_average_age_on_address_book_with_two_contacts(self):
        a = AddressBook()
        pers_1 = Person('Ana', 'Popa', 'F', 'Corbului, nr 22, Teleorman',  '02.01.1990')
        pers_2 = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, CLuj-Napoca', '13.02.1976')
        a.add_person(pers_1)
        a.add_person(pers_2)
        self.assertEqual(a.average_age(), 34.5)
        
    def test_average_age_on_address_book_with_no_contacts(self):
        a = AddressBook()
        with self.assertRaises(ValueError):
            a.average_age()
        
    def test_find_children_for_parent_with_no_children(self):
        a = AddressBook()
        parent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        a.add_person(parent)
        self.assertEqual(a.find_children(parent), [])
        
    # also tests add_relationship_children method    
    def test_find_children_for_parent_with_two_children(self):
        a = AddressBook()
        parent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        child_1 = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.2000')
        child_2 = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(parent)
        a.add_person(child_1)
        a.add_person(child_2)
        a.add_relationship_child(parent, child_1)
        a.add_relationship_child(parent, child_2)
        self.assertEqual(sorted(a.find_children(parent)), sorted([child_1, child_2]))
    
    # is this necesary?
    def test_find_children_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        self.assertEqual(a.find_children(person), [])
        
    def test_find_grandchildren_for_grandparent_with_two_grandchildren(self):
        a = AddressBook()
        grandparent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1966')
        parent_1 = Person('Maria', 'Popescu', 'F', '1 Mai, nr 43, Cluj-Napoca', '19.09.1990')
        parent_2 = Person('Ionut', 'Iftimie', 'M', '21 Decembrie, nr 25, Cluj-Napoca', '24.01.1985')
        child_1 = Person('Tudor', 'Popescu', 'M', '1 Mai, nr 43, Cluj-Napoca', '25.01.2010')
        child_2 = Person('Ioana', 'Iftimie', 'F', '21 Decembrie, nr 25, Cluj-Napoca', '04.05.2002')
        a.add_relationship_child(parent_1, child_1)
        a.add_relationship_child(parent_2, child_2)
        a.add_relationship_child(grandparent, parent_1)
        a.add_relationship_child(grandparent, parent_2)
        self.assertEqual(a.find_grandchildren(grandparent),[child_1, child_2])
        
    def test_find_grandchildren_for_grandparent_with_no_grandchildren(self):
        a = AddressBook()
        parent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1966')
        child_1 = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.2000')
        child_2 = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(parent)
        a.add_person(child_1)
        a.add_person(child_2)
        a.add_relationship_child(parent, child_1)
        a.add_relationship_child(parent, child_2)
        self.assertEqual(a.find_grandchildren(parent),[])
        
    def test_find_grandchildren_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1966')
        self.assertEqual(a.find_grandchildren(person),[])
    
    def test_find_siblings_for_two_siblings(self):
        a = AddressBook()
        parent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        child_1 = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.2000')
        child_2 = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(parent)
        a.add_person(child_1)
        a.add_person(child_2)
        a.add_relationship_child(parent, child_1)
        a.add_relationship_child(parent, child_2)
        self.assertEqual(a.find_siblings(child_1), [child_2])
        self.assertEqual(a.find_siblings(child_2), [child_1])
        
    def test_find_siblings_for_one_single_child(self):
        a = AddressBook()
        parent = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        child = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.2000')
        a.add_person(parent)
        a.add_person(child)
        a.add_relationship_child(parent, child)
        self.assertEqual(a.find_siblings(child), [])
         
    def test_find_siblings_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.2000')
        self.assertEqual(a.find_siblings(person), [])
        
    def test_find_parents_for_child_with_two_parents(self):
        a = AddressBook()
        parent_1 = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        parent_2 = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.1980')
        child_1 = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(parent_1)
        a.add_person(parent_2)
        a.add_person(child_1)
        a.add_relationship_child(parent_1, child_1)
        a.add_relationship_child(parent_2, child_1)
        self.assertEqual(sorted(a.find_parents(child_1)), sorted([parent_1, parent_2]))
    
    def test_find_parents_for_person_with_no_parents(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        a.add_person(person)
        self.assertEqual(a.find_parents(person), [])
    
    def test_find_parents_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        self.assertEqual(a.find_parents(person), [])
        
    def test_find_mother_for_child_with_mother(self):
        a = AddressBook()
        father = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        mother = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.1980')
        child = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(father)
        a.add_person(mother)
        a.add_person(child)
        a.add_relationship_child(father, child)
        a.add_relationship_child(mother, child)
        self.assertEqual(a.find_mother(child), mother)
    
    def test_find_mother_for_child_with_no_mother(self):
        a = AddressBook()
        father = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        child = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(father)
        a.add_person(child)
        a.add_relationship_child(father, child)
        self.assertEqual(a.find_mother(child), None)
        
    def test_find_mother_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        self.assertEqual(a.find_mother(person), None)
        
    def test_find_father_for_child_with_father(self): 
        a = AddressBook()
        father = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        mother = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.1980')
        child = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(father)
        a.add_person(mother)
        a.add_person(child)
        a.add_relationship_child(father, child)
        a.add_relationship_child(mother, child)
        self.assertEqual(a.find_father(child), father) 
    
    def test_find_father_for_child_no_father(self):
        a = AddressBook()
        mother = Person('Maria', 'Iftimie', 'F', 'Paltinis, nr 23, Cluj-Napoca', '19.09.1980')
        child = Person('Ionut', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '24.01.1998')
        a.add_person(mother)
        a.add_person(child)
        a.add_relationship_child(mother, child)
        self.assertEqual(a.find_father(child), None)
    
    def test_find_father_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Dorel', 'Iftimie', 'M', 'Paltinis, nr 23, Cluj-Napoca', '13.02.1976')
        self.assertEqual(a.find_father(person), None)
        
    def test_find_cousins_for_person_with_three_cousins(self):
        a = AddressBook()
        grandparent = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        parent_1 = Person('Ioana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '21.04.1970')
        parent_2 = Person('Mihai', 'Popa', 'M', 'Malin, nr 34, Cluj-Napoca', '03.12.1973')
        parent_3 = Person('Liviu', 'Popa', 'M', 'Stefan cel Mare, nr 12, Bacau', '31.10.1976')
        child_1 = Person('Maria', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '30.01.1995')
        child_2 = Person('Ana', 'Popa', 'M', 'Malin, nr 34, Cluj-Napoca', '13.12.1999')
        child_3 = Person('Delia', 'Popa', 'M', 'Malin, nr 34, Cluj-Napoca', '13.12.1999')
        child_4 = Person('Tudor', 'Popa', 'M', 'Stefan cel Mare, nr 12, Bacau', '09.05.2006')
        a.add_person(grandparent)
        a.add_person(parent_1)
        a.add_person(parent_2)
        a.add_person(parent_3)
        a.add_person(child_1)
        a.add_person(child_2)
        a.add_person(child_3)
        a.add_person(child_4)
        a.add_relationship_child(grandparent, parent_1)
        a.add_relationship_child(grandparent, parent_2)
        a.add_relationship_child(grandparent, parent_3)
        a.add_relationship_child(parent_1, child_1)
        a.add_relationship_child(parent_2, child_2)
        a.add_relationship_child(parent_2, child_3)
        a.add_relationship_child(parent_3, child_4)
        self.assertEqual(a.find_cousins(child_1), [child_2, child_3, child_4])
        
    def test_find_cousins_for_person_with_no_cousin(self):
        a = AddressBook()
        person = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        a.add_person(person)
        self.assertEqual(a.find_cousins(person), [])
        
    def test_find_cousins_for_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        self.assertEqual(a.find_cousins(person), [])
        
    def test_find_uncles_with_gender_for_person_with_two_uncles(self):
        a = AddressBook()
        grandparent_1 = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        grandparent_2 = Person('Ioana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '21.04.1945')
        parent_1 = Person('Mihai', 'Popa', 'M', 'Avram Iancu, nr 34, Floresti', '03.12.1973')
        parent_2 = Person('Maria', 'Avram', 'f', 'Malin, nr 34, Cluj-Napoca', '31.10.1976')
        parent_3 = Person('Ana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '30.01.1970')
        parent_4 = Person('Ioan', 'Avram', 'M', 'Malin, nr 34, Cluj-Napoca', '13.12.1970')
        child = Person('Delia', 'Avra,', 'F', 'Malin, nr 34, Cluj-Napoca', '13.12.1999')
        a.add_person(grandparent_1)
        a.add_person(grandparent_2)
        a.add_person(parent_1)
        a.add_person(parent_2)
        a.add_person(parent_3)
        a.add_person(parent_4)
        a.add_person(child)
        a.add_relationship_child(grandparent_1, parent_1)
        a.add_relationship_child(grandparent_1, parent_2)
        a.add_relationship_child(grandparent_2, parent_3)
        a.add_relationship_child(grandparent_2, parent_4)
        a.add_relationship_child(parent_2, child)
        a.add_relationship_child(parent_4, child)
        self.assertEqual(a.find_uncles_with_gender(child, 'M'), [parent_1]) 
        self.assertEqual(a.find_uncles_with_gender(child, 'F'), [parent_3])   
        
    def test_find_uncles_with_gender_when_person_has_no_uncles(self):
        a = AddressBook()
        person = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        a.add_person(person)
        self.assertEqual(a.find_uncles_with_gender(person, 'M'), [])
        self.assertEqual(a.find_uncles_with_gender(person, 'F'), [])
        
    def test_find_uncles_with_gender_when_person_not_in_address_book(self):
        a = AddressBook()
        person = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        self.assertEqual(a.find_uncles_with_gender(person, 'M'), [])
        self.assertEqual(a.find_uncles_with_gender(person, 'F'), [])
        
    def test_find_uncles_when_person_has_two_uncles(self):
        a = AddressBook()
        grandparent_1 = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        grandparent_2 = Person('Ioana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '21.04.1945')
        parent_1 = Person('Mihai', 'Popa', 'M', 'Avram Iancu, nr 34, Floresti', '03.12.1973')
        parent_2 = Person('Maria', 'Avram', 'f', 'Malin, nr 34, Cluj-Napoca', '31.10.1976')
        parent_3 = Person('Ana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '30.01.1970')
        parent_4 = Person('Ioan', 'Avram', 'M', 'Malin, nr 34, Cluj-Napoca', '13.12.1970')
        parent_5 = Person('Liviu', 'Avram', 'M', 'Paltinis, nr 23, Cluj-Napoca', '15.06.1980')
        child = Person('Delia', 'Avra,', 'F', 'Malin, nr 34, Cluj-Napoca', '13.12.1999')
        a.add_person(grandparent_1)
        a.add_person(grandparent_2)
        a.add_person(parent_1)
        a.add_person(parent_2)
        a.add_person(parent_3)
        a.add_person(parent_4)
        a.add_person(child)
        a.add_relationship_child(grandparent_1, parent_1)
        a.add_relationship_child(grandparent_1, parent_2)
        a.add_relationship_child(grandparent_2, parent_3)
        a.add_relationship_child(grandparent_2, parent_4)
        a.add_relationship_child(grandparent_2, parent_5)
        a.add_relationship_child(parent_2, child)
        a.add_relationship_child(parent_4, child)  
        self.assertEqual(sorted(a.find_uncles(child)), sorted([parent_1, parent_5]))    
        
        
    def test_find_aunts_when_person_has_two_aunts(self):
        a = AddressBook()
        grandparent_1 = Person('Mirabela', 'Popa', 'F', 'Avram Iancu, nr 34, Floresti', '14.11.1950')
        grandparent_2 = Person('Ioana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '21.04.1945')
        parent_1 = Person('Mihai', 'Popa', 'M', 'Avram Iancu, nr 34, Floresti', '03.12.1973')
        parent_2 = Person('Maria', 'Avram', 'f', 'Malin, nr 34, Cluj-Napoca', '31.10.1976')
        parent_3 = Person('Ana', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '30.01.1970')
        parent_4 = Person('Ioan', 'Avram', 'M', 'Malin, nr 34, Cluj-Napoca', '13.12.1970')
        parent_5 = Person('Livia', 'Avram', 'F', 'Paltinis, nr 23, Cluj-Napoca', '15.06.1980')
        child = Person('Delia', 'Avra,', 'F', 'Malin, nr 34, Cluj-Napoca', '13.12.1999')
        a.add_person(grandparent_1)
        a.add_person(grandparent_2)
        a.add_person(parent_1)
        a.add_person(parent_2)
        a.add_person(parent_3)
        a.add_person(parent_4)
        a.add_person(child)
        a.add_relationship_child(grandparent_1, parent_1)
        a.add_relationship_child(grandparent_1, parent_2)
        a.add_relationship_child(grandparent_2, parent_3)
        a.add_relationship_child(grandparent_2, parent_4)
        a.add_relationship_child(grandparent_2, parent_5)
        a.add_relationship_child(parent_2, child)
        a.add_relationship_child(parent_4, child)  
        self.assertEqual(a.find_aunts(child), [parent_3, parent_5])    
                    
                    
if __name__ == '__main__':
    unittest.main()	
