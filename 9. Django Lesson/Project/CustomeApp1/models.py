from django.db import models

# Create your models here.

# DataBase Tables Relationship. Feteching Data using Forward and Reverse Relationship

class  Interest(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class  City(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class  Person(models.Model): #ManyToMany_with_Interest
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    interest_obj = models.ManyToManyField(Interest) # *** # a Person can have many Interest and a Interest can be assigned to many Person

    def __str__(self):
        return self.name


class  PersonStreetAddress(models.Model):#OneToOneField_with_Person & #ForeignKey/OneToMany_with_City
    person_obj = models.OneToOneField(Person, on_delete=models.CASCADE) # *** # all Person has unique PersonStreetAddress and a PersonStreetAddress is associated with unique Person # a PersonStreetAddress is assigned to a unique Person and a Person has a unique PersonStreetAddress
    city_obj = models.ForeignKey(City, on_delete=models.CASCADE) # *** # a City can have many Street and many Street can be located in one City
    street = models.CharField(max_length=20)

    def __str__(self):
        return self.person_obj.name + " from (" + self.city_obj.city_name + ", " + self.street + ")"


# Person-Interest : Person and Interest are related with ManyToMany_Relationship
#                   This means that when a person_object is created a person_object can be associated with many interest_object
#                   a Person can have many Interest and a Interest can be assigned to many Person
#                   Person_1 can have Interest(Travelling, Sport, Cooking ) and Person_2 can have Interest(Travelling, Art, Cooking )
#                   here, a Person has many Interests and single Interest is assigned to manny Person


# PersonStreetAddress-Person :  PersonStreetAddress and Person are related with OneToOneField_Relationship
#                   This means that when a PersonStreetAddress_object is created a PersonStreetAddress_object can be associated with only one Person_object
#                   a PersonStreetAddress is assigned for a unique Person and a Person has a unique PersonStreetAddress


# PersonStreetAddress-City :  PersonStreetAddress and City are related with ForeignKey_Relationship/OneToMany_Relationship
#                   This means that when a PersonStreetAddress_object is created a PersonStreetAddress_object can be associated with only one City_object but City_object can be associated with many PersonStreetAddress_object
#                   a PersonStreetAddress is assigned for a unique City but a City can be assigned to many PersonStreetAddress
#                   many person from same city but different street_address




class  Department(models.Model): #OneToMany_with_Employee
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class  Employee(models.Model): #ManyToOne_with_Department
    name = models.CharField(max_length=200)
    department_obj = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return self.name




# # M-M
# Create and Save
# sport = Interest(title="Sports")
# sport.save()
# art = Interest(title="Art")
# art.save()
# study = Interest(title="Study")
# study.save()

# person_1 = Person(name="Ram", mobile=123123123)
# person_1.save()
# person_2 = Person(name="Hari", mobile=123123123)
# person_2.save()
# person_3 = Person(name="John", mobile=123123123)
# person_3.save()
# person_4 = Person(name="Sita", mobile=123123123)
# person_4.save()
# person_5 = Person(name="Gita", mobile=123123123)
# person_5.save()
# person_6 = Person(name="Rita", mobile=123123123)
# person_6.save()

# person_1.interest_obj.add(sport)
# person_2.interest_obj.add(art)
# person_3.interest_obj.add(study)
# person_4.interest_obj.add(study)
# person_5.interest_obj.add(art)
# person_6.interest_obj.add(sport)

# person_6.interest_obj.create(title="Fashion")

#Fetech