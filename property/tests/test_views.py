from property.models import Type, Patrimony, Image
from Property_Management import super_tests
from proprietary.models import Owner

class TestType(super_tests.TestAPI):
	model_class = Type
	post_dict = {'name':'Casa'}
	attribute_test_name = 'name'
	detail_link_name='type_detail'
	list_link_name = 'type_list'

class TestPatrimony(super_tests.TestAPI):
	model_class = Patrimony
	post_dict = {'owner':None,
		'name':'Casa de Maputo',
		'type':None,
		'description':'Nada de mais por agora',
		'file':None
	}
	attribute_test_name = 'name'
	detail_link_name='patrimony_detail'
	list_link_name = 'patrimony_list'

	def setUp(self):
		owner = Owner.objects.create(first_name='Generic',last_name='Owner')
		type = Type.objects.create(name='Casa')
		self.post_dict['owner'] = str(owner.id)
		self.post_dict['type']=type.name

"""
class TestImage(super_tests.TestAPI):
	model_class = Image
	post_dict = {'image':None,
		'name':'Casa de Maputo'}

	attribute_test_name = 'name'
	detail_link_name='patrimony_detail'
	list_link_name = 'patrimony_list'
"""