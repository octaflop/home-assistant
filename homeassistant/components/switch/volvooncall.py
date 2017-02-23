"""
Support for Volvo heater.

This platform uses the Telldus Live online service.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/switch.volvooncall/
"""
import logging

from homeassistant.components.volvooncall import VolvoEntity
from homeassistant.helpers.entity import ToggleEntity

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup Tellstick switches."""
    if discovery_info is None:
        return
    add_devices([VolvoSwitch(hass, discovery_info)])


class VolvoSwitch(VolvoEntity, ToggleEntity):
    """Representation of a Volvo switch."""

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self.vehicle.is_heater_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self.vehicle.start_heater()

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self.vehicle.stop_heater()

    @property
    def _name(self):
        """Return the name of the switch."""
        return 'Heater'

    @property
    def icon(self):
        """Return the icon."""
        return 'mdi:radiator'