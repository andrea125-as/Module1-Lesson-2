# Module1-Lesson-2
Arduino LED blinking system using HIGH, LOW, and delay values.

# Arduino LED Monitoring System

## Project Description
This project demonstrates how an Arduino Uno controls an LED using HIGH, LOW, and delay values.

## Components Used
1. Arduino Uno
2. Breadboard
3. LED
4. 220Ω Resistor
5. Jumper Wires

## Wiring Connections
1. Arduino GND → Blue negative rail
2. Arduino D8 → 220Ω resistor
3. Other resistor end → A10
4. LED anode (+) → E10
5. LED cathode (-) → E11
6. A11 → Blue negative rail

## How It Works
- HIGH turns the LED ON.
- LOW turns the LED OFF.
- delay(1000) waits for 1 second.
- delay(200) makes the LED blink faster.
- delay(3000) keeps the LED ON longer.

## Files
- app.py – Streamlit monitoring dashboard.
- sketch.ino – Arduino LED control program.
- README.md – Project documentation.

## Technologies Used
- Arduino
- C++
- Python
- Streamlit
- Pandas
- Wokwi
