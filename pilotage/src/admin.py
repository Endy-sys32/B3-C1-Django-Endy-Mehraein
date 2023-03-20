from django.contrib import admin
from .models import TypePilotage
from .models import VehiculePilotage
from .models import CoursPilotage
from .models import Reservation
from .models import User

admin.site.register(TypePilotage)
admin.site.register(VehiculePilotage)
admin.site.register(CoursPilotage)
admin.site.register(Reservation)
admin.site.register(User)
