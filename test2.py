from pywinauto import Application
from pywinauto.keyboard import send_keys

from common_lib import connect_app, click_without_id, click_without_id_invoke

target_window = connect_app('FL Studio 2024 Setup')

click_without_id_invoke(target_window, 'Next >', 'Button')
click_without_id_invoke(target_window, 'I Agree', 'Button')
