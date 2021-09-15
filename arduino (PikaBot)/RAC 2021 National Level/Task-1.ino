#include"PikaBot.h"

PikaBot bot;

void setup() {
    bot.moveForward(200);
}

void loop() {
    if (bot.ultrasonicDistance() < 8) {
        bot.turnLeft(200, 90);
    } else if (bot.ultrasonicDistance() < 15){
        bot.stop();
    } else {
        bot.moveForward(200);
    }
}
