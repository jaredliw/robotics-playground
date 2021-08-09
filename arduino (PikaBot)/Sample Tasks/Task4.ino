#include "PikaBot.h"

PikaBot bot;
long startTime;

void setup() {
    startTime = millis();
}

void loop() {
    if (millis() - startTime > 10) {
        bot.stop();
        while (true) {
            ;
        }
    } else {
        bot.lineFollow();
    }
}
