from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Crée un nouvel utilisateur
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
