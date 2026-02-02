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

## Home Assistant REST example (optional)

If you want to call the API directly from Home Assistant (without Node-RED),
you can define a `rest_command`:

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

