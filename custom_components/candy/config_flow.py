"""Config flow for GreenGo integration."""
from __future__ import annotations

import logging
from typing import Any

import async_timeout
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .client import detect_encryption
from .client.decryption import Encryption
from .const import *

_LOGGER = logging.getLogger(__name__)

STEP_DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_IP_ADDRESS): str,
    vol.Required(CONF_KEY_USE_ENCRYPTION, default=True): bool,
    vol.Optional(CONF_PASSWORD): str
})


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Candy."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(
            self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=STEP_DATA_SCHEMA)
            
        return self.async_create_entry(title=CONF_INTEGRATION_TITLE, data=user_input)
