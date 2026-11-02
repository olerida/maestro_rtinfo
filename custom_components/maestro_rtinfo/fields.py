"""Extract scalar fields without exposing credentials or identifiers."""
from dataclasses import fields, is_dataclass
import re

# Network identifiers and account/device credentials are not telemetry.
PRIVATE = re.compile(r"password|passwd|pwd|secret|token|credential|ssid|mac_wifi|(?:^|_)serial|(?:^|_)sn$|unique.?code", re.I)
# Fields supported by app code, the existing integration, or observed device data.
# A label alone does not make an undocumented field confirmed.
CONFIRMED_FIELDS = frozenset({
    "pos_ric_flu", "pos_ric_pel", "mod_ada_on", "pul_brac", "att_eco",
    "ingr_amb", "sens_liv_pellet", "adaptive_on", "potenza_att",
    "potenza_counter", "t_dur_pul", "t_int_pul", "set_pot_man", "pressione",
    "pressione_imp", "state", "state_duration", "mode", "is_connected",
    "is_in_error", "last_alarm", "crono_enabled", "silent_enabled",
    "sleep_enabled", "clean_in_prog", "clean_air_in_prog", "ore_prox_manut",
    "index_vel_v1", "index_vel_v2", "index_vel_v3", "set_amb1", "set_amb2",
    "set_amb3", "temp_fumi", "temp_scheda", "vel_real_ventola_fumi",
    "vel_imp_ventola_fumi", "vel_real_coclea", "vel_imp_coclea",
    "temp_caldaia", "temp_bollitore", "temp_puffer",
})
LABELS = {
    "pos_ric_flu": ("Receta activo", None, None),
    "pos_ric_pel": ("Receta pellet", None, None),
    "mod_ada_on": ("Receta modo de adaptación", None, None),
    "pul_brac": ("Matic", None, None),
    "att_eco": ("Start/Stop", None, None),
    "ingr_amb": ("T.EXT", None, None),
    "sens_liv_pellet": ("Sensor de nivel de pellet", None, None),
    "adaptive_on": ("Modo de adaptación activo", None, None),
    "potenza_att": ("Potencia activa", None, None),
    "potenza_counter": ("Duración de la potencia activa", None, None),
    "t_dur_pul": ("Duración prevista de limpieza del brasero", "s", None),
    "set_pot_man": ("Nivel de potencia manual seleccionado", None, None),
    "pressione": ("Activo real", None, None),
    "pressione_imp": ("Activo establecido", None, None),
    "t_int_pul": ("Tiempo restante hasta limpieza del brasero", "s", None),
    "state": ("Estado de la estufa", None, None),
    "state_duration": ("Duración del estado", None, None),
    "mode": ("Modo de funcionamiento", None, None),
    "is_connected": ("Estufa conectada", None, None),
    "is_in_error": ("Error de la estufa", None, None),
    "last_alarm": ("Última alarma", None, None),
    "crono_enabled": ("Programación horaria activada", None, None),
    "silent_enabled": ("Modo silencioso activado", None, None),
    "sleep_enabled": ("Modo descanso activado", None, None),
    "clean_in_prog": ("Limpieza en curso", None, None),
    "clean_air_in_prog": ("Limpieza del aire en curso", None, None),
    "ore_prox_manut": ("Horas hasta el próximo mantenimiento", None, None),
    "index_vel_v1": ("Nivel de ventilación 1", None, None),
    "index_vel_v2": ("Nivel de ventilación 2", None, None),
    "index_vel_v3": ("Nivel de ventilación 3", None, None),
    "set_amb1": ("Temperatura ambiente objetivo 1", None, None),
    "set_amb2": ("Temperatura ambiente objetivo 2", None, None),
    "set_amb3": ("Temperatura ambiente objetivo 3", None, None),
    "temp_fumi": ("Temperatura de humos", "°C", "temperature"),
    "temp_scheda": ("Temperatura de la placa", "°C", "temperature"),
    "vel_real_ventola_fumi": ("Velocidad real del extractor de humos", "rpm", None),
    "vel_imp_ventola_fumi": ("Velocidad solicitada del extractor de humos", "rpm", None),
    "vel_real_coclea": ("Velocidad real del sinfín", "rpm", None),
    "vel_imp_coclea": ("Velocidad solicitada del sinfín", "rpm", None),
    "temp_caldaia": ("Temperatura de la caldera", "°C", "temperature"),
    "temp_bollitore": ("Temperatura del acumulador", "°C", "temperature"),
    "temp_puffer": ("Temperatura del depósito de inercia", "°C", "temperature"),
}


def values(obj):
    if obj is None:
        return {}
    if isinstance(obj, dict):
        data = obj
    elif is_dataclass(obj):
        data = {field.name: getattr(obj, field.name, None) for field in fields(obj)}
    else:
        data = vars(obj)
    result = {}
    for key, value in data.items():
        if key == "unknown_fields" and isinstance(value, dict):
            result.update(values(value))
        elif isinstance(key, str) and not key.startswith("_") and not PRIVATE.search(key) and isinstance(value, (str, int, float, bool)):
            # HA's state limit is 255 characters; containers and empty values are skipped.
            if not isinstance(value, str) or len(value) <= 255:
                result[key] = value
    return result


def snapshot(stove):
    # State wins, matching the legacy integration; Status supplies remaining fields.
    result = values(getattr(stove, "Status", None))
    result.update(values(getattr(stove, "State", None)))
    return result
