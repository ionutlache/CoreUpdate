import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import CreateView
from CoreUpdate.settings import DEFAULT_FROM_EMAIL
from userextend.forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'
            new_user.save()

            subject = "Cont nou in aplicatie!"
            message = f"""Felicitari {new_user.first_name} {new_user.last_name},
            Contul tau a fost creat cu succes.

            Pentru autentificare te rog sa te loghezi cu username-ul: {new_user.username}
            """
            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])

            return HttpResponseRedirect(self.success_url)
        else:

            return self.form_invalid(form)
