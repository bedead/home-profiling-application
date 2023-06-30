import eel
import __auth__
import __generateData__

eel.init('web', allowed_extensions=['.js', '.html','.css'])

eel.start(
    'starter.html',
    mode='chrome',
    port=8003,
    shutdown_delay=5,
    )