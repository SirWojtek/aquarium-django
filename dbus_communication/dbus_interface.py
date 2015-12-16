from dbus import SessionBus

class Dbus:
    service_name = 'org.romek.service'
    service_object = '/org/romek/service'
    interface_name = 'org.romek.interface'

    bus = SessionBus()

    @classmethod
    def get_temperature_status(cls):
        obj = cls._get_dbus_object()
        return obj.get_temperature_status(dbus_interface = cls.interface_name)

    @classmethod
    def get_schedule_list(cls):
        obj = cls._get_dbus_object()
        return obj.list_schedule_task(dbus_interface = cls.interface_name)

    @classmethod
    def add_schedule_task(cls, task):
        obj = cls._get_dbus_object()
        return obj.add_schedule_task(task, dbus_interface = cls.interface_name)

    @classmethod
    def _get_dbus_object(cls):
        return cls.bus.get_object(cls.service_name, cls.service_object)

# def _get_dbus_session(request):
#     if not request.session.get('dbus'):
#         request.session['dbus'] = dbus.SessionBus()
#     return request.session['dbus']
