"""Message type identifiers for raspberry-pi."""

MESSAGE_FAMILY = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/raspberrypi-interactions/1.0"

READ_SENSOR = f"{MESSAGE_FAMILY}/read_sensor"
SENSOR_VALUE = f"{MESSAGE_FAMILY}/sensor_value"
DISPLAY_MESSAGE = f"{MESSAGE_FAMILY}/display_message"
DISPLAY_LETTER = f"{MESSAGE_FAMILY}/display_letter"
SET_PIXELS = f"{MESSAGE_FAMILY}/set_pixels"

MESSAGE_TYPES = {
	READ_SENSOR: "aries_cloudagent.messaging.raspberrypi_interactions." + "messages.read_sensor.ReadSensor",
    SENSOR_VALUE: "aries_cloudagent.messaging.raspberrypi_interactions." +"messages.sensor_value.SensorValue",
    DISPLAY_MESSAGE: "aries_cloudagent.messaging.raspberrypi_interactions." + "messages.display_message.DisplayMessage",
    DISPLAY_LETTER: "aries_cloudagent.messaging.raspberrypi_interactions." + "messages.display_letter.DisplayLetter",
    SET_PIXELS: "aries_cloudagent.messaging.raspberrypi_interactions." + "messages.set_pixels.SetPixels"

}
