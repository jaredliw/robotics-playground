#include "PikaBot.h"

PikaBot bot;

void setup() {
}

void loop() {
    // Line follow
    // The robot won't follow the line if the speed is too high,
    // try to maintain the speed below 128
    bot.lineFollow(100);
}
