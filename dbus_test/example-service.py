#!/usr/bin/env python

usage = """Usage:
python example-service.py &
python example-client.py
python example-async-client.py
python example-client.py --exit-service
"""

# Copyright (C) 2004-2006 Red Hat Inc. <http://www.redhat.com/>
# Copyright (C) 2005-2007 Collabora Ltd. <http://www.collabora.co.uk/>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import gi.repository.GLib as gobject

import dbus
import dbus.service
import dbus.mainloop.glib

class SomeObject(dbus.service.Object):

    @dbus.service.method("com.biometria.HeadInterface",
                         in_signature='', out_signature='')
    def Exit(self):
        mainloop.quit()

    @dbus.service.method("com.biometria.HeadInterface",
                         in_signature='', out_signature='')
    def process_task(self,task):
        print(task['task'])


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    session_bus = dbus.SessionBus()
    name = dbus.service.BusName("com.biometria.HeadService", session_bus)
    object = SomeObject(session_bus, '/SomeObject')

    mainloop = gobject.MainLoop()
    print ("Running example service.")
    mainloop.run()
