// Service Worker for PORK UP Website
const CACHE_NAME = 'porkup-website-v1.0';
const urlsToCache = [
  '/',
  '/gioi-thieu',
  '/san-pham',
  '/lien-he',
  '/static/style.css',
  '/static/LOGO.png',
  '/static/STANDEE.png',
  '/static/banner.png',
  '/static/banner_1.png',
  '/static/banner_2.png',
  '/static/banner_4.jpg',
  '/static/dk_1.jpg',
  '/static/dk_2.jpg'
];

// Install event - cache resources
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event - serve from cache
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Return cached version or fetch from network
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
