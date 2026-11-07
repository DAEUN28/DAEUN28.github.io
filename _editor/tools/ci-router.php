<?php
// CI-only router for php -S. Strips origin checks that the loopback editor
// needs; this script runs inside a GitHub Actions job that nothing else can
// reach.
$path = rawurldecode((string) parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH));
$root = realpath(__DIR__ . '/..');
if ($root === false) { http_response_code(500); exit; }
$file = realpath($root . $path);
if ($file !== false && str_starts_with($file, $root . '/') && is_file($file) &&
    (str_starts_with($path, '/wikiwikiwiki/assets/') || preg_match('#^/themes/[^/]+/assets/#', $path))) {
    return false;
}
$_SERVER['SCRIPT_NAME'] = '/index.php';
require $root . '/index.php';
