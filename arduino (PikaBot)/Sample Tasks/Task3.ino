#include "PikaBot.h"

PikaBot bot;
long startTime;

void setup() {
    startTime = millis();
    bot.turnLeft(255);
}

void loop() {
    if (millis() - startTime > 10000) {
        bot.stop();
        while (true) {
            ;
        }
    } else {
        bot.playTone("C", 4);
    }
}
