from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ClubMiddleware(MiddlewareMixin):
    def progress_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            exp = int(request.POST.get("experience"))
            if exp < 1:
                request.club = "Стажер"
            elif 1 <= exp <= 2:
                request.club = "Младший специалист"
            elif 2 <= exp <= 3:
                request.club = "Специалист"
            elif 3 <= exp <= 5:
                request.club = "Ведущий специалист"
            elif 5 <= exp <= 10:
                request.club = "Главный специалист"
            elif exp > 10:
                request.club = "Руководитель"
            else:
                return HttpResponseBadRequest("Извините вы не подходите для регистрации")

        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "club", "клуб не определен.")