// src/remove-ads-iframe.ts

(function() {
    setInterval(() => {
        document.querySelectorAll('iframe').forEach((iframe: HTMLIFrameElement) => {
            let src = iframe.getAttribute('src');
            if (src && src.includes("ads-iframe")) {
                iframe.remove();
            }
        });
    }, 300);
})();
