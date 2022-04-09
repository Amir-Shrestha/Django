from django.shortcuts import render
from django.views.generic import View
from . models import *

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):

        # get <QuerySet> of all person objects
        all_person = Person.objects.all()
        print('All Person Objects of Person class:\n ',all_person)
        #get <QuerySet> of all city objects
        all_city = City.objects.all()
        print('All all_city Objects of City class:\n ',all_city)
        #get <QuerySet> of all interest objects
        all_interest = Interest.objects.all()
        print('All all_interest Objects of Interest class:\n ',all_interest)
        #get <QuerySet> of all person_street_address objects
        all_person_street_address = PersonStreetAddress.objects.all()
        print('All person_street_address Objects of PersonStreetAddress class:\n ',all_person_street_address)


        # #get all attributes/property of all person_objects QuerySet   #Person and Interest M-N relationship
        # for person in all_person:
        #     print('A Person Object: ',person)
        #     print('A Person Object name attribute: ',person.name)
        #     print('A Person Object mobile attribute: ',person.mobile)
        #     print('A Person Object QuerySet attribute as interest_obj that holds all interest_object of a Person_Object: ',person.interest_obj) # CustomeApp1.Interest.None # here,interest_obj is 'ManyRelatedManager' object which is not iterable so use all() to fetch QuerySet But if it was OnToOneRelatedManager no all() needed
        #     #get interest_object as attributes of person_objects
        #     print('A Person Object QuerySet attribute as interest_obj that holds all interest_object of a Person_Object: ',person.interest_obj.all())
        #     print(type(person.interest_obj.all()))
        #     a_person_all_interest = person.interest_obj.all() # Fetching data using forward relationship
        #     for interest in a_person_all_interest:
        #         #get attributes of interest_object feteching from person_objects attributes i.e : person.interest_obj
        #         print(interest)


        # # get all PersonStreetAddress_objects from PersonStreetAddress_objects_QuerySet
        # for person_street_address in all_person_street_address:
        #     print('     A person_street_address Object: ',person_street_address)
        # #     #get all attributes/property of individul PersonStreetAddress_objects # Fetching data using forward relationship
        #     print('         person_obj as an attribute of a person_street_address Object: ',person_street_address.person_obj)
        #     print('         city_obj  as an attribute of a person_street_address Object: ',person_street_address.city_obj)
        #     print('         street as an attribute of a person_street_address Object: ',person_street_address.street)

        #     # Person and PersonStreetAddress 1-1 relationship
        #     #get attributes of person_obj feteching from person_street_address attributes i.e : person_street_address.person_obj
        #     # 1-1 relationship so no iteration so no need of .all()
            # print('         person_obj as an attribute of a person_street_address Object: ',person_street_address.person_obj)
            # print('             name attributes of a person_obj(an attribute of a person_street_address Object): ',person_street_address.person_obj.name) # Fetching data using forward relationship
            # print('             mobile attributes of a person_obj(an attribute of a person_street_address Object): ',person_street_address.person_obj.mobile)
            # print('             interest_obj attributes of a person_obj(an attribute of a person_street_address Object): ',person_street_address.person_obj.interest_obj)
            # print('             interest_obj attributes of a person_obj(an attribute of a person_street_address Object): ',person_street_address.person_obj.interest_obj.all()) # this can be iterable

        #     # City and PersonStreetAddress 1-M relationship
        #     #get attributes of city_obj feteching from person_street_address attributes i.e : person_street_address.city_obj
        #     # 1-M relationship so no iteration
            # print("         An city_obj attribute of person_street_address(This is object of City class) ", person_street_address.city_obj)
            # print("             This is attributes/property of city_obj ", person_street_address.city_obj.city_name)
            #note : object of one class itself can be attributes of another class if any kind of relationship exist between them


        # # Forward Relationship
        # print('Forward Relationship ********************')
        # for person_street_address in all_person_street_address:
        #     print(person_street_address.person_obj)

        # # Reverse Relationship
        # print('Reverse Relationship ********************')
        # for city in all_city:
        #     print(city) #object of City class
        #     for street in city.personstreetaddress_set.all():
        #         print(street ,"...")

        # here, City and PersonStreetAddress has ForeignKey/OneToMany relationship. One city can have many street.
        # here, city.personstreetaddress_set.all()
            # city is object of City class
            # personstreetaddress is object of PersonStreetAddress class
            # as it is Data Fetching using Reverse Relationship so _set : ie personstreetaddress_set
            # all() as City and PersonStreetAddress has ForeignKey/OneToMany relationship.One city can have many street.



        # get <QuerySet> of all employee objects
        # all_employee = Employee.objects.all()
        # print(all_employee)

        # emp_1 =  Employee.objects.filter(name="Amir")
        # print(emp_1)



        emp1 = Employee.objects.get(name="Amir")
        print(emp1)
        emp1_dep = emp1.department_obj
        print(emp1_dep)
        print(emp1_dep.name)


       # all_teachers =  Employee.objects.filter(department_obj=teacher_dep)
        # print(all_teachers) #Not poosiibel so solution

        dep1 = Department.objects.get(name="Teacher")
        print(dep1)
        dep1_emp = dep1.employees.all()
        print(dep1_emp)


        # # 1-M
        # print(PersonStreetAddress.objects.filter(city__name = "Kathmandu"))
        # print(PersonStreetAddress.objects.filter(city__name__startswith = "Kat"))
        # print(City.objects.filter(personstreetaddress__name = "Kathmandu"))

        context = {}
        return render(request, "app1/home.html")
