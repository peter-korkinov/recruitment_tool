import json

from rest_framework.test import APIRequestFactory, APITestCase, APIClient

from recruitment_tool.candidates.views import CandidateView
from recruitment_tool.skills.models import SkillModel


class CreateCandidateTest(APITestCase):
    CLIENT_DATA = {
        'first_name': 'dancho',
        'last_name': 'Kanchev',
        'email': 'dancho@maila.com',
        'bio': 'interesna',
        'birth_date': '2000-10-10',
        'skills': [1]
    }

    SKILL1_DATA = {
        'title': 'python'
    }

    SKILL2_DATA = {
        'title': 'javascript'
    }

    def setUp(self):
        client = APIClient()

        SkillModel.objects.create(**{'title': 'blqjangular'})
        # SkillModel.objects.create(title='JavaScript')

        response = client.post('/candidates/', json.dumps(self.CLIENT_DATA), content_type='application/json')
        print(response)
        # self.response_dict = json.loads(response.body)
        self.response_dict = {}

    def test_post_returns_json_with_the_attrs_that_are_set(self):
        self.assertEqual(self.response_dict, self.response_dict | self.CLIENT_DATA)

    # def test_created_record_has_int_id(self):
    #     print(self.response_dict)


# class CandidateViewTest(TestCase):
#     def test_get(self):
#         client = Client()
#         response = client.get('candidate/1')
#         self.assertJSONEqual()