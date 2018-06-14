from django.core.management.base import BaseCommand, CommandError
from cli_example.models import City as city_instance, Baranggay as baranggay_instance, Resident as resident_instance
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):

    help = 'prints no args if there are no args'

    def add_arguments(self, parser):
        """ Add City"""
        parser.add_argument(
            '--add_city',
            action = 'store_true',
            dest = 'add_city',
            help = 'Add city'
        )
        """delete city"""
        parser.add_argument(
            '--delete_city',
            action = 'store_true',
            dest = 'delete_city',
            help= 'delete city'
        )

        """ Update City"""
        parser.add_argument(
            '--update_city',
            action = 'store_true',
            dest = 'update_city',
            help = 'Update City'
        )

        """new baranggay"""
        parser.add_argument(
            '--add_baranggay',
            action = 'store_true',
            dest = 'add_baranggay',
            help = 'Add Baranggay'
        )
        """update baranggay"""
        parser.add_argument(
            '--update_baranggay',
            action = 'store_true',
            dest = 'update_baranggay',
            help = 'Update Baranggay'
        )
        """delete baranggay"""
        parser.add_argument(
            '--delete_baranggay',
            action = 'store_true',
            dest = 'delete_baranggay',
            help= 'delete city'
        )

        parser.add_argument(
            '--add_resident',
            action = 'store_true',
            dest = 'new_resident',
            help = 'new resident'
        )
        parser.add_argument(
            '--update_resident',
            action = 'store_true',
            dest = 'update_resident',
            help = 'update resident'
        )
        parser.add_argument(
            '--delete_resident',
            action = 'store_true',
            dest = 'delete_resident',
            help= 'delete resident'
        )
        parser.add_argument(
            '--get_resident_updated_today',
            action = 'store_true',
            dest = 'get_resident_updated_today',
            help= 'get resident updated today'
        )

    def handle(self, *args, **options):
        
        
        def view_resident():
            
            try:
                resident  = resident_instance.objects.all()
                
                print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Updated"))
                for obj in resident:
                    print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                        obj.baranggay.baranggay, obj.street, obj.house_no, 
                        obj.date_created.strftime('%m/%d/%y')))
            except resident_instant.DoesNotExist:
                raise CommandError('Resident does not exist')
        
        def view_city():
            try:
                print("All Cities")
                city = city_instance.objects.all()
                print("{:^10}|{:^10}|{:^10}|".format("ID","City","Date Updated"))
                for obj in city:
                    print("{:^10}|{:^10}|{:^10}|".format(obj.id, obj.city, obj.date_created.strftime('%m/%d/%y')))
            except city_instance.DoesNotExist:
                raise CommandError('City "%s" Does not exist' %city_id)
        
        def view_baranggay():
            try:
                print("All Baranggay")
                baranggay = baranggay_instance.objects.all()
                print("{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","City","Baranggay","Date Updated"))
                for obj in baranggay:
                    print("{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.city.city, obj.baranggay,obj.date_created.strftime('%m/%d/%y')))
            except baranggay_instance.DoesNotExist:
                raise CommandError ('Baranggay DoesNotExist')
        def view_baranggay_by_city(city_id):
            try:
                print("Baranggays from city"+ city_id.city)
                baranggay = baranggay_instance.objects.filter(city= city_id)
                print("{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","City","Baranggay","Date Updated"))
                for obj in baranggay:
                    print("{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.city.city, obj.baranggay,obj.date_created.strftime('%m/%d/%y')))
            except baranggay_instance.DoesNotExist:
                raise CommandError ('Baranggay DoesNotExist')

        def choose_baranggay(baranggay_id):
            try:
                return baranggay_instance.objects.get(pk=baranggay_id)
            except baranggay_instance.DoesNotExist:
                print("Baranggay Does not exist")    
                return False

        def choose_city(city_id):
            try:
                return city_instance.objects.get(pk=city_id)
            except:
                print("City does not exist") 

        def choose_resident(resident_id):
            try:
                return resident_instance.objects.get(pk=resident_id)
            except:
                print("Resident does not exist")
        
        """Options"""    

        if options['add_city']:
            
            city_name = str(input("Enter City name:  "))
            date = timezone.now()

            city_obj = city_instance(city= city_name , date_created= date)
            city_obj.save()
            print("City Saved Successfully")
        
        if options['update_city']:
            view_city()
            city_id = int(input("Enter the City ID you want to update: "))
            city_obj = choose_city(city_id)
            city_obj.city = str(input("Enter New City Name: "))
            city_obj.date_created = timezone.now()
            city_obj.save()
            print("Successfully Updated")

        if options['add_baranggay']:
            view_city()
            city_id = int(input("Enter the City ID  : "))
            baranggay_name = str(input("Please Enter baranggay Name:"))
            baranggay_obj = baranggay_instance(city =choose_city(city_id), baranggay = baranggay_name, date_created= timezone.now())
            baranggay_obj.save()
            print("Baranggay saved Successfully")

        if options['update_baranggay']:
            view_baranggay()
            baranggay_obj = choose_baranggay(int(input("Enter the Baranggay ID you want to update : ")))
            view_city()
            baranggay_obj.city =choose_city(int(input("Enter City ID : ")))
            baranggay_obj.baranggay = str(input("Please Enter new baranggay Name:"))
            baranggay_obj.date_created = timezone.now()
            baranggay_obj.save()
            print("Baranggay saved Successfully")

        if options['delete_city']:
            view_city()
            city_obj = choose_city(int(input("Enter the ID of the City you wish to delete :")))
            print('Successfully Deleted' + city_obj.city)
            city_obj.delete()

        if options['delete_baranggay']:
            view_baranggay()
            baranggay_obj = choose_baranggay(int(input("Enter the ID of the baranggay you wish to delete :")))
            print('Successfully Deleted ' + baranggay_obj.baranggay)
            baranggay_obj.delete()
        
        if options['new_resident']:
            view_city()
            city_obj = choose_city(int(input("Enter the ID of your city : ")))
            view_baranggay_by_city(city_obj)
            a = 1
            while a == 1:
                baranggay_obj = choose_baranggay(int(input("Enter the ID of your Baranggay : ")))
                try:
                    if(baranggay_obj.city.id == city_obj.id):
                        a = 0
                    else:
                        a = 1
                except :
                    print("Try Again")

            street = str(input("Enter street:"))
            house_number = str(input("Enter House Number"))        
            first_name = str(input("Enter your First Name: "))
            middle_name = str(input("Enter you Middle Name"))
            last_name = str(input("Enter your Last Name"))

            resident_obj = resident_instance(city= city_obj , date_created= timezone.now(), street = street ,
                         first_name = first_name, middle_name=middle_name , last_name=last_name, house_no=house_number,
                         baranggay = baranggay_obj)            

            resident_obj.save()
            print("Successfully saved the data")

        if options['update_resident']:
            view_resident()

            resident_obj = choose_resident(int(input("Enter resident ID to update : ")))

            view_city()
            city_obj = choose_city(int(input("Enter the ID of your city : ")))
            view_baranggay_by_city(city_obj)
            a = 1
            while a == 1:
                try:
                    baranggay_obj = choose_baranggay(int(input("Enter the ID of your Baranggay : ")))
                    if(baranggay_obj.city.id == city_obj.id):
                        a = 0
                    else:
                        a = 1
                
                except :
                    print("Try Again")


            resident_obj.city = city_obj
            resident_obj.baranggay  = baranggay_obj        
            resident_obj.street = str(input("Enter street:"))
            resident_obj.house_number = str(input("Enter House Number"))        
            resident_obj.first_name = str(input("Enter your First Name: "))
            resident_obj.middle_name = str(input("Enter you Middle Name"))
            resident_obj.last_name = str(input("Enter your Last Name"))
            resident_obj.save()
            print("Successfully saved the data")

        if options['delete_resident']:
            view_resident()
            resident_obj = choose_resident(int(input("Enter resident ID to update : ")))
            resident_obj.delete()
            print("Successfully deleted resident")
        
        if options['get_resident_updated_today']:
            try:
                resident  = resident_instance.objects.filter(date_created__date=timezone.now() )
                print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Updated"))

                for obj in resident:
                    print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                        obj.baranggay.baranggay, obj.street, obj.house_no, 
                        obj.date_created.strftime('%m/%d/%y')))

            except resident_instance.DoesNotExist:
                raise CommandError('Resident does not exist')    