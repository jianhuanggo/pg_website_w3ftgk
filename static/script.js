// animate webpage title
let originalTitle = document.title;
let title = originalTitle;
let position = 0;

let spacer = " ".repeat(1);
title = spacer + title + spacer;

function animateTitle() {
    document.title = title.slice(position);
    position++;
    if (position >= title.length - 1) {
        position = 0;
    }
}

setInterval(animateTitle, 200);