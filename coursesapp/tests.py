from django.test import TestCase, Client
from .models import Category, Branch, Contact, Course

class CourseTestCases(TestCase):

	def setUp(self) -> None:
		self.category = Category.objects.create(name = 'language', imgpath = 'image.jpg')
		self.branch = Branch.objects.create(latitude = 'lat', longitude = 'long', address = 'Ibraimova, 24')
		self.contact = Contact.objects.create(type = 1, value = '0707070797')

		self.course = Course.objects.create(
			name = 'python',
			description = 'Python Course for Beginners',
			category = self.category,
			logo = 'logo.jpg',
			contacts = self.contact,
			branches = self.branch
		)

	def test_create_course(self):
		self.assertEqual(self.category, self.course.category)
		self.assertEqual(self.branch, self.course.branches)
		self.assertEqual(self.contact, self.course.contacts)
		self.assertEqual('python', self.course.name)
		self.assertEqual('Python Course for Beginners', self.course.description)
		self.assertEqual('logo.jpg', self.course.logo)

	def test_get_course_list(self):
		client = Client()
		response = client.get('/courses/')
		self.assertEqual(response.status_code, 200)

	def test_get_course_detail(self):
		client = Client()
		response = client.get('/courses/1')
		self.assertEqual(response.status_code, 301) # Cant understand this why 301 code returns


