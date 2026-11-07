<?php
// CI-only: seed a throwaway admin so engine boot clears the install-first
// gate. Password is random per-run and never printed; the user file is
// written to _editor/users/ which is gitignored.
declare(strict_types=1);
chdir(__DIR__ . '/..');
require_once __DIR__ . '/../wikiwikiwiki/src/bootstrap.php';
if (user_count() > 0) { fwrite(STDERR, "ci-seed-user: skip, user exists\n"); exit(0); }
$hash = password_hash(bin2hex(random_bytes(32)), PASSWORD_BCRYPT);
$ok = user_create('ci-bot', [
    'username' => 'ci-bot',
    'password_hash' => $hash,
    'role' => 'admin',
    'created_at' => time(),
]);
if (!$ok) { fwrite(STDERR, "ci-seed-user: user_create failed\n"); exit(1); }
fwrite(STDERR, "ci-seed-user: seeded ci-bot\n");
