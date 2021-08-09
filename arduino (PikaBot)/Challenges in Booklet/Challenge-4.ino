#include "PikaBot.h"

PikaBot bot;

void setup() {
    bot.tempo = 180;
    bot.play("e5:8 e5 r e5 r c5 e5:4 g5");
    delay(1000);
    bot.resetTempo();
    String repeated = "g5:8 g5 g5 g5:16 g5:8 g5:16 g5:8";
    bot.play("d5 e5 " + repeated + " d5 e5 " + repeated + " d5 e5 " + repeated + " g5:8 g5 f5:2");
}

void loop() {
}
