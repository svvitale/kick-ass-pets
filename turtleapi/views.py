import time
from django.http import JsonResponse
from django.views import View

turtle_data = [
    # 0
    """Diamondback terrapins are turtles with concentric, diamond-shaped markings and grooves on the scutes (plates)
    of their carapaces (top shells), which range from medium gray or brown to nearly black. No two individual diamondback
    terrapins are exactly alike in coloration and pattern.""",
    # 1
    """Irwin's Snapping Turtle was first discovered by Steve Irwin, the late Crocodile Hunter, and his father, Bob Irwin,
    in the early 1990s. There is still very little known about this species,
    and biologists today are working on both collecting more specimens and observing them in the wild to learn more
    about their behavior.""",
    # 2
    """The yellow-footed tortoise gets its name from the distinctive yellow or orange scales found on its limbs.
    These animals communicate with each other with rapid head movements. Females lay approximately four to eight eggs
    in each clutch, with a year-round breeding period."""
]


class SlowApiCall(View):
    def get(self, request):
        # Simulate a slow API by delaying for 10 seconds...
        time.sleep(10)

        return JsonResponse({
            'turtles': turtle_data
        })
