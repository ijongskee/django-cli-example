from django.core.management.base import BaseCommand, CommandError
from cli_example.models import City as city_instance, Baranggay as baranggay_instance, Residence as residence_instance
from django.utils import timezone

class Command(BaseCommand):
	help = 'prints no args if there are no args'

	def add_arguments(self, parser):

		parser.add_argument('search_string', nargs='+', type=str)

		""" Add City"""
		parser.add_argument(
			'--get_residence_by_last_name',
			action = 'store_true',
			dest = 'get_residence_by_last_name',
			help = 'Get Residence by Last Name'
		)
		parser.add_argument(
			'--get_residence_by_first_name',
			action = 'store_true',
			dest = 'get_residence_by_first_name',
			help = 'Get Residence by first Name'
		)

		parser.add_argument(
			'--get_residence_by_baranggay',
			action = 'store_true',
			dest = 'get_residence_by_baranggay',
			help = 'Get Residence by baranggay'
		)

		parser.add_argument(
			'--get_residence_by_city',
			action = 'store_true',
			dest = 'get_residence_by_city',
			help = 'Get Residence by city'
		)
		parser.add_argument(
			'--get_residence_updated_today',
			action = 'store_true',
			dest = 'get_residence_updated_today',
			help = 'Get Residence Updated today'
		)
	def handle(self, *args, **options):

		
		if options['get_residence_by_last_name']:

			for search_string in options['search_string']:
				print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Updated"))
				try:
					residence = residence_instance.objects.filter(last_name=search_string)
					for obj in residence:
						print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
							obj.baranggay.baranggay, obj.street, obj.house_no, 
							obj.residence_date_created.strftime('%m/%d/%y')))
				except residence_instance.DoesNotExist:
					raise CommandError('Residence does not exist')

		if options['get_residence_by_first_name']:

			for search_string in options['search_string']:
				print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Updated"))
				try:
					residence = residence_instance.objects.filter(first_name=search_string)
					for obj in residence:
						print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
							obj.baranggay.baranggay, obj.street, obj.house_no, 
							obj.residence_date_created.strftime('%m/%d/%y')))
				except residence_instance.DoesNotExist:
					raise CommandError('Residence does not exist')

		if options['get_residence_updated_today']:
				print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Updated"))
				try:
					residence = residence_instance.objects.filter(residence_date_created=timezone.now())
					for obj in residence:
						print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
							obj.baranggay.baranggay, obj.street, obj.house_no, 
							obj.residence_date_created.strftime('%m/%d/%y')))
				except residence_instance.DoesNotExist:
					raise CommandError('Residence does not exist')


		if options['get_residence_by_baranggay']:

			for search_string in options['search_string']:
				baranggay = baranggay_instance.objects.filter(baranggay = search_string)
				print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Created"))
				try:
					for baranggay_obj in baranggay:

						residence = residence_instance.objects.filter(baranggay = baranggay_obj.id)
						for obj in residence:
							print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
								obj.baranggay.baranggay, obj.street, obj.house_no, 
								obj.residence_date_created.strftime('%m/%d/%y')))
				except residence_instance.DoesNotExist:
					raise CommandError('Residence does not exist')

		if options['get_residence_by_city']:

			for search_string in options['search_string']:
				print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("ID","First Name","Middle Name","Last Name", "City",
					"Baranggay", "Street", "House Number","Date Created"))
				city = city_instance.objects.filter(city= search_string)
				try:
					for city_obj in city:
						residence = residence_instance.objects.filter(city=city_obj.id)
						for obj in residence:
							print("{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(obj.id, obj.first_name, obj.middle_name, obj.last_name, obj.city.city,
								obj.baranggay.baranggay, obj.street, obj.house_no, 
								obj.residence_date_created.strftime('%m/%d/%y')))
				except residence_instance.DoesNotExist:
					raise CommandError('Residence does not exist')
		
