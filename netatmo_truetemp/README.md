# Netatmo TrueTemp API Add-on

This add-on runs a local HTTP API that wraps `py-netatmo-truetemp-cli`.

## Configuration
- `username`: Netatmo account username
- `password`: Netatmo account password
- `home_id` (optional): Netatmo Home ID

## API
- `GET /rooms`
- `POST /set_true_temperature`

Designed for local use (Node-RED, automations).

## Home Assistant automation example (optional)

This add-on only exposes a local HTTP API. If you want automatic correction of Netatmo “True Temperature”
based on a reference temperature sensor, you can implement it in Home Assistant.

### Concept
For each room we define 3 template triggers:

- **A (after heating stops):** if heating has been off for 15 minutes AND the valve reading differs from the reference by ≥ 0.5°C
- **B (while heating):** if heating has been on for 15 minutes AND the reference is ≥ 0.5°C warmer than the valve reading
- **C (heating should be on but isn’t):** setpoint is in comfort range (≥ 20°C), the room is cold vs setpoint, and the valve sensor is reading too high

When any trigger fires, we call a generic script that:
- checks window open
- checks cooldown (30 min)
- applies **max step ±1.0°C** per run
- calls the add-on HTTP endpoint `/set`

### Prerequisites
- Create `input_datetime` helpers for cooldown (one per room), e.g. `input_datetime.truetemp_lock_until_entrance`
- Create a `rest_command` (example below) or call the endpoint from Node-RED

### REST command (example)
```yaml
rest_command:
  netatmo_truetemp_set:
    url: "http://homeassistant.local:18199/set"
    method: POST
    headers:
      content-type: "application/json"
    payload: >
      {"room_name":"{{ room_name }}","temperature":{{ temperature }}}
    timeout: 15



Example service call:
action: rest_command.netatmo_truetemp_set
data:
  room_name: "Living Room"
  temperature: 20.4


## Node-RED example

Use an HTTP Request node:

- Method: `POST`
- URL: `http://homeassistant.local:18199/set`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "room_name": "Living Room",
  "temperature": 20.4
}

