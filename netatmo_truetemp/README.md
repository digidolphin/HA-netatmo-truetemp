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
