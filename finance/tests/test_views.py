from finance.models import Valuetion
from proprietary.models import Owner
from property.models import Patrimony, Type
from django.contrib.auth.models import User
from Property_Management import super_tests

class TestValuetion(super_tests.TestAPI):
	model_class = Valuetion
	post_dict = {'user':'genericuser',
		'patrimony_id':None,
		'description':'Nada',
		'value':120000
	}
	attribute_test_name = 'description'
	detail_link_name='valuetion_detail'
	list_link_name = 'valuetion_list'

	@classmethod
	def setUpTestData(cls):
		user = User.objects.create_user("genericuser","","Original2001#")

	def setUp(self):
		owner = Owner.objects.create(first_name='Generic',last_name='Owner')
		type = Type.objects.create(name='Casa')
		patrimony = Patrimony.objects.create(type_id=type, owner_id=owner, 
			name='generic', description='generic description')
		self.post_dict['patrimony_id'] = str(patrimony.id)		