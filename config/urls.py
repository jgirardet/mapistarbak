# Third Party Libraries
from apistar import Include
from apistar.handlers import docs_urls
from apistar.handlers import static_urls
from patients.urls import patients_urls
from users.urls import users_urls
from actes.urls import actes_urls

routes = [
    Include('/docs', docs_urls),
    Include('/static', static_urls),
    Include('/patients', patients_urls),
    Include('/users', users_urls),
    Include('/actes', actes_urls),
]
