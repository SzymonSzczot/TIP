import re

from django.http import JsonResponse
from django.views import View

from JoinMe_Server.address_book.models import Contact


class IP(View):
    def get(self, request, *args, **kwargs):
        query_string = request.environ["QUERY_STRING"]
        name = re.sub(".+=", " ", query_string)
        try:
            contact = Contact.objects.get(name=name.strip())
            return JsonResponse({"name": contact.name, "ip": contact.ip})
        except Contact.DoesNotExist:
            return JsonResponse({"Not found": "Error"})


class AddContact(View):

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        ip = request.POST.get("ip")

        if name and ip:
            contact, created = Contact.objects.get_or_create(name=name, ip=ip)
            if not created:
                return JsonResponse(
                    {
                        "Already saved": {
                            "name": contact.name,
                            "ip": contact.ip
                        }
                    }
                )

            return JsonResponse(
                {
                    "ok": "Added",
                    "contact": {
                        "name": contact.name,
                        "ip": contact.ip
                    }
                }
            )
        return JsonResponse({"error": "Wrong data"})
