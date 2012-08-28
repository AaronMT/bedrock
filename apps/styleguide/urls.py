from django.conf.urls.defaults import *
from mozorg.util import page

urlpatterns = patterns('',
    page('', 'styleguide/home.html'),
    page('identity/firefox/branding', 'styleguide/identity/firefox-branding.html'),
    page('sandstone', 'styleguide/sandstone-intro.html'),
    page('sandstone/buttons', 'styleguide/sandstone-buttons.html'),
    page('sandstone/colors', 'styleguide/sandstone-colors.html'),
    page('sandstone/forms', 'styleguide/sandstone-forms.html'),
    page('sandstone/grids', 'styleguide/sandstone-grids.html'),
    page('sandstone/tables', 'styleguide/sandstone-tables.html'),
    page('sandstone/tabzilla', 'styleguide/sandstone-tabzilla.html'),
    page('sandstone/typefaces', 'styleguide/sandstone-typefaces.html'),
    page('sandstone/examples', 'styleguide/sandstone-examples.html'),
)
