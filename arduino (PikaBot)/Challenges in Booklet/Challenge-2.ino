#include"PikaBot.h"

PikaBot bot;

void setup() {
    bot.moveForward(255);
}

void loop() {
    if (bot.ultrasonicDistance() <= 20) {
        bot.turnLeft(255, 90);
    } else {
        bot.moveForward(255);
    }
}
