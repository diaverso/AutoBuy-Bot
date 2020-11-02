while :
do
 python3 bot.py || echo "No funciono... Reiniciando..." >&2
 sleep 1
 pgrep chrome | xargs kill -9
 echo "Press Ctrl-C to quit." && sleep 1
done
