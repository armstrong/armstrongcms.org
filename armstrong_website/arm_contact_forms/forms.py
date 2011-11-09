from django import forms
from django.conf import settings

from contact_form.forms import attrs_dict
from contact_form.forms import ContactForm


class ArmstrongContactForm(ContactForm):
    company = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs=attrs_dict),
                              label=u'Company')
    from_email = 'info@armstrongcms.org'

    @property
    def recipient_list(self):
        return [self.cleaned_data["email"], ]

    def save(self, fail_silently=False):
        from django.core.mail import EmailMessage
        message_dict = self.get_message_dict()
        message_dict["to"] = message_dict.pop("recipient_list")
        message_dict["cc"] = [message_dict["from_email"], ]
        message_dict["body"] = message_dict.pop("message")
        message_dict["bcc"] = [settings.BCC_EMAIL, ]
        message = EmailMessage(**message_dict)
        message.send(fail_silently=fail_silently)