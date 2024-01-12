from django.shortcuts import render, redirect
from telebot import TeleBot


from .forms import ContactForm
from .models import *


def send_telegram_message(data):
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot = TeleBot(token='6814468678:AAHLQx652tFC_8CL0FGowt1Wus55f4FSUA4')
    chat_id = '1230394567'  # Replace with your chat ID
    try:
        message = (f"Sizda yangni foydalanuvchi bor: \n\n"
               f"Name: {data['name']}\n"
               f"Telefon: {data['tel']}\n"
               f"Message: {data['message']}")
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=f"ERROR: {e}")


def projectslist(request):
    categories = Category.objects.all()
    projects = Projects.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            try:
                send_telegram_message(form.cleaned_data)
            except:
                pass
            return redirect("projects")
    else:
        form = ContactForm()

    context = {
        'projects': projects,
        'form': form,
        'categories': categories,
        'title': "Muhammadali Bovaqulov"
    }


    return render(request, 'myportfolio/index.html', context=context)



