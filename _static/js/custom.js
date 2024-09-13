
/* This nonsense is required to make the iframe scroll position restoration
work. On Chrome ( 2024-09-13 ) loading a page in Chrome causes the mouse
position to be placed in each of the iframes, causing, the page to scroll down.
This hack just scrolls the page back to the top. */

document.addEventListener("DOMContentLoaded", function () {
    let scrollPosition = 0;
    console.log("Foreach Iframe")
    document.querySelectorAll("iframe").forEach(iframe => {
        // Log when the mouse enters the iframe
        //iframe.addEventListener("mouseenter", () => {
        //    scrollPosition = window.scrollY;
        //    console.log(`Mouse entered iframe. Current scroll position saved: ${scrollPosition}`);
        //});

        // Log when the iframe finishes loading and scroll position is restored
        iframe.addEventListener("load", () => {
            console.log(`Iframe loaded. Restoring scroll position to: ${scrollPosition}`);
            window.scrollTo(0, scrollPosition);
        });
    });
});

