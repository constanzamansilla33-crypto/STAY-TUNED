const CACHE_NAME = "stay-tuned-v2";

const ARCHIVOS = [
    "/static/eventos/manifest.json",
    "/static/eventos/css/style.css",
    "/static/eventos/img/icon-192.png",
    "/static/eventos/img/icon-512.png"
];

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ARCHIVOS);
        })
    );

    self.skipWaiting();
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((nombres) => {
            return Promise.all(
                nombres
                    .filter((nombre) =>
                        nombre.startsWith("stay-tuned-") &&
                        nombre !== CACHE_NAME
                    )
                    .map((nombre) => caches.delete(nombre))
            );
        }).then(() => self.clients.claim())
    );
});

self.addEventListener("fetch", (event) => {
    const url = new URL(event.request.url);

    if (event.request.method !== "GET") return;

    if (url.origin !== self.location.origin) return;

    if (!ARCHIVOS.includes(url.pathname)) return;

    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.open(CACHE_NAME).then((cache) => {
                return cache.match(url.pathname);
            });
        })
    );
});