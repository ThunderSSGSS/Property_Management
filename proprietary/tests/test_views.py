from django.test import TestCase
from proprietary.models import Owner
from Property_Management import super_tests
from django.contrib.auth.models import User

class TestOwner(super_tests.TestAPI):
	model_class = Owner
	post_dict = {'user':'genericuser',
		'first_name':'James',
		'last_name':'Nada'}
	attribute_test_name = 'first_name'
	detail_link_name='owner_detail'
	list_link_name = 'owner_list'

	@classmethod
	def setUpTestData(cls):
		user = User.objects.create_user("genericuser","","Original2001#")