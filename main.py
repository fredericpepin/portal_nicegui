import os

from nicegui import app, ui
from dg_portal.commons.settings import app_settings
from dg_portal.commons.internal_paths import STATIC_DIR

app.config.title = app_settings.app_title
app.add_static_files('/static', STATIC_DIR)

# Import all modules to register their decorators
import dg_portal.modules.home
import dg_portal.modules.reports
import dg_portal.modules.engineering
import dg_portal.modules.operations
import dg_portal.modules.logistics
import dg_portal.modules.purchasing
import dg_portal.modules.sales
import dg_portal.modules.inventory
import dg_portal.modules.quality
import dg_portal.modules.maintenance
import dg_portal.modules.field_service
import dg_portal.modules.finance
import dg_portal.modules.marketing
import dg_portal.modules.hr
import dg_portal.modules.platform_admin


def run():
    ui.run(storage_secret='MY_SECRET_KEY')


if __name__ in {'__main__', '__mp_main__'}:
    run()