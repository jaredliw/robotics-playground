#include "PikaBot.h"

PikaBot bot;

void setup() {
    bot.play("e g:8 c:2 r:8 a:4 c5:8 f4:2 b:8 g a b d5:8 c5:2");
}

void loop() {
    bot.lineFollow(80);
}
