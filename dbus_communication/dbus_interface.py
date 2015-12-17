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
    def get_temperature_settings(cls):
        obj = cls._get_dbus_object()
        return obj.get_temperature_settings(dbus_interface = cls.interface_name)

    @classmethod
    def set_temperature_settings(cls):
        obj = cls._get_dbus_object()
        return obj.set_temperature_settings(dbus_interface = cls.interface_name)

    @classmethod
    def get_manual_mode(cls):
        obj = cls._get_dbus_object()
        return obj.get_manual_mode(dbus_interface = cls.interface_name)

    @classmethod
    def get_schedule_list(cls):
        obj = cls._get_dbus_object()
        return obj.list_schedule_task(dbus_interface = cls.interface_name)

    @classmethod
    def add_schedule_task(cls, task):
        obj = cls._get_dbus_object()
        return obj.add_schedule_task(task, dbus_interface = cls.interface_name)

    @classmethod
    def update_schedule_task(cls, old_task, new_task):
        obj = cls._get_dbus_object()
        return obj.update_schedule_task((old_task, new_task), dbus_interface = cls.interface_name)

    @classmethod
    def remove_schedule_task(cls, task):
        obj = cls._get_dbus_object()
        return obj.remove_schedule_task(task, dbus_interface = cls.interface_name)

    @classmethod
    def _get_dbus_object(cls):
        return cls.bus.get_object(cls.service_name, cls.service_object)
