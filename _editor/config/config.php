<?php

declare(strict_types=1);

define('WIKI_TITLE', 'daeun28 wiki');
define('WIKI_DESCRIPTION', '단어를 따라 생각을 고치는 곳');
define('BASE_URL', '');
define('THEME', '');
define('LANGUAGE', 'ko');
define('TIMEZONE', 'Asia/Seoul');
define('HOME_PAGE', '처음');
// Engine runs only during CI export (Vercel/Next.js handles live editing).
// 'private' makes the exporter's anonymous requests get a proper 404 for
// missing pages instead of being redirected into the /edit form, which
// otherwise leaks the editor HTML into the exported static site.
define('EDIT_PERMISSION', 'private');
