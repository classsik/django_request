from django.http import HttpResponse


def home(request):
    return HttpResponse(f"""
    <p>Хост: {request.META['HTTP_HOST']}</p>
    <p>Браузер: {request.META['HTTP_USER_AGENT']}</p>
    <p>IP-адрес: {request.META['REMOTE_ADDR']}</p>
    """)


def error(request):
    return HttpResponse(f"""
    <p>К сожалению произошла ошибка</p>
    """, status=500)


def user(request, login=None, folder_name=None, post_id=None):
    login_text = login if login is not None else "Не задан"
    folder_name_text = folder_name if folder_name is not None else "Не задано"
    post_id_text = post_id if post_id is not None else "Не задан"

    result = f"""
    <p>Логин пользователя: {login_text}</p>
    <p>Имя папки: {folder_name_text}</p>
    <p>ID поста: {post_id_text}</p>
    """

    return HttpResponse(result)

