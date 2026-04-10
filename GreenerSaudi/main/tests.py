from django.test import TestCase
from django.urls import reverse

from .views import THEME_COOKIE_NAME


class ThemeModeTests(TestCase):
	def test_default_theme_is_dark(self):
		response = self.client.get(reverse('main:home_view'))

		self.assertContains(response, 'data-bs-theme="dark"')

	def test_theme_cookie_is_applied_to_template(self):
		self.client.cookies[THEME_COOKIE_NAME] = 'dark'

		response = self.client.get(reverse('main:home_view'))

		self.assertContains(response, 'data-bs-theme="dark"')

	def test_set_theme_view_persists_cookie_and_redirects_back(self):
		response = self.client.post(
			reverse('main:set_theme_view'),
			{'theme': 'dark', 'next': reverse('main:progress_view')},
		)

		self.assertRedirects(response, reverse('main:progress_view'))
		self.assertEqual(response.cookies[THEME_COOKIE_NAME].value, 'dark')
