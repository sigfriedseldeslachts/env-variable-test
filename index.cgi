#!/bin/sh
s=$(( $(date +%s) - $(cat /tmp/start) ))

echo "Content-Type: text/html"
echo
echo "<h1>${MESSAGE:-No message set}</h1>"
printf '<p>Uptime: %dd %02dh %02dm %02ds</p>\n' $((s/86400)) $((s%86400/3600)) $((s%3600/60)) $((s%60))
