from django.core.management.base import BaseCommand, CommandError
from cli_example.models import City as c, Baranggay as b
from django.utils import timezone


class Command(BaseCommand):

	help = 'prints no args if there are no args'


	

	def add_arguments(self, parser):

		parser.add_argument(
			'--add_city',
			action = 'store_true',
			dest = 'add_city',
			help = 'Add city'
		)
		parser.add_argument(
			'--add_baranggay',
			action = 'store_true',
			dest = 'add_baranggay',
			help = 'Add Baranggay'
		)




	def handle(self, *args, **options):
		def view_city():
			try:
				print("All Cities")
				city = c.objects.all()
				print("{:^10}|{:^10}|{:^10}|".format("ID","City","Date Created"))
				for obj in city:
					print("{:^10}|{:^10}|{:^10}|".format(obj.id, obj.city, obj.date_created.strftime('%m/%d/%y')))
			except c.DoesNotExist:
				raise CommandError('City "%s" Does not exist' %city_id)
		
		if options['add_city']:
						
			city_name = str(input("Enter City name:  "))
			date = timezone.now()

			city_obj = c(city= city_name , date_created= date)
			city_obj.save()
			print("City Saved Successfully")
		if options['add_baranggay']:
			view_city()
			city_id = int(input("Enter City ID:"))
			baranggay_name = str(input("Please Enter baranggay Name"))
			city_obj = c.objects.get(pk=city_id)
			baranggay_obj = b(city = city_obj, baranggay = baranggay_name, baranggay_date_created= timezone.now())
			baranggay_obj.save()
			print("Baranggay saved Successfully")


		

    				


    	