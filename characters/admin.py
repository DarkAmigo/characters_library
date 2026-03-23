from django.contrib import admin
from .models import (
    Character,
    Universe,
    Creator,
    Ability,
    Weapon,
    Team
)


admin.site.register(Character)
admin.site.register(Universe)
admin.site.register(Creator)
admin.site.register(Ability)
admin.site.register(Weapon)
admin.site.register(Team)
