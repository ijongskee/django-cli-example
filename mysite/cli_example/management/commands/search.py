from django.core.management.base import BaseCommand, CommandError
from cli_example.models import City as city_instance, Baranggay as baranggay_instance, Resident as resident_instance
from django.utils import timezone


class Command(BaseCommand):
    help = 'prints no args if there are no args'
    def add_arguments(self, parser):

        parser.add_argument('search_string', nargs='+', type=str)

        """ Get Resident by last name"""
        parser.add_argument(
            '--get_resident_by_last_name',
            action = 'store_true',
            dest = 'get_resident_by_last_name',
            help = 'Get resident by Last Name'
        )
        """ Get Resident by first name"""
        parser.add_argument(
            '--get_resident_by_first_name',
            action = 'store_true',
            dest = 'get_resident_by_first_name',
            help = 'Get resident by first Name'
        )

        """ Get Resident by baranggay"""
        parser.add_argument(
            '--get_resident_by_baranggay',
            action = 'store_true',
            dest = 'get_resident_by_baranggay',
            help = 'Get resident by baranggay'
        )
        """ Get Resident by city"""
        parser.add_argument(
            '--get_resident_by_city',
            action = 'store_true',
            dest = 'get_resident_by_city',
            help = 'Get resident by city'
        )
        
    def handle(self, *args, **options):

        
        if options['get_resident_by_last_name']:
            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Updated"))
                
            for search_string in options['search_string']:
                try:
                    resident= resident_instance.objects.filter(last_name__contains=search_string)
                    for obj in resident:
                        print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                            obj.baranggay.baranggay, obj.street, obj.house_no, 
                            obj.date_created.strftime('%m/%d/%y')))
                except resident_instance.DoesNotExist:
                    raise CommandError('resident does not exist')

        if options['get_resident_by_first_name']:

            for search_string in options['search_string']:
                print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Updated"))
                try:
                    resident = resident_instance.objects.filter(first_name__contains=search_string)
                    for obj in resident:
                        print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                            obj.baranggay.baranggay, obj.street, obj.house_no, 
                            obj.date_created.strftime('%m/%d/%y')))
                except resident_instance.DoesNotExist:
                    raise CommandError('resident does not exist')

        


        if options['get_resident_by_baranggay']:

            for search_string in options['search_string']:
                baranggay = baranggay_instance.objects.filter(baranggay__contains = search_string)
                print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Created"))
                try:
                    for baranggay_obj in baranggay:
                        resident = resident_instance.objects.filter(baranggay = baranggay_obj.id)
                        for obj in resident:
                            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                                obj.baranggay.baranggay, obj.street, obj.house_no, 
                                obj.date_created.strftime('%m/%d/%y')))
                
                except resident_instance.DoesNotExist:
                    raise CommandError('resident does not exist')


        if options['get_resident_by_city']:

            for search_string in options['search_string']:
                print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
                    "Baranggay", "Street", "House Number","Date Created"))
                city = city_instance.objects.filter(city__contains= search_string)
                
                try:
                    for city_obj in city:
                        resident = resident_instance.objects.filter(city=city_obj.id)
                        for obj in resident:
                            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
                                obj.baranggay.baranggay, obj.street, obj.house_no, 
                                obj.date_created.strftime('%m/%d/%y')))
                
                except resident_instance.DoesNotExist:
                    raise CommandError('resident does not exist')