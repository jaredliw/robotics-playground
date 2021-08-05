#include "PikaBot.h"

PikaBot bot;

void setup() {
    bot.calibrateMotors(255, 500, 18);  // Edit this line if necessary
}

void loop() {
    for (int i = 0; i < 4; i++) {
        bot.moveForward(255, 20);
        bot.turnRight(90);
    }
}
