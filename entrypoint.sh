echo "Docker container has been started"
echo "*/5 * * * * cd /home/scraper && $(which python3) src/scraper.py >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt
crontab scheduler.txt
cron -f