from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from escola.models import Aluno


class AlunoTestCase(APITestCase):
    def setUp(self) -> None:
        self.aluno_test1 = Aluno.objects.create(
                nome="Iracilda Mamedes",
                rg="31299393",
                cpf="04217741421",
                data_nascimento="1982-02-25",
            )
         
        self.urls_list = reverse('Alunos-list')
        self.client = APIClient()

        self.superuser = User.objects.create_superuser(username='maercio', password='2325')

    def test_get_aluno(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(self.urls_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
