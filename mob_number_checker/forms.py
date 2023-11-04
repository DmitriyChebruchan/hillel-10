from django import (
    forms,
)
import phonenumbers
from .models import (
    PhoneNumber,
    VerificationPair,
)


class VarificationForm(forms.ModelForm):
    class Meta:
        model = VerificationPair
        fields = ["code"]


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ["phone_number"]

    def clean_phone_number(
        self,
    ):
        phone = self.cleaned_data["phone_number"]

        # phone check
        if not phone:
            raise forms.ValidationError("Phone is missing")

        min_phone_length = 8  # Change to your desired minimum length
        if len(phone) < min_phone_length:
            raise forms.ValidationError("Phone is too short")

        try:
            parsed_phone = phonenumbers.parse(phone)
            phone_format = phonenumbers.PhoneNumberFormat.INTERNATIONAL
            normalized_number = phonenumbers.format_number(
                numobj=parsed_phone,
                num_format=phone_format,
            )
        except phonenumbers.phonenumberutil.NumberParseException:
            raise forms.ValidationError("Invalid phone number")

        return normalized_number
