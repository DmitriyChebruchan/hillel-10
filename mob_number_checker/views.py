from random import (
    randint,
)

from django.shortcuts import (
    render,
    redirect,
)
from .tasks import (
    send_sms,
)

from .forms import (
    PhoneNumberForm,
    VarificationForm,
)

from .models import (
    VerificationPair,
    PhoneNumber,
)


def main(
    request,
):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            test_code = randint(
                99999,
                100000,
            )
            phone_number = form.cleaned_data.get("phone_number")
            the_number = PhoneNumber.objects.create(phone_number=phone_number)
            verification_pair = VerificationPair.objects.create(
                phone_number=the_number,
                code=test_code,
            )
            send_sms.delay(
                phone_number,
                test_code,
            )
            return redirect("/verification-" + str(verification_pair.id))

    form = PhoneNumberForm()
    return render(
        request,
        "main.html",
        {"form": form},
    )


def verification(
    request,
    pk,
):
    verification_pair = VerificationPair.objects.get(pk=pk)
    phone_number = verification_pair.phone_number
    form = VarificationForm()
    if request.method == "POST":
        form = VarificationForm(request.POST)
        if form.is_valid():
            code_entered = form.cleaned_data.get("code")
            code_sent = verification_pair.code
            print(
                code_entered,
                code_sent,
            )
            if code_entered == code_sent:
                verification_pair.delete()
                return render(
                    request,
                    "verification_completed.html",
                )
            return render(
                request,
                "code_verification.html",
                {
                    "form": form,
                    "phone_number": phone_number,
                    "verification_status": "failed",
                },
            )

    return render(
        request,
        "code_verification.html",
        {
            "form": form,
            "phone_number": phone_number,
        },
    )


def verification_completed(
    request,
):
    return render(
        request,
        "verification_completed.html",
    )
