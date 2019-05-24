from django.forms.utils import ErrorList
from django import forms

class FormUserNeededMixin(object):

	def form_valid(self,form):
		if not self.request.user.is_authenticated():
			form._errors[forms.forms.NON_FIELD_ERRORS]= ErrorList(["User must be logged in "])
			return self.form_invalid(form)
		form.instance.user=self.request.user
		return super(FormUserNeededMixin, self).form_valid(form) 