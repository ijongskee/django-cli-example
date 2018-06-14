from django.core.management.base import BaseCommand, CommandError
from cli_example.models import City , Baranggay, Resident 
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
				resident  = Resident.objects.all()
				
				print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Updated"))
				for obj in resident:
					print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.name,
						obj.baranggay.name, obj.street, obj.house_no, 
						obj.date_created.strftime('%m/%d/%y')))
			except resident_instant.DoesNotExist:
				raise CommandError('Resident does not exist')
		
		def view_city():
			try:
				print("All Cities")
				city = City.objects.all()
				print("{:^20}|{:^20}|{:^20}|".format("ID","City","Date Updated"))
				for obj in city:
					print("{:^20}|{:^20}|{:^20}|".format(obj.id, obj.name, obj.date_created.strftime('%m/%d/%y')))
			except City.DoesNotExist:
				raise CommandError('City "%s" Does not exist' %city_id)
		
		def view_baranggay():
			try:
				print("All Baranggay")
				baranggay = Baranggay.objects.all()
				print("{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","City","Baranggay","Date Updated"))
				for obj in baranggay:
					print("{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.city.name, obj.name,obj.date_created.strftime('%m/%d/%y')))
			except Baranggay.DoesNotExist:
				raise CommandError ('Baranggay DoesNotExist')
		def view_baranggay_by_city(city_id):
			try:
				print("Baranggays from city "+ city_id.name)
				baranggay = Baranggay.objects.filter(city= city_id)
				print("{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","City","Baranggay","Date Updated"))
				for obj in baranggay:
					print("{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.city.name, obj.name,obj.date_created.strftime('%m/%d/%y')))
			except Baranggay.DoesNotExist:
				raise CommandError ('Baranggay DoesNotExist')

		def choose_baranggay(baranggay_id):
			try:
				return Baranggay.objects.get(pk=baranggay_id)
			except Baranggay.DoesNotExist:
				print("Baranggay Does not exist")	
				return False

		def choose_city(city_id):
			try:
				return City.objects.get(pk=city_id)
			except:
				print("City does not exist") 

		def choose_resident(resident_id):
			try:
				return Resident.objects.get(pk=resident_id)
			except:
				print("Resident does not exist")
		
		"""Options"""	

		if options['add_city']:
			
			city_name = str(input("Enter City name : "))
			date = timezone.now()
			city = City(name= city_name , date_created= date)
			city.save()
			print("City Saved Successfully")
		
		if options['update_city']:
			view_city()
			city_id = int(input("Enter the City ID you want to update: "))
			city = choose_city(city_id)
			city.name = str(input("Enter New City Name : "))
			city.date_created = timezone.now()
			city.save()
			print("Successfully Updated")

		if options['add_baranggay']:
			view_city()
			city_id = int(input("Enter the City ID  : "))
			baranggay_name = str(input("Please Enter baranggay Name:"))
			baranggay = Baranggay(city =choose_city(city_id), name = baranggay_name, date_created= timezone.now())
			baranggay.save()
			print("Baranggay saved Successfully")

		if options['update_baranggay']:
			view_baranggay()
			baranggay = choose_baranggay(int(input("Enter the Baranggay ID you want to update : ")))
			view_city()
			baranggay.city =choose_city(int(input("Enter City ID : ")))
			baranggay.name = str(input("Please Enter new baranggay Name:"))
			baranggay.date_created = timezone.now()
			baranggay.save()
			print("Baranggay saved Successfully")

		if options['delete_city']:
			view_city()
			city = choose_city(int(input("Enter the ID of the City you wish to delete : ")))
			print('Successfully Deleted' + city.name)
			city.delete()

		if options['delete_baranggay']:
			view_baranggay()
			baranggay = choose_baranggay(int(input("Enter the ID of the baranggay you wish to delete : ")))
			print('Successfully Deleted ' + baranggay.name)
			baranggay.delete()
		
		if options['new_resident']:
			view_city()
			city = choose_city(int(input("Enter the ID of your city : ")))
			view_baranggay_by_city(city)
			a = 1
			while a == 1:
				baranggay = choose_baranggay(int(input("Enter the ID of your Baranggay : ")))
				try:
					if(baranggay.city.id == city.id):
						a = 0
					else:
						a = 1
				except :
					print("Try Again")

			street = str(input("Enter street: "))
			house_number = str(input("Enter House Number: "))		
			first_name = str(input("Enter your First Name: "))
			middle_name = str(input("Enter you Middle Name: "))
			last_name = str(input("Enter your Last Name: "))

			resident = Resident(city= city , date_created= timezone.now(), street = street ,
						 first_name = first_name, middle_name=middle_name , last_name=last_name, house_no=house_number,
						 baranggay = baranggay)			

			resident.save()
			print("Successfully saved the data")

		if options['update_resident']:
			view_resident()

			resident = choose_resident(int(input("Enter resident ID to update : ")))

			view_city()
			city = choose_city(int(input("Enter the ID of your city : ")))
			view_baranggay_by_city(city)
			a = 1
			while a == 1:
				try:
					baranggay = choose_baranggay(int(input("Enter the ID of your Baranggay : ")))
					if(baranggay.city.id == city.id):
						a = 0
					else:
						a = 1
				
				except :
					print("Try Again")


			resident.city = city
			resident.name  = baranggay		
			resident.street = str(input("Enter street: "))
			resident.house_number = str(input("Enter House Number: "))		
			resident.first_name = str(input("Enter your First Name: "))
			resident.middle_name = str(input("Enter you Middle Name: "))
			resident.last_name = str(input("Enter your Last Name: "))
			resident.save()
			print("Successfully saved the data")

		if options['delete_resident']:
			view_resident()
			resident = choose_resident(int(input("Enter resident ID to update : ")))
			resident.delete()
			print("Successfully deleted resident")
		
		if options['get_resident_updated_today']:
			try:
				resident  = Resident.objects.filter(date_created__date=timezone.now() )
				print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Updated"))

				for obj in resident:
					print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.name,
						obj.baranggay.name, obj.street, obj.house_no, 
						obj.date_created.strftime('%m/%d/%y')))

			except Resident.DoesNotExist:
				raise CommandError('Resident does not exist')