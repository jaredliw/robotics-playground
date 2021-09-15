#include"PikaBot.h"

PikaBot bot;

void setup() {
}

void loop() {
    if (bot.isPressed()) {
        bot.moveForward(255, 37);
        bot.move(0,-255);
        delay(500);
        bot.stop();
        bot.moveBackward(255, 30);
        while (true) {;}
    }
}
