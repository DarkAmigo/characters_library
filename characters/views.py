from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, Universe, Ability
from .forms import CharacterForm
from users.decorators import role_required
from django.contrib.auth.decorators import login_required

@login_required
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters/list.html', {'characters': characters})

@login_required
def characters_by_universe(request, universe_id):
    universe = get_object_or_404(Universe, id=universe_id)
    characters = Character.objects.filter(universe=universe)
    return render(request, 'characters/list_by_universe.html', {
        'universe': universe,
        'characters': characters
    })

@login_required
def characters_by_ability(request, ability_id):
    ability = get_object_or_404(Ability, id=ability_id)
    characters = Character.objects.filter(abilities=ability)
    return render(request, 'characters/list_by_ability.html',{
        'ability': ability,
        'characters': characters
    })

@login_required
@role_required(['admin'])
def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()

    return render(request, 'characters/character_form.html', {'form': form})

@login_required
@role_required(['admin'])
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        character.delete()
        return redirect("character_list")
    return render(request, "characters/character_confirm_delete.html", {"character": character})