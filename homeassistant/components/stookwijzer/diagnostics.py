"""Diagnostics support for Stookwijzer."""
from __future__ import annotations

from typing import Any

from stookwijzer import Stookwijzer

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    client: Stookwijzer = hass.data[DOMAIN][entry.entry_id]

    last_updated = None
    if client.last_updated:
        last_updated = client.last_updated.isoformat()

    return {
        "state": client.state,
        "last_updated": last_updated,
        "alert": client.alert,
        "air_quality_index": client.lki,
        "windspeed_bft": client.windspeed_bft,
        "windspeed_ms": client.windspeed_ms,
        "forecast": client.forecast,
    }
