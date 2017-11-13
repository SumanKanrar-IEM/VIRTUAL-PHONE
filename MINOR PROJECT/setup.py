from distutils.core import setup
import os, sys
import py2exe
setup(console=['homescreen.py'],
      options = {
          'py2exe': {
                  'packages': ['PyQt5','QtWebEngineWidgets','datetime','twilio.rest','pyowm','json','requests']
                    }
                }
)
